import streamlit as st
import openai
import json

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"


def get_job_posting_information(job_posting):
    try:
        prompt = f"""
                You are an helpful assistant that extracts useful information from a job posting \
                analyze the job posting provided delimited with triple back ticks \
                and extract the following information in a json response \
                1- Job Title
                2- Company Name
                3- Job Location Type (Hybrid, Remote, Physical)
                4- Job Description (in 4 to 5 words)
                5- Academic Requirement
                6- Experience Requirement
                7- Skills Requirement
                8- Salary Package Detail
                9- Location
                10- Job Type (Full Time, Part Time, Internship, Contract Based, Freelancing)
                11- Application Deadline
                12- Company Email
                13- Company Phone Number
                14- Keywords
                15- Company Website
                16- How to Apply

                JSON object example \
                {{
                  "title": "",
                  "company": "",
                  "loc_type": "",
                  "location": "",
                  "job_type": "",
                  "description": "",
                  "academic": "",
                  "experience": "",
                  "skills": "",
                  "salary": "",
                  "deadline": "",
                  "email": "",
                  "phone": "",
                  "keywords": "",
                  "website": "",
                  "how_to_apply": "",
                }}

                Job Posting:
                ```
                {job_posting}
                ```
        """

        messages = [{"role": "system", "content": "You are an expert and helpful assistant that extracts "
                                                  "useful information from a job posting"},
                    {"role": "user", "content": prompt}]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
        )

        # Extracting relevant information from the GPT-3 response
        responseJSON = json.loads(response.choices[0].text)

        return responseJSON
    except Exception as e:
        st.error(f"Error extracting the information: {str(e)}")
        return None


def main():
    st.title("Job Posting Information Extractor")

    # User input for review
    job_posting = st.text_area("Enter your job posting here:")

    if st.button("Extract Information"):
        if job_posting:
            extracted_info = get_job_posting_information(job_posting)
            if extracted_info:
                st.subheader("Extracted Information:")
                st.write(f"Item: {extracted_info['title']}")
                st.write(f"Item: {extracted_info['company']}")
                st.write(f"Item: {extracted_info['loc_type']}")
                st.write(f"Item: {extracted_info['location']}")
                st.write(f"Item: {extracted_info['job_type']}")
                st.write(f"Item: {extracted_info['description']}")
                st.write(f"Item: {extracted_info['academic']}")
                st.write(f"Item: {extracted_info['experience']}")
                st.write(f"Item: {extracted_info['skills']}")
                st.write(f"Item: {extracted_info['salary']}")
                st.write(f"Item: {extracted_info['deadline']}")
                st.write(f"Item: {extracted_info['email']}")
                st.write(f"Item: {extracted_info['phone']}")
                st.write(f"Item: {extracted_info['keywords']}")
                st.write(f"Item: {extracted_info['website']}")
                st.write(f"Item: {extracted_info['how_to_apply']}")
        else:
            st.warning("Please enter a job posting.")


if __name__ == "__main__":
    main()
