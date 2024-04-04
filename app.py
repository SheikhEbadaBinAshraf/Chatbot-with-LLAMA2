# These Three things are very Important for Paid API Or Open Source Model
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# 3rd Party Integration
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Initialize all Environment Variables
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# langSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt_template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a very helpful assistant. Please response to the user queries"),
        ("user", "Question{question}")
    ]
)

# Streamlit Framework
st.title("Your BOT With LLAMA2")
input_text = st.text_input("Search the topic you want")

# Ollama LLAMA2 LLM
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Applying Streamlit's built-in style options
st.write(
    """
    <style>
    input.st-ae.st-bc.st-bd.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-ah.st-bm.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-ax.st-ay.st-az.st-bu.st-b1.st-b2.st-bb.st-bv.st-bw.st-bx {
      background-color: black;
      color: #fff;
    }
    span.st-emotion-cache-10trblm.e1nzilvr1{
    position: relative;
    }
    span.st-emotion-cache-10trblm.e1nzilvr1::before {
    content: url("./1.png");
    position: absolute;
    left: 10px;
    }
    .stTextInput{
        background-color: #f0f0f0 !important;
        border-color: #a3a3a3 !important;
        border-radius: 10px !important;
        padding: 10px !important;
        font-size: 16px !important;
    }
    .stTextInput>div>label {
        color: #333333 !important;
        font-size: 18px !important;
    }
    .stButton>button {
        background-color: #4CAF50 !important;
        color: white !important;
        padding: 10px 20px !important;
        text-align: center !important;
        font-size: 16px !important;
        border-radius: 10px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        background-color: #45a049 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if input_text:
    st.write(chain.invoke({"question": input_text}))
