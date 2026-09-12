import json, sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.core import ingest_text, answer
ROOT=Path(__file__).resolve().parents[1]
ingest_text((ROOT/'data'/'university_rulebook.md').read_text(encoding='utf-8'))
sets=[]
for fn in ['answerable_questions.json','unanswerable_questions.json','contradiction_questions.json']:
    sets += json.loads((ROOT/'evaluation'/fn).read_text())
correct=0; citation_ok=0
for item in sets:
    r=answer(item['question'])
    ok=r['status']==item['expected_status']; correct+=ok
    citation_ok += (item['expected_status']=='NOT_COVERED' or bool(r['citations']))
    if not ok: print(f"FAIL {item['id']}: expected={item['expected_status']} actual={r['status']}")
print('=====================================')
print('RuleGuard AI Evaluation')
print('Total questions:',len(sets))
print('Status accuracy: {:.2f}%'.format(100*correct/len(sets)))
print('Citation presence: {:.2f}%'.format(100*citation_ok/len(sets)))
print('=====================================')
