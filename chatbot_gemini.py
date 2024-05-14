import os
import warnings
from scraper import scraper
from langchain.chains import RetrievalQA

warnings.filterwarnings("ignore")
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate





API_KEY = 'AIzaSyAhJFxbj1d0iaj_d4H4i1USleWhpqwZpoM'
model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=API_KEY,
                               temperature=0.1,convert_system_message_to_human=True)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=API_KEY)

template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know
            {context}
            Question: {question}
            Helpful Answer:"""


class chatbot:
    
    def __init__(self,data):
        self.data = "".join(data)
        self.model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=API_KEY,
                               temperature=0.2,convert_system_message_to_human=True)
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=API_KEY)
        self.vector_index = self.prep_pdf()
        self.QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
        self.qa_chain = RetrievalQA.from_chain_type(
            self.model,
            retriever=self.vector_index,
            return_source_documents=True,
            chain_type_kwargs={"prompt":self.QA_CHAIN_PROMPT}
        )

    def prep_pdf(self):

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        texts = text_splitter.split_text(self.data)
        vector_index = Chroma.from_texts(texts, self.embeddings).as_retriever()
        
        return vector_index
    
# while True:
#   try:
#       question = input("You: ")
#       result = qa_chain({"query": question})
#       print("Chatbot: ",result["result"])
#   except KeyboardInterrupt:
#             break
        

# bot = chatbot(scraper(input("url")))

# while True:
#     try:
#         question = input("You: ")
#         result = bot.qa_chain({"query": question})
#         print("Chatbot: ",result["result"])

#     except KeyboardInterrupt:
#         break

#     except Exception as e:
#         print("Error: ", e)