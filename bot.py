import streamlit as st

st.set_page_config(page_title="Simple Chat Bot")

st.title("🤖 Simple Chat Bot")

question = st.text_input("Type your message")

if st.button("Send"):

    # Save question to questions.txt
    with open("questions.txt", "a", encoding="utf-8") as f:
        f.write(question + "\n")

    msg = question.strip().lower()

    if msg in ["hello", "hlo", "hi"]:
        st.success("🤖 Hi, kive ho?")

    elif msg == "how are you":
        st.success("🤖 Main theek haan. Tusi dasso?")

    elif msg == "what is your name":
        st.success("🤖 Mera naam Simple Chat Bot hai.")

    else:
        st.warning("🤖 Sorry! Main is question da answer nahi jaanda.")
