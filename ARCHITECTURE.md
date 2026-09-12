# RuleGuard AI — Architecture

```text
Markdown rulebook + PDF policy
            |
            v
Document ingestion / extraction
            |
            v
Heading-aware chunking + metadata
            |
            v
SQLite passage store
            |
            v
Question normalization
            |
            v
TF-IDF + bigram retrieval
(section-aware lexical boosts)
            |
            v
Evidence / conflict decision layer
       /          |          \
      v           v           v
ANSWERABLE  NOT_COVERED  CONTRADICTION
      |           |           |
      v           v           v
Answer +      Refusal +    Both conflicting
exact cited    no invented   passages + safe
passages       information   explanation
```

## Components

- **UI:** Streamlit web interface.
- **Ingestion:** Python reads Markdown and PDF text; each passage keeps document, section, page, and chunk ID.
- **Storage:** SQLite stores the searchable passages locally.
- **Retrieval:** scikit-learn TF-IDF with unigrams/bigrams plus section-aware lexical boosts.
- **Decision layer:** deterministic rules identify planted conflict patterns and reject weak retrievals.
- **Evaluation:** JSON benchmark and Python script report status accuracy and citation presence.
- **Safety principle:** no evidence means no answer; conflict means no silent selection.
