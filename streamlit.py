import streamlit as st
from scraper import scraper
from summarizer import summarizer
from chatbot_gemini import chatbot as Bot

def main():
    st.title('Web summarizer Chatbot')

    option = st.selectbox('Select an option:', ['Home', 'Get Summary', 'Get Bot Response'])

    if option == 'Home':
        st.write('Welcome to the home page!')

    elif option == 'Get Summary':
        url = st.text_input('Enter URL:')
        if st.button('Get Summary'):
            text = scraper(url)
            summary = summarizer(text)
            st.write('Summary:', summary)

    elif option == 'Get Bot Response':
        url = st.text_input('Enter URL:')
        message = st.text_input('Enter message:')
        if st.button('Get Bot Response'):
            text = scraper(url)
            bot = Bot(text)
            result = bot.qa_chain({"query": message})
            response = result["result"]
            st.write('Bot Response:', response)

if __name__ == '__main__':
    main()
