from pathlib import Path
from src.core import ingest_text
ROOT=Path(__file__).resolve().parents[1]
md=ROOT/'data'/'university_rulebook.md'
print('Indexed passages:', ingest_text(md.read_text(encoding='utf-8')))
print('PDF included for mixed-format corpus:', (ROOT/'data'/'medical_exemption_policy.pdf').exists())
