# Streamlit app for phonological plausibility demo

import streamlit as st
from phonological_plausibility_demo import analyse_string

st.set_page_config(page_title="Phonological Plausibility Demo")

st.title("Phonological Plausibility Demo")
st.caption("Given a string of symbols, what structural hypotheses are reasonable?")

word = st.text_input("Please enter a string")

if word:
    results = analyse_string(word)

    st.subheader("Generated skeletons")
    st.write(results["skeletons"])

    for entry in results["evaluations"]:
        st.subheader(entry["family"])
        st.write(f"Strain index: {entry['strain']}")
        st.write(f"Plausibility score (1–5): {entry['plausibility']}")
        if entry["diagnostics"]:
            st.write("Diagnostics:")
            for d in entry["diagnostics"]:
                st.write(f"- {d}")
