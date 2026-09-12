# RuleGuard AI

## The Rulebook That Argues With Itself

RuleGuard AI is a contradiction-aware, grounded question-answering
system for university regulations.

It helps students ask questions in plain English and receive answers
based on the uploaded rulebook rather than unsupported guesses. Every
result includes source information so that the evidence can be checked.

The system supports three possible outcomes:

-   **ANSWERABLE** --- the rulebook contains enough relevant information
    to answer.
-   **NOT_COVERED** --- the rulebook does not provide enough
    information; the system refuses to invent an answer.
-   **CONTRADICTION** --- two or more relevant provisions may conflict,
    so the system shows the evidence instead of silently choosing one
    rule.

------------------------------------------------------------------------

## Features

-   Loads a university rulebook from Markdown and PDF files.
-   Splits documents into smaller heading-aware passages.
-   Stores passages and metadata in SQLite.
-   Uses TF-IDF and cosine similarity for local document retrieval.
-   Uses section-aware keyword matching for better retrieval.
-   Detects important contradiction scenarios.
-   Displays source citations containing:
    -   Document name
    -   Section
    -   Page number, when available
    -   Passage/chunk identifier
-   Provides a Streamlit web interface.
-   Includes an evaluation script with answerable, unanswerable, and
    contradiction questions.
-   Runs locally without requiring an external LLM API key.

------------------------------------------------------------------------

## Project Architecture

``` text
                 Rulebook Documents
                 Markdown + PDF
                        |
                        v
                Document Ingestion
                        |
                        v
               Text Extraction/Cleaning
                        |
                        v
             Heading-Aware Chunking
                        |
                        v
                 SQLite Database
       text + section + page + document + chunk ID
                        |
                        v
                  User Question
                        |
                        v
                TF-IDF Retrieval
          cosine similarity + keyword boost
                        |
                        v
                 Decision Layer
                        |
             +----------+----------+
             |          |          |
             v          v          v
        ANSWERABLE  NOT_COVERED  CONTRADICTION
             |          |          |
             v          v          v
       Grounded     Refusal to    Conflicting
       response +   hallucinate   provisions +
       citations                  citations
```

------------------------------------------------------------------------

## Technology Stack

  -----------------------------------------------------------------------
  Layer                   Technology              Purpose
  ----------------------- ----------------------- -----------------------
  Programming language    Python 3.11+            Application logic

  Frontend                Streamlit               Interactive web
                                                  application

  Document processing     PyMuPDF                 PDF text extraction

  Text processing         Python and regular      Cleaning and passage
                          expressions             splitting

  Information retrieval   scikit-learn TF-IDF     Retrieve relevant
                                                  passages

  Similarity              Cosine similarity       Rank evidence

  Database                SQLite                  Store passages and
                                                  metadata

  Evaluation              Python and JSON         Measure system
                                                  performance

  Documentation           Markdown                Project documentation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Folder Structure

``` text
RuleGuard-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── ARCHITECTURE.md
├── VIDEO_SCRIPT.md
├── .env.example
├── .gitignore
│
├── src/
│   └── core.py
│
├── data/
│   ├── university_rulebook.md
│   ├── medical_exemption_policy.pdf
│   ├── contradictions.md
│   └── eval/
│
├── evaluation/
│   └── evaluate.py
│
└── scripts/
    └── ingest_documents.py
```

------------------------------------------------------------------------

## Requirements

-   Python 3.11 or newer
-   pip
-   Windows, macOS, or Linux

------------------------------------------------------------------------

## Installation

Open a terminal inside the project folder.

### 1. Install dependencies

``` bash
python -m pip install -r requirements.txt
```

If the command `python` does not work on Windows, try:

``` bash
py -m pip install -r requirements.txt
```

### 2. Run the application

``` bash
python -m streamlit run app.py
```

If successful, Streamlit will show a local URL similar to:

``` text
http://localhost:8501
```

Open that URL in your browser.

------------------------------------------------------------------------

## Running the Evaluation

From the project root folder, run:

### Windows

``` bash
python evaluation\evaluate.py
```

### macOS/Linux

``` bash
python evaluation/evaluate.py
```

The evaluation script reports:

-   Total number of questions
-   Status accuracy
-   Citation presence

