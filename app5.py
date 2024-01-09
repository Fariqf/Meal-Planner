import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain


load_dotenv()
API_KEY=os.environ['OPENAI_API_KEY']

llm=OpenAI(openai_api_key=API_KEY , temperature=.6)

prompt_template = PromptTemplate(
    template="Give me an example of a meal could be made using the following ingredients : {ingredients} and also list the step by step process to make the meal",
    input_variables=['ingredients']
)

meal_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    verbose=True
)

st.markdown("<h1 style='text-align: center; color: grey;'>MEAL PLANNER</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("parotta.jpg")

with col3:
    st.write(' ')

user_prompt=st.text_input("Enter a comma-separated list of incredients...")
if st.button("Generate") and user_prompt:
    with st.spinner('Generating...'):
        output=meal_chain.run(ingredients=user_prompt)
        st.write(output)

st.caption("Made with ❤️ by @fariq")