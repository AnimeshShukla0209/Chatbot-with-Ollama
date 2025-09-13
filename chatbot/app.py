# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama
# import streamlit as st
# import os
# from dotenv import load_dotenv

# # Load env variables
# load_dotenv()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# # Prompt Template
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful assistant. Please respond clearly and concisely."),
#         ("user", "Question: {question}")
#     ]
# )

# # Streamlit UI
# st.set_page_config(page_title="LangChain + LLaMA2", page_icon="🤖", layout="centered")

# st.markdown(
#     """
#     <style>
#         .main-title {
#             font-size:2.2rem; 
#             font-weight:bold; 
#             color:#4CAF50;
#             text-align:center; 
#             margin-bottom:1rem;
#         }
#         .user-input {
#             padding:10px; 
#             border-radius:10px; 
#             border:1px solid #ddd;
#             width:100%;
#         }
#         .response-box {
#             background-color:#f9f9f9; 
#             padding:20px; 
#             border-radius:10px; 
#             margin-top:20px; 
#             border:1px solid #ddd;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown("<div class='main-title'>🤖 Chatbot with LLaMA2</div>", unsafe_allow_html=True)

# input_text = st.text_input("🔎 Ask me anything:", key="input")

# # LLaMA2 Model
# llm = Ollama(model="llama2")
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser

# if input_text:
#     with st.spinner("Thinking... 🤔"):
#         response = chain.invoke({"question": input_text})
#     st.markdown("<div class='response-box'>", unsafe_allow_html=True)
#     st.markdown(f"**Answer:** {response}")
#     st.markdown("</div>", unsafe_allow_html=True)