Example output format:

``` text
=====================================
RuleGuard AI Evaluation
Total questions: 43
Status accuracy: XX.XX%
Citation presence: XX.XX%
=====================================
```

The displayed values should always be taken from the actual evaluation
run. Do not claim a perfect score without running the script.

------------------------------------------------------------------------

## Demo Questions

### 1. ANSWERABLE

``` text
What is the fee deadline?
```

Expected behavior:

-   Returns `ANSWERABLE`
-   Retrieves the Fee Deadlines section
-   Displays the relevant source citation

### 2. CONTRADICTION

``` text
Can I sit for exams with 68% attendance and medical leave?
```

Expected behavior:

-   Returns `CONTRADICTION`
-   Shows the general attendance requirement
-   Shows the medical exemption provision
-   Displays both relevant citations

### 3. NOT_COVERED

``` text
Can I miss an exam because of a family wedding?
```

Expected behavior:

-   Returns `NOT_COVERED`
-   Explains that the rulebook does not authorize this exception
-   Avoids inventing an answer

### 4. ANSWERABLE

``` text
How can I file a grievance?
```

Expected behavior:

-   Returns `ANSWERABLE`
-   Retrieves the Student Grievances section
-   Displays the grievance procedure citation

------------------------------------------------------------------------

## Data and Evaluation Design

The corpus contains university-style regulations covering topics such
as:

-   Attendance requirements
-   Medical exemptions
-   Examination rules
-   Fee deadlines
-   Student grievances
-   Hostel rules
-   Library rules
-   Scholarships
-   Student societies
-   Disciplinary procedures

The evaluation set contains:

1.  Questions directly answerable from the corpus.
2.  Plausible near-miss questions that the corpus does not cover.
3.  Questions designed to test planted contradictions.

The file `data/contradictions.md` records the planted contradictions and
the relevant provisions.

------------------------------------------------------------------------

## What Is Mocked or Local

This project intentionally uses a local retrieval pipeline.

-   The university rulebook is a synthetic/demo corpus.
-   The rulebook content is not an official university policy.
-   The system does not call an external LLM API in local demo mode.
-   The response generation is deterministic and based on retrieved
    passages.
-   Contradiction handling uses explicit rules and evidence matching.
-   The project is intended as a demonstration of grounded retrieval and
    transparent decision-making, not as official academic advice.

------------------------------------------------------------------------

## Limitations

-   TF-IDF is lexical retrieval, so it may miss some deeply semantic
    paraphrases.
-   Contradiction detection is rule-assisted and depends on the
    provisions represented in the corpus.
-   The generated rulebook is a demonstration dataset.
-   The system should not be used as an official source for real
    university decisions.
-   A real production system would need stronger semantic retrieval,
    document versioning, human review, and more comprehensive
    contradiction analysis.

------------------------------------------------------------------------

## How to Use the Application

1.  Start the Streamlit application.
2.  Enter a question in the input box.
3.  Click **Ask RuleGuard**.
4.  Read the status:
    -   `ANSWERABLE`
    -   `NOT_COVERED`
    -   `CONTRADICTION`
5.  Review the retrieved evidence.
6.  Open the source citation to verify the document section and passage.

------------------------------------------------------------------------

## Suggested Git Commit History

The project can be developed with commits such as:

``` bash
git add .
git commit -m "Add initial rulebook corpus and project structure"

git add .
git commit -m "Add document ingestion and SQLite indexing"

git add .
git commit -m "Add TF-IDF retrieval and source citations"

git add .
git commit -m "Add contradiction and not-covered handling"

git add .
git commit -m "Add evaluation dataset and scoring script"

git push
```

------------------------------------------------------------------------

## Video Demonstration

The recommended demonstration order is:

1.  Introduce the problem and project.
2.  Explain the architecture briefly.
3.  Show an `ANSWERABLE` question.
4.  Show a `CONTRADICTION` question.
5.  Show a `NOT_COVERED` question.
6.  Run the evaluation script.
7.  Show the repository structure.

------------------------------------------------------------------------

## Author

Built as a submission for the IT Geeks AI Developer Vibe Coding Round.

**Selected problem:**\
**1 · The Rulebook That Argues With Itself**
