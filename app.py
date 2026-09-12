import sys
from pathlib import Path
import streamlit as st
sys.path.append(str(Path(__file__).parent))
from src.core import answer, ingest_text, load_chunks

st.set_page_config(page_title='RuleGuard AI', page_icon='📘', layout='wide')
ROOT=Path(__file__).parent; RULEBOOK=ROOT/'data'/'university_rulebook.md'
if RULEBOOK.exists(): ingest_text(RULEBOOK.read_text(encoding='utf-8'))

st.title('📘 RuleGuard AI')
st.caption('Contradiction-aware, grounded question answering over a university rulebook')
with st.sidebar:
    st.header('Demo questions')
    for example in ['What is the fee deadline?','Can I sit for exams with 68% attendance and medical leave?','Can I miss an exam because of a family wedding?','How can I file a grievance?']:
        if st.button(example,use_container_width=True): st.session_state['question']=example
    st.divider(); st.metric('Indexed passages',len(load_chunks())); st.caption('Local demo mode • No API key required')
question=st.text_input('Ask a question about the rulebook',value=st.session_state.get('question',''),placeholder='Example: What is the fee deadline?')
if st.button('Ask RuleGuard',type='primary') and question.strip():
    result=answer(question.strip()); colors={'ANSWERABLE':'green','NOT_COVERED':'orange','CONTRADICTION':'red'}
    st.markdown(f"### :{colors[result['status']]}[{result['status']}]")
    st.write(result['answer']); st.info(result['reason'])
    st.subheader('Source citations')
    if not result['citations']: st.warning('No source citation available because the rulebook did not support the question.')
    for c in result['citations']:
        with st.expander(f"{c['document']} · {c['section']} · page {c['page']} · {c['chunk_id']}"): st.write(c['text'])
    with st.expander('Retrieved evidence and scores'): st.json(result['evidence'])
