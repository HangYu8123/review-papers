# Example review

Seven items on a toy document, one of each kind, to show how the page, the batches and the apply step behave. Nothing here touches the dissertation.

7 items, built 2026-11-03 00:17. Open `review.html` in this folder to accept or reject each one. Nothing in the dissertation changes until the apply step is run with `--write`.

| Change type | Tag written around accepted text | Items |
| --- | --- | ---: |
| Pronoun | `\hang{pronoun start}` ... `\hang{pronoun end}` | 3 |
| Deletion | `\hang{delete start}` ... `\hang{delete end}` | 2 |
| New text | `\hang{create start}` ... `\hang{create end}` | 1 |
| Update | `\hang{update start}` ... `\hang{update end}` | 1 |

## Requests

**R1** (2026-10-11, by Hang)

> replace the first-person pronouns in the study chapter

**R2** (2026-10-11, by Hang)

> cut anything the reader has already been told

**R3** (2026-10-11, by a committee member, sample/notes.txt)

> Why does the method rescale ratings instead of dividing by the maximum?

A second agent (Example second agent, 2026-11-02) looked at 7 of these 7 items and disagreed on 5. Those entries show two options, from `disagreements.txt`.

## Chapter 1 · A Toy Study

### S-001

- **Location:** Chapter 1 › Introduction, `chapters/study.tex` lines 6-7
- **Change type:** Pronoun
- **Request:** R1
- **Version:** `24917304d123`
- **Two options:** a second agent (Example second agent) disagrees: another wording.
- **Why option A:** First person replaced by a passive; the citation stays where it was.
- **Why option B:** The passive keeps "was conducted", which tells the reader nothing. Making the participants the subject removes the pronoun and the empty verb together.

**Original**

```latex
We conducted a study with 24 participants to see how people rate a robot that sorts blocks \cite{toy2024}.
```

**Option A**

```latex
A study with 24 participants was conducted to see how people rate a robot that sorts blocks \cite{toy2024}.
```

**Option B**

```latex
Twenty-four participants took part in a study of how people rate a robot that sorts blocks \cite{toy2024}.
```

### S-002

- **Location:** Chapter 1 › Introduction, `chapters/study.tex` line 7
- **Change type:** Pronoun
- **Request:** R1
- **Version:** `22cefb1f9904`
- **Two options:** a second agent (Example second agent) disagrees: remove the passage.
- **Why option B:** The next section reports the drift itself, so an intuition stated here adds nothing once the pronoun is gone.

**Original**

```latex
Our intuition is that ratings drift as a session goes on.
```

**Option A**

```latex
The intuition is that ratings drift as a session goes on.
```

**Option B** *(remove the passage)*

### S-003

- **Location:** Chapter 1 › Introduction, `chapters/study.tex` lines 10-11
- **Change type:** Deletion
- **Request:** R2
- **Version:** `d2bf0f67c225`
- **Two options:** a second agent (Example second agent) disagrees: leave the passage as it is.
- **Why option A:** The order of the clips is already given in the Methodology. With no revised text, accepting this removes the sentence.
- **Why option B:** The reason given for this cut does not hold. This chapter is the only place that states the order of the clips, so removing the sentence loses the fact.

**Original**

```latex
The clips were shown in a random order.
```

**Option A** *(removed)*

**Option B** *(leave the passage as it is)*

### S-004

- **Location:** Chapter 1 › Results › Rating drift, `chapters/study.tex` lines 17-18
- **Change type:** Pronoun
- **Request:** R1
- **Version:** `2fde6c670cf2`
- **Why:** Results as the subject, following the "results suggested that" pattern.

**Original**

```latex
We found that ratings fell by $0.4 \pm 0.1$ points between the first and the last block, as shown in \autoref{fig:drift}.
```

**Revised**

```latex
Ratings fell by $0.4 \pm 0.1$ points between the first and the last block, as shown in \autoref{fig:drift}.
```

### S-005

- **Location:** Chapter 1 › Results › Rating drift, `chapters/study.tex` line 20
- **Change type:** Deletion
- **Request:** R2
- **Version:** `dc0d0e7318da`
- **Why:** Repeats the previous paragraph. Kept in the file with delete tags, so it can be seen in the PDF before it goes.

**Original**

```latex
The effect was the same for both groups.
```

**Revised** *(kept, marked for deletion)*

### S-006 · A closing sentence for the Discussion

- **Location:** Chapter 1 › Discussion, `chapters/study.tex` line 24
- **Change type:** New text
- **Request:** none, nobody asked for this edit
- **Version:** `99176d4441c6`
- **Two options:** a second agent (Example second agent) disagrees: another wording.
- **Why option A:** The section ends without saying what the drift means for the method chapter.
- **Why option B:** The proposed sentence runs two ideas together with a colon. One short sentence says the same and points to the method chapter sooner.

**Inserted after**

```latex
It is, however, consistent across participants.
```

**Option A**

```latex
This consistency is what the method in \autoref{ch:method} relies on: a drift that
every participant shares can be corrected with a single adjustment.
```

**Option B**

```latex
Because every participant shares this drift, the method in \autoref{ch:method} can correct it with a single adjustment.
```

## Chapter 2 · A Toy Method

### M-001 · Rewritten description of the rescaling

- **Location:** Chapter 2 › Approach, `chapters/method.tex` lines 6-10
- **Change type:** Update
- **Request:** R3
- **Status:** already in the text, tagged; rejecting it restores the original
- **Version:** `59bb2a28c687`
- **Two options:** a second agent (Example second agent) disagrees: another wording.
- **Why option A:** This one was put into the text directly, between update tags. Rejecting it puts the original back.
- **Why option B:** The second sentence is easier to follow when the two effects come in the order the reader needs them, and "rescales" already says what happens to the rating.

**Original**

```latex
The method divides each rating by the largest rating the participant gave.
```

**Option A**

```latex
The method rescales each rating by the participant's own range before it is used
as a reward. This keeps the order of a participant's ratings and removes the
difference in how widely participants spread them.
```

**Option B**

```latex
The method rescales each rating by the participant's own range before it is used
as a reward. This removes the difference in how widely participants spread their
ratings and keeps the order of each participant's ratings.
```
