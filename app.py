import streamlit as st
import pandas as pd

st.title("🏠 Where Did I Put My Stuff?")

# Create empty data if none exists
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Item", "Location", "Notes"]
    )

st.header("➕ Add Item")
item = st.text_input("Item name")
location = st.text_input("Location")
notes = st.text_area("Notes")

if st.button("Save"):
    new_row = {
        "Item": item,
        "Location": location,
        "Notes": notes
    }
    st.session_state.data = pd.concat(
        [st.session_state.data, pd.DataFrame([new_row])],
        ignore_index=True
    )
    st.success("Saved!")

st.header("🔍 Search")
search = st.text_input("Search item")

if search:
    results = st.session_state.data[
        st.session_state.data["Item"].str.contains(search, case=False, na=False)
    ]
    st.table(results)
else:
    st.table(st.session_state.data)
