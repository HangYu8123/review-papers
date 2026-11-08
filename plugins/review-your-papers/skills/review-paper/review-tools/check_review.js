#!/usr/bin/env node
// Checks a review-data.js against the format of review_template/review.html, guideline.md, and the
// reviewing voice of the review-paper skill. Shared by the review-paper and advisor-review-paper skills.
//
//   node check_review.js <path/to/review-data.js>
//
// ERROR  the page or import_review.py would fail, or a link points nowhere. Fix these.
// WARN   a guideline or style rule looks broken. Fix it, or keep it for a reason.
// NOTE   worth a look, often fine.
// Exits with 1 when there is an error.
'use strict';

const fs = require('fs');

const GROUPS = ['summary', 'strength', 'weakness', 'improvement', 'recommendation'];
const CATEGORIES = {
  strength: ['Technical novelty and innovation', 'Significance of contributions',
    'Experimental rigor and validation', 'Clarity of presentation'],
  weakness: ['Unclear contributions', 'Insufficient evidence for claims',
    'Technical limitations or concerns', 'Missing comparisons or related work'],
};
const SOURCES = ['claims', 'method', 'experiments', 'baselines', 'presentation', 'prior', 'field',
  'guideline', 'previous', 'style', 'summary', 'strength', 'weakness', 'improvement'];
const EXTERNAL = ['prior', 'field'];
const ROLES = ['intuition', 'contribution', 'work', 'experiment', 'context'];
const KINDS = ['start', 'end', 'choice', 'state'];

// The same tests the page runs on the kept points.
const BASELINE_LIKE = /baselines?\b|recent (work|method|approach)|more recent|newer (work|method)/i;
const NOT_EXPERT = /not an expert|would not (argue|defend)/i;

// Wording to review in assistant drafts. The portable guide also records terms
// Hang uses, so words such as moreover and leverage are not blanket errors.
const AI_WORDS = [
  /\bdelv(e|es|ed|ing)\b/i, /\bshowcas(e|es|ed|ing)\b/i, /\bpivotal\b/i,
  /\bcrucial(ly)?\b/i, /\bnotably\b/i, /\bseamless(ly)?\b/i, /\bgroundbreaking\b/i,
  /\brealm\b/i, /\bholistic\b/i, /\bunderscor(e|es|ed|ing)\b/i, /\ba testament to\b/i,
  /\bit is worth noting\b/i, /\bplays? a vital role\b/i,
  /\belegant(ly)?\b/i, /\bparadigm shift\b/i,
];

const out = { ERROR: [], WARN: [], NOTE: [] };
const report = function (level, where, msg) { out[level].push((where ? where + ': ' : '') + msg); };

function load(path) {
  let text;
  try { text = fs.readFileSync(path, 'utf8'); } catch (e) { console.error('Cannot read ' + path); process.exit(1); }
  const a = text.indexOf('{');
  const b = text.lastIndexOf('}');
  if (a < 0 || b < a) { console.error('No object found between braces in ' + path); process.exit(1); }
  if (!/window\.REVIEW_DATA\s*=/.test(text.slice(0, a))) report('ERROR', '', 'The file should assign window.REVIEW_DATA = { ... }.');
  try { return JSON.parse(text.slice(a, b + 1)); } catch (e) {
    console.error('ERROR: the part between the first { and the last } is not strict JSON. ' + e.message);
    const m = /position (\d+)/.exec(e.message);
    if (m) {
      const pos = a + Number(m[1]);
      const line = text.slice(0, pos).split('\n').length;
      console.error('Near line ' + line + ': ' + text.slice(Math.max(a, pos - 60), pos + 60).replace(/\n/g, ' '));
    }
    process.exit(1);
  }
}

function words(s) { return (s.match(/\S+/g) || []).length; }

