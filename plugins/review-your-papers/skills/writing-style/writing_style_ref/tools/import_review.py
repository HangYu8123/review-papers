"""Copy the decisions of a review into sources/review-decisions.json.

The style reference cites what Hang accepted, edited, or declined in a review.
Review folders are removed once a review is finished, so the suggested wording,
the decision, Hang's final wording, and any note Hang left are kept here.

    python writing_style_ref/tools/import_review.py <review folder> [--prefix P-] [decisions file ...]

The folder can be under waiting_for_review/ or elsewhere, such as the talk's
wait_to_review/ folder. Without a decisions file, every *.decisions.*.json in the
folder is read in name order, and a later batch replaces an earlier decision on
the same item. Importing a review again replaces its earlier copy.

A decision saved with a decision_source (assistant-delegated or inferred) was not
made by Hang, and the reference gives it no weight. --prefix is put in front of
every item id, for a review whose ids repeat those of another review.
"""

import hashlib
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parent
SNAPSHOT = HERE / 'sources' / 'review-decisions.json'


def read_js(path):
    text = path.read_text(encoding='utf-8')
    return json.loads(text[text.index('{'):text.rindex('}') + 1])


def document(data):
    files = {it.get('file', '') for it in data['items']}
    if 'film' in data['review_id']:
        return 'film text'
    if any(f.endswith('.pptx') for f in files):
        return 'slides'
    return 'dissertation'


def main(argv):
    args = list(argv)
    prefix = ''
    if '--prefix' in args:
        i = args.index('--prefix')
        prefix = args[i + 1]
        del args[i:i + 2]
    if not args:
        raise SystemExit(__doc__)
    folder = Path(args[0])
    if not folder.is_absolute():
        folder = ROOT / folder
    folder = folder.resolve()
    data = read_js(folder / 'review-data.js')
    files = [Path(a) if Path(a).is_absolute() else ROOT / a for a in args[1:]]
    if not files:
        files = sorted(folder.glob('*.decisions.*.json'))
    if not files:
        raise SystemExit('No decisions file in ' + str(folder))

    decisions, batches = {}, []
    for path in files:
        batch = json.loads(path.read_text(encoding='utf-8'))
        if batch['review_id'] != data['review_id']:
            raise SystemExit(path.name + ' belongs to another review.')
        source = batch.get('decision_source') or 'hang'
        batches.append({'file': path.name, 'saved_at': batch['saved_at'], 'source': source,
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
        for d in batch['decisions']:
            decisions[d['id']] = dict(d, source=d.get('decision_source') or source)

    items, stale = [], []
    for it in data['items']:
        d = decisions.get(it['id'])
        if d is None or d['status'] not in ('accepted', 'rejected'):
            continue
        if d.get('hash') != it.get('hash'):
            stale.append(it['id'])
        accepted = d['status'] == 'accepted'
        edited = accepted and 'revised_override' in d
        record = {
            'id': prefix + it['id'], 'type': it['type'], 'group': it.get('group', ''), 'file': it.get('file', ''),
            'line': it.get('line'), 'op': it['op'], 'title': it.get('title', ''), 'note': it.get('note', ''),
            'where': it.get('where', ''), 'original': it.get('original', ''), 'anchor': it.get('anchor', ''),
            'suggested': it.get('revised', ''), 'status': d['status'], 'edited': edited,
            'final': (d['revised_override'] if edited else it.get('revised', '')) if accepted else None,
            'decided_at': d['decided_at'], 'source': d['source'],
            # A comment saved with Hang's decision is Hang's note. A delegated decision's comment is the assistant's reason.
            'comment': d.get('comment', ''),
        }
        if prefix:
            record['item_id'] = it['id']
        if it.get('slide') is not None:
            record['slide'] = it['slide']
        items.append(record)
    if stale:
        raise SystemExit('The suggestion changed after the decision was made: ' + ', '.join(stale))

    by_hang = [i for i in items if i['source'] == 'hang']
    groups = data.get('groups', [])
    if groups and isinstance(groups[0], str):
        groups = [{'key': g, 'label': g} for g in groups]
    review = {
        'review_id': data['review_id'], 'title': data['title'], 'built': data.get('generated', ''),
        'folder': os.path.relpath(str(folder), str(ROOT)).replace('\\', '/'),
        'document': document(data), 'prefix': prefix, 'batches': batches,
        'counts': {
            'items': len(data['items']), 'decided': len(items),
            'accepted': sum(i['status'] == 'accepted' for i in items),
            'edited': sum(i['edited'] for i in items),
            'declined': sum(i['status'] == 'rejected' for i in items),
            'by_hang': len(by_hang),
            'hang_notes': sum(bool(i['comment']) for i in by_hang),
        },
        'types': {k: (v['label'] if isinstance(v, dict) else v) for k, v in data.get('types', {}).items()},
        'groups': groups, 'labels': data.get('labels', {}), 'items': items,
    }
    snapshot = {'schema': 'style-review-snapshot/2', 'reviews': []}
    if SNAPSHOT.exists():
        snapshot = json.loads(SNAPSHOT.read_text(encoding='utf-8'))
        snapshot['schema'] = 'style-review-snapshot/2'
    snapshot['reviews'] = [r for r in snapshot['reviews'] if r['review_id'] != review['review_id']] + [review]
    SNAPSHOT.write_text(json.dumps(snapshot, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = review['counts']
    print('Imported {}: {} decisions ({} accepted, {} of them edited, {} declined; {} by Hang, {} notes).'.format(
        review['review_id'], c['decided'], c['accepted'], c['edited'], c['declined'], c['by_hang'], c['hang_notes']))


if __name__ == '__main__':
    main(sys.argv[1:])
