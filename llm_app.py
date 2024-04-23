import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

prompt_template = """
You are an expert at fitness training planner.

Please take the users request and plan a comprehensive week exercise plan for them.

Please include the following details:
- The 7-days plan
- The type of Exercises each day
- The duration of each workout
- The level of effort to be applied
- The nutrient intake everyday
- The rest and recovery time each day

The user's request is:
I want a 7-days exercise plan. {prompt}
"""

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

st.title("🏃 Fitness Training Planner")

prompt = st.text_area("Enter your exercise goals and routine (time, current level, nutrient intake, etc.):")
if st.button("Give me a plan!"):
    reply = generate_content(prompt)
    st.write(reply)