// A style heuristic, not a parser: ignore decimal points, initials, and the
// paper-reference abbreviations that otherwise inflate sentence counts.
function sentences(s) {
  const normalized = s.replace(/\b(?:Eq|Eqs|Fig|Figs|Sec|Secs|Dr|Mr|Ms|Prof|vs|e\.g|i\.e)\./gi, 'ref')
    .replace(/\bp\.\s*(?=\d)/gi, 'page ')
    .replace(/\b[A-Z]\.(?=\s*[A-Z])/g, 'initial')
    .replace(/(\d)\.(?=\d)/g, '$1decimal');
  return normalized.split(/[.!?]+(?:["'\u2019\u201d)]*)(?:\s+|$)/).filter(function (part) { return part.trim(); }).length;
}

function checkStyle(it) {
  const t = it.revised || '';
  const id = it.id;
  if (/—/.test(t)) report('WARN', id, 'Has an em dash. Use a comma, a which clause, or a new sentence.');
  if (/\s–\s/.test(t)) report('WARN', id, 'Has an en dash used as a dash. Use a comma, a which clause, or a new sentence.');
  const semis = (t.match(/;/g) || []).length;
  if (semis) report('WARN', id, semis + ' semicolon' + (semis > 1 ? 's' : '') + '. State the relation in words, or start a new sentence.');
  // Colons, leaving out times and ratios such as 3:1, and a colon right before a quotation.
  const colons = (t.replace(/\d:\d/g, '').match(/:(?!\s*["“])/g) || []).length;
  if (colons > 1) report('WARN', id, colons + ' colons. Keep a colon only before a list or a quotation.');
  else if (colons === 1 && !/:\s*(\n|a\.|1\.|\()/.test(t)) report('NOTE', id, 'Has a colon. Keep it only before a list or a quotation.');
  AI_WORDS.forEach(function (re) {
    const m = t.match(re);
    if (m) report('WARN', id, 'Uses "' + m[0] + '", which reads as AI-written.');
  });
  if (/!/.test(t)) report('WARN', id, 'Has an exclamation mark.');
  if (/\bsignificant(ly)?\b/i.test(t)) report('NOTE', id, 'Says significant. Keep it only for a tested statistical claim, or for the paper\'s own test.');
  if (/\b(equivalent|as good as|on par with|identical performance)\b/i.test(t)) report('NOTE', id, 'Claims equivalence. Write similar unless an equivalence test was run.');
  if (/\bwe\b/i.test(t) && it.group !== 'summary') report('NOTE', id, 'Uses "we". The reviewer is "I", and the authors are "the authors".');
  if (/\b(as far as I know|new to me|to me,|I (?:worked through|checked|verified|went through)|I would (?:still )?love to see)\b/i.test(t)) {
    report('WARN', id, 'Has a conversational hedge or review-process narration. State the supported point and move checks or search limits into the evidence.');
  }
  const firstPerson = (t.match(/\b(?:I|me|my)\b/gi) || []).length;
  if (it.group !== 'recommendation' && firstPerson > 1) report('NOTE', id, 'Repeated first person. Prefer the authors, method, or results as the subject.');
  const n = words(t);
  if (it.group === 'strength' && (n > 60 || sentences(t) > 2)) {
    report('WARN', id, n + ' words and about ' + sentences(t) + ' sentences. Strengths usually need one or two sentences and one supporting fact. Move detail into the evidence.');
  } else if ((it.group === 'weakness' || it.group === 'improvement') && n > 100) {
    report('NOTE', id, n + ' words. Keep one concern and one decisive example; move additional support into the evidence.');
  }
}

function checkItems(data) {
  const items = data.items;
  const ids = {};
  const byGroup = {};
  GROUPS.forEach(function (g) { byGroup[g] = []; });
  let lastGroup = 0;
  items.forEach(function (it, i) {
    const where = it.id || ('item ' + (i + 1));
    if (!it.id) report('ERROR', where, 'Has no id.');
    else if (ids[it.id]) report('ERROR', where, 'The id is used twice.');
    ids[it.id] = it;
    const gi = GROUPS.indexOf(it.group);
    if (gi < 0) { report('ERROR', where, 'Has the group "' + it.group + '". Use one of ' + GROUPS.join(', ') + '.'); return; }
    if (gi < lastGroup) report('WARN', where, 'Is out of section order (summary, strength, weakness, improvement, recommendation).');
    lastGroup = Math.max(lastGroup, gi);
    byGroup[it.group].push(it);
    if (typeof it.revised !== 'string' || !it.revised.trim()) report('ERROR', where, 'Has no review text in revised.');
    if (it.type !== 'review') report('WARN', where, 'type should be "review".');
    if (it.op !== 'insert') report('WARN', where, 'op should be "insert".');
    if (it.id && it.group && it.id.indexOf(it.group + '-') !== 0) report('NOTE', where, 'Ids usually start with the group, such as ' + it.group + '-1.');

    if (it.category != null) {
      if (it.group === 'summary' || it.group === 'recommendation') report('WARN', where, 'Has a category. Leave it out of summary and recommendation.');
      else if (CATEGORIES[it.group] && CATEGORIES[it.group].indexOf(it.category) < 0) {
        report('NOTE', where, 'Category "' + it.category + '" is not one of the names in the template: ' + CATEGORIES[it.group].join(', ') + '.');
      }
    }

    const ev = it.evidence;
    if (ev == null || (Array.isArray(ev) && !ev.length)) {
      report(it.group === 'summary' || it.group === 'recommendation' ? 'NOTE' : 'WARN', where, 'Has no evidence. Hang decides from the evidence under each point.');
    } else if (!Array.isArray(ev)) {
      report('ERROR', where, 'evidence must be a list.');
    } else {
      if (ev.length > 6) report('NOTE', where, ev.length + ' references. One to five is usually enough.');
      ev.forEach(function (e, j) {
        const w = where + ' evidence ' + (j + 1);
        ['where', 'text', 'reason'].forEach(function (k) {
          if (typeof e[k] !== 'string' || !e[k].trim()) report('WARN', w, 'Has no ' + k + '.');
        });
        if (!e.source) report('WARN', w, 'Has no source, so the Connections tab cannot count it.');
        else if (SOURCES.indexOf(e.source) < 0) report('WARN', w, 'Has the source "' + e.source + '". Use one of ' + SOURCES.join(', ') + '.');
        if (EXTERNAL.indexOf(e.source) >= 0 && !e.url) report('WARN', w, 'Is an external source with no url.');
        if (e.url && !/^https?:\/\//.test(e.url)) report('WARN', w, 'url should start with http:// or https://.');
      });
    }
    checkStyle(it);
  });

  // Section rules from guideline.md, as the page checks them.
  const n = function (g) { return byGroup[g].length; };
  if (!n('summary')) report('ERROR', 'summary', 'There is no summary.');
  if (n('summary') > 2) report('WARN', 'summary', n('summary') + ' paragraphs. One or two is usual.');
  const summaryWords = words(byGroup.summary.map(function (it) { return it.revised || ''; }).join(' '));
  if (summaryWords > 140) report('WARN', 'summary', summaryWords + ' words. Usually keep the whole summary to 80 to 140 words.');
  if (n('summary') > 1) {
    const second = byGroup.summary[1].revised || '';
    if (sentences(second) > 2 || words(second) > 45) {
      report('WARN', byGroup.summary[1].id, 'Keep the second summary paragraph to one or two sentences, usually 45 words or fewer.');
    }
  }
  if (n('summary') && !/^In this work, the authors\b/.test(byGroup.summary[0].revised || '')) {
    report('NOTE', 'summary', 'Hang\'s summaries usually open with "In this work, the authors ...".');
  }
  if (n('strength') < 2) report('WARN', 'strength', n('strength') + ' points. Three to six is usual.');
  if (n('strength') > 7) report('NOTE', 'strength', n('strength') + ' points. Three to six is usual.');
  if (n('weakness') < 2) report('WARN', 'weakness', n('weakness') + ' points. Three to five is usual.');
  if (n('weakness') > 6) report('WARN', 'weakness', n('weakness') + ' points. Leave out the minor ones, as the guideline asks.');
  const baselineLike = byGroup.weakness.filter(function (it) { return BASELINE_LIKE.test(it.revised || ''); });
  if (baselineLike.length > 2) {
    report('WARN', 'weakness', baselineLike.length + ' points look like more baselines or more recent work (' +
      baselineLike.map(function (it) { return it.id; }).join(', ') + '). The guideline allows at most two, and the page flags this too.');
  }
  if (n('improvement') < 1 || n('improvement') > 2) report('WARN', 'improvement', n('improvement') + ' points. The guideline asks for one or two.');
  if (n('recommendation') !== 1) report('WARN', 'recommendation', n('recommendation') + ' paragraphs. One is usual.');
  if (n('recommendation') && !byGroup.recommendation.some(function (it) { return NOT_EXPERT.test(it.revised || ''); })) {
    report('WARN', 'recommendation', 'The not-an-expert line is missing.');
  }
  GROUPS.forEach(function (g) {
    const withCat = byGroup[g].filter(function (it) { return it.category != null; }).length;
    if (withCat && byGroup[g].length <= 2 && g !== 'summary' && g !== 'recommendation') {
      report('NOTE', g, 'Has categories with only ' + byGroup[g].length + ' points. The template leaves them out for one or two points.');
    }
    if (withCat && withCat < byGroup[g].length) report('NOTE', g, withCat + ' of ' + byGroup[g].length + ' points have a category.');
  });
  return ids;
}

function checkMachine(data, ids) {
  const m = data.machine;
  if (!m || !Array.isArray(m.states) || !m.states.length) { report('WARN', 'machine', 'There is no state machine yet.'); return; }
  if (!m.title) report('WARN', 'machine', 'Has no title.');
  if (!m.caption) report('WARN', 'machine', 'Has no caption.');
  const byId = {};
  let lastRole = 0;
  const roleCount = {};
  m.states.forEach(function (s, i) {
    const where = 'state ' + (s.id || (i + 1));
    if (!s.id) report('ERROR', where, 'Has no id.');
    else if (byId[s.id]) report('ERROR', where, 'The id is used twice.');
    byId[s.id] = { s: s, index: i, out: [] };
    if (!s.label) report('ERROR', where, 'Has no label.');
    else if (s.label.length > 32) report('NOTE', where, 'Label has ' + s.label.length + ' characters. About 28 at most fits the box.');
    if (s.role != null) {
      const ri = ROLES.indexOf(s.role);
      if (ri < 0) report('ERROR', where, 'Has the role "' + s.role + '". Use one of ' + ROLES.join(', ') + '.');
      else {
        if (ri < lastRole) report('WARN', where, 'Is listed after a later role. List states by role: ' + ROLES.join(', ') + '.');
        lastRole = Math.max(lastRole, ri);
        roleCount[s.role] = (roleCount[s.role] || 0) + 1;
      }
      if (s.kind != null && s.kind !== 'state') report('NOTE', where, 'Has a kind and a role. The template says to leave kind out when role is set.');
      if (s.role === 'experiment' && !s.sub) report('WARN', where, 'An experiment needs a sub line with the environment and total workload.');
      if (s.role === 'work' && !s.where) report('NOTE', where, 'A work state should say where it is in the paper.');
    }
    if (s.kind != null && KINDS.indexOf(s.kind) < 0) report('ERROR', where, 'Has the kind "' + s.kind + '". Use one of ' + KINDS.join(', ') + '.');
    (s.points || []).forEach(function (p) {
      if (!ids[p]) report('ERROR', where, 'Links to the review point "' + p + '", which does not exist.');
    });
  });

  (m.transitions || []).forEach(function (t, i) {
    const where = 'transition ' + (i + 1) + ' (' + t.from + ' to ' + t.to + ')';
    if (!byId[t.from]) report('ERROR', where, 'from names no state.');
    if (!byId[t.to]) report('ERROR', where, 'to names no state.');
    if (!byId[t.from] || !byId[t.to]) return;
    byId[t.from].out.push(t);
    if (byId[t.to].index <= byId[t.from].index) report('NOTE', where, 'Runs up the list, so it is drawn as a loop.');
    if (t.label && t.label.length > 30) report('NOTE', where, 'The label is long. Keep edge labels to a few words.');
  });

  const n = m.states.length;
  if (n < 8 || n > 16) report('NOTE', 'machine', n + ' states. About 8 to 16 is usual.');
  const hasRoles = Object.keys(roleCount).length > 0;
  if (!hasRoles) { report('WARN', 'machine', 'No state has a role, so the page draws it as a pipeline. The guideline asks to map the argument.'); return; }
  const ic = roleCount.intuition || 0;
  const cc = roleCount.contribution || 0;
  if (ic < 1 || ic > 2) report('WARN', 'machine', ic + ' intuition states. Use one, two at most.');
  if (cc < 2 || cc > 4) report('WARN', 'machine', cc + ' contribution states. Two to four is usual.');
  if (!roleCount.experiment) report('WARN', 'machine', 'There are no experiment states.');

  const roleOf = function (id) { return byId[id] ? byId[id].s.role : null; };
  m.states.filter(function (s) { return s.role === 'contribution'; }).forEach(function (c) {
    const out = byId[c.id].out;
    const work = out.filter(function (t) { return roleOf(t.to) === 'work'; });
    if (!work.length) report('WARN', 'state ' + c.id, 'This contribution has no work state under it.');
    const reach = out.filter(function (t) { return roleOf(t.to) === 'experiment'; });
    work.forEach(function (t) {
      byId[t.to].out.forEach(function (u) { if (roleOf(u.to) === 'experiment') reach.push({ weak: t.weak || u.weak }); });
    });
    if (!reach.length) report('WARN', 'state ' + c.id, 'No experiment backs this contribution. If that is true, say so in a weakness.');
    else if (reach.every(function (t) { return t.weak; })) report('NOTE', 'state ' + c.id, 'Only weak links back this contribution.');
  });
  const linked = m.states.filter(function (s) { return (s.points || []).length; }).length;
  if (linked < Math.ceil(n / 2)) report('NOTE', 'machine', 'Only ' + linked + ' of ' + n + ' states link to review points.');
  const weakEdges = (m.transitions || []).filter(function (t) { return t.weak; }).length;
  const weaknesses = Object.keys(ids).filter(function (k) { return ids[k] && ids[k].group === 'weakness'; }).length;
  if (weaknesses && !weakEdges) report('NOTE', 'machine', 'No transition is marked weak, although the review has weaknesses. Check whether one of them is about weak support.');
}

function main() {
  const path = process.argv[2];
  if (!path) { console.error('Usage: node check_review.js <path/to/review-data.js>'); process.exit(2); }
  const data = load(path);
  if (!data || !Array.isArray(data.items)) { console.error('ERROR: there is no list of items.'); process.exit(1); }
  if (!data.review_id) report('ERROR', '', 'There is no review_id.');
  if (!data.title) report('WARN', '', 'There is no title.');
  if (!data.generated || isNaN(new Date(data.generated))) report('NOTE', '', 'generated is missing or not a date.');
  if (!data.paper || !data.paper.venue) report('NOTE', '', 'paper.venue is missing.');
  const ids = checkItems(data);
  checkMachine(data, ids);

  const counts = GROUPS.map(function (g) { return data.items.filter(function (it) { return it.group === g; }).length + ' ' + g; });
  console.log('Checked ' + path);
  console.log('Items: ' + counts.join(', ') + '. Machine: ' + ((data.machine && data.machine.states) || []).length + ' states.');
  ['ERROR', 'WARN', 'NOTE'].forEach(function (level) {
    if (!out[level].length) return;
    console.log('\n' + level + ' (' + out[level].length + ')');
    out[level].forEach(function (line) { console.log('  ' + line); });
  });
  if (!out.ERROR.length && !out.WARN.length) console.log('\nNo errors or warnings.');
  process.exit(out.ERROR.length ? 1 : 0);
}

main();
