// Written by build_review.py. Do not edit: change items.txt and build again.
window.REVIEW_DATA = {
 "schema": "review-data/1",
 "review_id": "example",
 "title": "Example review",
 "description": "Seven items on a toy document, one of each kind, to show how the page, the batches and the apply step behave. Nothing here touches the dissertation.",
 "generated": "2026-11-03T00:17:14-05:00",
 "root": "sample",
 "folder": "C:\\Users\\Hang Yu\\Desktop\\Dissertation\\waiting_for_review\\_template\\example",
 "apply_command": "python waiting_for_review/_template/apply_decisions.py waiting_for_review/_template/example",
 "types": {
  "pronoun": {
   "label": "Pronoun",
   "marker": "pronoun",
   "tagged": true
  },
  "delete": {
   "label": "Deletion",
   "marker": "delete",
   "tagged": true
  },
  "create": {
   "label": "New text",
   "marker": "create",
   "tagged": true
  },
  "update": {
   "label": "Update",
   "marker": "update",
   "tagged": true
  }
 },
 "groups": [
  {
   "key": "file:chapters/study.tex",
   "label": "Chapter 1 \u00b7 A Toy Study"
  },
  {
   "key": "file:chapters/method.tex",
   "label": "Chapter 2 \u00b7 A Toy Method"
  }
 ],
 "macros": {
  "\\toolname{}": "the sorting robot"
 },
 "labels": {
  "ch:study": "Chapter 1",
  "ch:method": "Chapter 2"
 },
 "items": [
  {
   "id": "S-001",
   "type": "pronoun",
   "original": "We conducted a study with 24 participants to see how people rate a robot that sorts blocks \\cite{toy2024}.",
   "revised": "A study with 24 participants was conducted to see how people rate a robot that sorts blocks \\cite{toy2024}.",
   "anchor": "",
   "op": "replace",
   "file": "chapters/study.tex",
   "wrap": [
    "\\hang{pronoun start} ",
    " \\hang{pronoun end}"
   ],
   "title": "",
   "note": "First person replaced by a passive; the citation stays where it was.",
   "tags": [],
   "line": 6,
   "line_end": 7,
   "state": "proposed",
   "context_before": "\\chapter{A Toy Study: Feedback in a Sorting Task}\n\\label{ch:study}\n\n\\section{Introduction}",
   "context_after": " Our intuition is that ratings drift as a session goes on.\n% We conducted a study with 24 participants (an older, commented-out draft of the line above).\n\nIt is worth noting that every participant saw the same twelve clips. The clips were\nshown in a random order.\n\n\\section{Results}\n\n\\subsection{Rating drift}",
   "where": "Chapter 1 \u203a Introduction",
   "group": "file:chapters/study.tex",
   "hash": "24917304d123",
   "second": {
    "action": "reword",
    "revised": "Twenty-four participants took part in a study of how people rate a robot that sorts blocks \\cite{toy2024}.",
    "note": "The passive keeps \"was conducted\", which tells the reader nothing. Making the participants the subject removes the pronoun and the empty verb together.",
    "by": "Example second agent",
    "against": "24917304d123",
    "stale": false,
    "hash": "1b679f258ae3"
   }
  },
  {
   "id": "S-002",
   "type": "pronoun",
   "original": "Our intuition is that ratings drift as a session goes on.",
   "revised": "The intuition is that ratings drift as a session goes on.",
   "anchor": "",
   "op": "replace",
   "file": "chapters/study.tex",
   "wrap": [
    "\\hang{pronoun start} ",
    " \\hang{pronoun end}"
   ],
   "title": "",
   "note": "",
   "tags": [],
   "line": 7,
   "line_end": 7,
   "state": "proposed",
   "context_before": "\\chapter{A Toy Study: Feedback in a Sorting Task}\n\\label{ch:study}\n\n\\section{Introduction}\n\nWe conducted a study with 24 participants to see how people rate a robot\nthat sorts blocks \\cite{toy2024}. ",
   "context_after": "% We conducted a study with 24 participants (an older, commented-out draft of the line above).\n\nIt is worth noting that every participant saw the same twelve clips. The clips were\nshown in a random order.\n\n\\section{Results}\n\n\\subsection{Rating drift}",
   "where": "Chapter 1 \u203a Introduction",
   "group": "file:chapters/study.tex",
   "hash": "22cefb1f9904",
   "second": {
    "action": "remove",
    "revised": "",
    "note": "The next section reports the drift itself, so an intuition stated here adds nothing once the pronoun is gone.",
    "by": "Example second agent",
    "against": "22cefb1f9904",
    "stale": false,
    "hash": "9555833874ac"
   }
  },
  {
   "id": "S-003",
   "type": "delete",
   "original": "The clips were shown in a random order.",
   "revised": "",
   "anchor": "",
   "op": "delete",
   "file": "chapters/study.tex",
   "delete_style": "remove",
   "wrap": [
    "\\hang{delete start} ",
    " \\hang{delete end}"
   ],
   "title": "",
   "note": "The order of the clips is already given in the Methodology. With no revised text, accepting this removes the sentence.",
   "tags": [],
   "line": 10,
   "line_end": 11,
   "state": "proposed",
   "context_before": "that sorts blocks \\cite{toy2024}. Our intuition is that ratings drift as a session goes on.\n% We conducted a study with 24 participants (an older, commented-out draft of the line above).\n\nIt is worth noting that every participant saw the same twelve clips. ",
   "context_after": "\\section{Results}\n\n\\subsection{Rating drift}\n\nWe found that ratings fell by $0.4 \\pm 0.1$ points between the first and the last\nblock, as shown in \\autoref{fig:drift}.\n\nThe effect was the same for both groups.\n\n\\section{Discussion}\n\nThe drift is small. It is, however, consistent across participants.",
   "where": "Chapter 1 \u203a Introduction",
   "group": "file:chapters/study.tex",
   "hash": "d2bf0f67c225",
   "second": {
    "action": "keep",
    "revised": "",
    "note": "The reason given for this cut does not hold. This chapter is the only place that states the order of the clips, so removing the sentence loses the fact.",
    "by": "Example second agent",
    "against": "d2bf0f67c225",
    "stale": false,
    "hash": "c33471b92899"
   }
  },
  {
   "id": "S-004",
   "type": "pronoun",
   "original": "We found that ratings fell by $0.4 \\pm 0.1$ points between the first and the last block, as shown in \\autoref{fig:drift}.",
   "revised": "Ratings fell by $0.4 \\pm 0.1$ points between the first and the last block, as shown in \\autoref{fig:drift}.",
   "anchor": "",
   "op": "replace",
   "file": "chapters/study.tex",
   "wrap": [
    "\\hang{pronoun start} ",
    " \\hang{pronoun end}"
   ],
   "title": "",
   "note": "Results as the subject, following the \"results suggested that\" pattern.",
   "tags": [],
   "line": 17,
   "line_end": 18,
   "state": "proposed",
   "context_before": "% We conducted a study with 24 participants (an older, commented-out draft of the line above).\n\nIt is worth noting that every participant saw the same twelve clips. The clips were\nshown in a random order.\n\n\\section{Results}\n\n\\subsection{Rating drift}",
   "context_after": "The effect was the same for both groups.\n\n\\section{Discussion}\n\nThe drift is small. It is, however, consistent across participants.",
   "where": "Chapter 1 \u203a Results \u203a Rating drift",
   "group": "file:chapters/study.tex",
   "hash": "2fde6c670cf2"
  },
  {
   "id": "S-005",
   "type": "delete",
   "original": "The effect was the same for both groups.",
   "revised": "",
   "anchor": "",
   "op": "delete",
   "file": "chapters/study.tex",
   "delete_style": "mark",
   "wrap": [
    "\\hang{delete start} ",
    " \\hang{delete end}"
   ],
   "title": "",
   "note": "Repeats the previous paragraph. Kept in the file with delete tags, so it can be seen in the PDF before it goes.",
   "tags": [],
   "line": 20,
   "line_end": 20,
   "state": "proposed",
   "context_before": "It is worth noting that every participant saw the same twelve clips. The clips were\nshown in a random order.\n\n\\section{Results}\n\n\\subsection{Rating drift}\n\nWe found that ratings fell by $0.4 \\pm 0.1$ points between the first and the last\nblock, as shown in \\autoref{fig:drift}.",
   "context_after": "\\section{Discussion}\n\nThe drift is small. It is, however, consistent across participants.",
   "where": "Chapter 1 \u203a Results \u203a Rating drift",
   "group": "file:chapters/study.tex",
   "hash": "dc0d0e7318da"
  },
  {
   "id": "S-006",
   "type": "create",
   "original": "",
   "revised": "This consistency is what the method in \\autoref{ch:method} relies on: a drift that\nevery participant shares can be corrected with a single adjustment.",
   "anchor": "It is, however, consistent across participants.",
   "op": "insert",
   "file": "chapters/study.tex",
   "position": "after",
   "sep": "\n\n",
   "wrap": [
    "\\hang{create start}\n",
    "\n\\hang{create end}"
   ],
   "title": "A closing sentence for the Discussion",
   "note": "The section ends without saying what the drift means for the method chapter.",
   "tags": [],
   "line": 24,
   "line_end": 24,
   "state": "proposed",
   "context_before": "shown in a random order.\n\n\\section{Results}\n\n\\subsection{Rating drift}\n\nWe found that ratings fell by $0.4 \\pm 0.1$ points between the first and the last\nblock, as shown in \\autoref{fig:drift}.\n\nThe effect was the same for both groups.\n\n\\section{Discussion}\n\nThe drift is small. ",
   "context_after": "",
   "where": "Chapter 1 \u203a Discussion",
   "group": "file:chapters/study.tex",
   "hash": "99176d4441c6",
   "second": {
    "action": "reword",
    "revised": "Because every participant shares this drift, the method in \\autoref{ch:method} can correct it with a single adjustment.",
    "note": "The proposed sentence runs two ideas together with a colon. One short sentence says the same and points to the method chapter sooner.",
    "by": "Example second agent",
    "against": "99176d4441c6",
    "stale": false,
    "hash": "41b445654bc2"
   }
  },
  {
   "id": "M-001",
   "type": "update",
   "original": "The method divides each rating by the largest rating the participant gave.",
   "revised": "The method rescales each rating by the participant's own range before it is used\nas a reward. This keeps the order of a participant's ratings and removes the\ndifference in how widely participants spread them.",
   "anchor": "",
   "op": "replace",
   "file": "chapters/method.tex",
   "wrap": [
    "\\hang{update start}\n",
    "\n\\hang{update end}"
   ],
   "title": "Rewritten description of the rescaling",
   "note": "This one was put into the text directly, between update tags. Rejecting it puts the original back.",
   "tags": [],
   "line": 6,
   "line_end": 10,
   "state": "in_text",
   "context_before": "\\chapter{A Toy Method}\n\\label{ch:method}\n\n\\section{Approach}",
   "context_after": "\\section{Limitations}\n\nThe method was tested on one task only.",
   "where": "Chapter 2 \u203a Approach",
   "group": "file:chapters/method.tex",
   "hash": "59bb2a28c687",
   "second": {
    "action": "reword",
    "revised": "The method rescales each rating by the participant's own range before it is used\nas a reward. This removes the difference in how widely participants spread their\nratings and keeps the order of each participant's ratings.",
    "note": "The second sentence is easier to follow when the two effects come in the order the reader needs them, and \"rescales\" already says what happens to the rating.",
    "by": "Example second agent",
    "against": "59bb2a28c687",
    "stale": false,
    "hash": "fde90b8eeeb6"
   }
  }
 ],
 "second_look": {
  "by": "Example second agent",
  "date": "2026-11-02",
  "looked_at": 7,
  "disagrees": 5
 }
};
