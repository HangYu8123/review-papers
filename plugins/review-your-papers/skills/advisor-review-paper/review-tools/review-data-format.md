# review-data.js in practice

The specification is the header comment of review_template/review.html, which takes precedence if this reference disagrees with it. The examples below describe the format for any paper. Bracketed text is a placeholder: replace it with verified facts from the current manuscript. Do not treat example wording, labels, or metadata as evidence.

## Skeleton

```js
// Review of the current manuscript. Use its actual venue and submission information.
window.REVIEW_DATA = {
 "review_id": "[unique-paper-review-id]",
 "title": "[paper title]",
 "generated": "[local ISO 8601 timestamp]",
 "paper": { "id": "[submission id, if supplied]", "venue": "[venue, if supplied]" },
 "items": [],
 "machine": { "title": "", "caption": "", "states": [], "transitions": [] }
};
```

Everything from the first opening brace to the last closing brace must be strict JSON. Escape double quotes inside strings. Keep the items in section order: summary, strength, weakness, improvement, recommendation. Derive review_id from the paper being reviewed and keep it stable when revising that review.

## One item with its evidence

```json
{
 "id": "strength-1",
 "group": "strength",
 "type": "review",
 "op": "insert",
 "revised": "[One specific contribution and the fact that supports it, in one or two sentences.]",
 "evidence": [
  {
   "where": "[section, table, or figure and page]",
   "text": "[The verified result, with the relevant condition, measure, baseline, and values.]",
   "reason": "[Why this evidence supports the strength, including any assumptions or calculation.]",
   "source": "experiments"
  }
 ]
}
```

Set source to the kind of evidence actually used. Add a category only when the section has at least three points and the category helps organize them. Exact comparisons and additional conditions belong in evidence; the review text states the point and its essential support. External evidence also needs its source URL.

## Argument map

Use the following object as the machine value. Replace the contribution and work states with what the paper actually contributes and builds. Include the evaluations that test those contributions, with the actual setting and total workload. The weak edge illustrates partial support; keep it only when the current evidence has that limitation.

```json
{
 "title": "Contributions and supporting evidence",
 "caption": "[The central intuition and how well the evidence supports the contributions.]",
 "states": [
  {
   "id": "idea",
   "role": "intuition",
   "label": "[central idea]",
   "text": "[One sentence explaining the intuition to a reader outside the area.]"
  },
  {
   "id": "contribution-a",
   "role": "contribution",
   "label": "[first contribution]",
   "text": "[What the paper contributes.]",
   "points": ["summary-1", "strength-1"]
  },
  {
   "id": "contribution-b",
   "role": "contribution",
   "label": "[second contribution]",
   "text": "[A distinct contribution.]",
   "points": ["strength-2"]
  },
  {
   "id": "work-a",
   "role": "work",
   "label": "[work supporting A]",
   "where": "[method section or derivation]",
   "text": "[What was built or established, distinguishing new work from borrowed components.]"
  },
  {
   "id": "work-b",
   "role": "work",
   "label": "[work supporting B]",
   "where": "[relevant section]",
   "text": "[The work that implements or establishes the second contribution.]"
  },
  {
   "id": "evaluation-a",
   "role": "experiment",
   "label": "[evaluation of A]",
   "sub": "[setting and total workload]",
   "where": "[results location]",
   "text": "[The comparison, main result, and its scope.]",
   "points": ["strength-1"]
  },
  {
   "id": "evaluation-b",
   "role": "experiment",
   "label": "[evaluation of B]",
   "sub": "[setting and total workload]",
   "where": "[results location]",
   "text": "[What this evaluation supports and what it leaves unresolved.]",
   "points": ["weakness-1"]
  },
  {
   "id": "context",
   "role": "context",
   "label": "[relevant assumption]",
   "text": "[An assumption or dependency that explains the evidence gap.]",
   "points": ["weakness-1"]
  }
 ],
 "transitions": [
  { "from": "idea", "to": "contribution-a" },
  { "from": "idea", "to": "contribution-b" },
  { "from": "contribution-a", "to": "work-a" },
  { "from": "contribution-b", "to": "work-b" },
  { "from": "work-a", "to": "evaluation-a", "label": "[supported result]" },
  { "from": "work-b", "to": "evaluation-b", "label": "[partial support]", "weak": true },
  { "from": "evaluation-b", "to": "context", "label": "depends on" }
 ]
}
```

The map follows the argument: intuition, contributions, the work behind them, and supporting evaluations. Use the paper's own contributions and evidence rather than filling every example slot. Set novel to true only on work that is new. Explain any computed workload totals and mark inferences explicitly.

## Practical notes

- Every id is unique within its list. Each points entry names an existing review item.
- List states by role. Transitions to an earlier state are drawn as loops.
- Keep state labels to about 28 characters and edge labels to a few words.
- A weak edge identifies a specific gap, such as a test that does not isolate the contribution. Link it to the corresponding weakness.
- Include context states only when they explain the paper or an important concern.
- Revising an item's text or evidence can invalidate its saved decision, so change only the items that need revision.
