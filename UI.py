# import streamlit as st
# import groq
# import os                                                                                                                                                                                                          
# from dotenv import load_dotenv

# load_dotenv()
# client = groq.Groq(api_key=os.getenv("API_KEY"))

# def get_response(query):
#     response = client.chat.completions.create(messages=[
#     {
#         "role": "assistant",
#         "content": f'''${query}'''.strip(),
#     }
#     ],
#         model="llama3-70b-8192",
#     )
#     return f"Response to: {response.choices[0].message.content}"

# # Set the title of the app
# st.title('Simple Search Interface')

# # Create a search bar
# query = st.text_input('Enter your query here:', '',key=1)

# # Create a search button
# if st.button('Search'):
#     if query:
#         response = get_response(query)
#         st.write('### Response:')
#         st.write(response)
#     else:
#         st.write('Please enter a query.')







import streamlit as st
import groq
import os
from dotenv import load_dotenv

load_dotenv()
client = groq.Groq(api_key=os.getenv("API_KEY"))

def get_response(query):
    response = client.chat.completions.create(messages=[
        {
            "role": "assistant",
            "content": f'''{query}'''.strip(),
        }
    ],
        model="llama3-70b-8192",
    )
    return response.choices[0].message.content

st.title('Simple Search Interface')

if 'query' not in st.session_state:
    st.session_state.query = ''
if 'response' not in st.session_state:
    st.session_state.response = ''

query = st.text_input('Enter your query here:', value=st.session_state.query, key='query_input')

if st.button('Search'):
    if query:
        st.session_state.response = get_response(query)
        st.session_state.query = ''
        st.rerun();
    else:
        st.write('Please enter a query.')

if st.session_state.response:
    st.write('### Response:')
    st.write(st.session_state.response)
