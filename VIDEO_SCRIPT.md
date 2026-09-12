# 2–3 Minute Demo Video Script

1. **Problem (15 sec)**
   “University rulebooks contain scattered and sometimes conflicting provisions. A normal chatbot may answer confidently without showing evidence. RuleGuard AI is designed to be checkable.”

2. **Architecture (25 sec)**
   “The rulebook is ingested, split into heading-aware passages, and stored in SQLite with document, section, page, and chunk metadata. A question is retrieved using TF-IDF and bigram similarity. A deterministic decision layer returns one of three states.”

3. **ANSWERABLE demo (25 sec)**
   Ask: `What is the fee deadline?`
   Explain: “The system retrieves the Fee Deadlines section and displays the supporting citation.”

4. **NOT_COVERED demo (25 sec)**
   Ask: `Can I miss an exam because of a family wedding?`
   Explain: “The rulebook discusses medical leave and personal commitments, but does not grant a family-wedding exception. The system refuses to invent a policy.”

5. **CONTRADICTION demo (30 sec)**
   Ask: `Can I sit for exams with 68% attendance and medical leave?`
   Explain: “The general attendance rule says 75%, while the approved medical concession can reduce it to 65%. RuleGuard shows the conflict and points to committee review.”

6. **Evaluation (20 sec)**
   Run: `python evaluation\\evaluate.py`
   Explain that the benchmark contains answerable, unanswerable, and contradiction questions and reports measured results.

7. **Close (10 sec)**
   “The core design is grounded retrieval, explicit uncertainty, contradiction visibility, and traceable citations.”
