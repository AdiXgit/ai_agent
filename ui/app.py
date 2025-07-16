import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agents.research_agent import get_research_agent
from tools.search_tool import search_google  
from tools.extract_tool import extract_text
from tools.summarise_tool import summarise_article
from utils.relevance_filter import filter_relevant_text
from memory.vector_store import get_vector

st.title("AutoResearch Agent")
query = st.text_input("Enter your research topic")

if st.button("Run Agent") and query:
    urls = search_google(query)
    summaries = []

    for url in urls:
        st.write(f"🔗 Visiting: {url}")
        text = extract_text(url)
        if "Error" in text or len(text) < 300:
            continue

        relevance = filter_relevant_text(text, query)
        st.write(f"Relevance Check: {relevance}")
        if "yes" not in relevance.lower():
            continue

        summary = summarise_article(text)
        st.success(summary)
        summaries.append(summary)

    if summaries:
        st.subheader("Final Synthesis")
        all_summaries = "\n".join(summaries)
        final_summary = summarise_article(all_summaries)
        st.markdown(final_summary)

        # Save to vector DB
        vector_store = get_vector()
        for summary in summaries:
            vector_store.add_texts([summary])
        vector_store.persist()
