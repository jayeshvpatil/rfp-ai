from crewai import Crew
from textwrap import dedent
from rfp_crew import RFPCrew
import streamlit as st
import asyncio

if __name__ == "__main__":
    st.title("Welcome to RFP Assistant Crew")
    st.write('-------------------------------')
    company = st.text_input("Name of the company requesting for a proposal:")
    competitors = st.text_area("List the top 3 competitors? If no known competitor, mention 'No Competitors':")
    business_problem = st.text_area("Describe the business problem or objective in few sentences:")
    industry = st.text_input("Mention the relevant industry for the client:")

    if st.button('Submit'):
        with st.spinner("Crew is working your RFP Research..Be Right back...."):
            rfp_crew = RFPCrew(company, competitors, business_problem, industry)
            rfp_response =  rfp_crew.run()
            file_name = company + '_rfp_response.txt'
            with open(file_name,'w')as file:
                file.write(str(rfp_response))
                st.info(rfp_response)