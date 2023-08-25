import streamlit as st

from watsonx_api import checkReview
checkReview_obj = checkReview()

st.markdown(
    """
    <style>
    .stButton>button {
        margin: 0 auto;
        display: block;
    }
    
    .output {
        background-color: #e0f0ff;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    
    .st-spinner {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    }
    
    </style>
    """,
    unsafe_allow_html=True,
)




# Creating the Streamlit app page

# Adding link to my GitHub repository
github_link = """
<div style='float: right;'>
    <a href='https://github.com/amaan-ai/Product-Review-Analyzer-App-watsonxai'>
        <img src='https://img.shields.io/badge/GitHub-Repo-green?style=flat-square&logo=github'>
    </a>
</div>
"""
st.markdown(github_link, unsafe_allow_html=True)

# Adding a header and project description
st.title("Review Analyzer App - Watsonx.ai")
st.write("One-stop solution for Review Analysis: Entity detection (PERSON, EMAIL, PHONE, PRODUCT, COMPETITOR), Sentiment assessment, and concise summarization.")

# Creating a layout with two columns
col1, col2 = st.columns(2)

# In the left column, creating a text area for user input
with col1:
    st.write("Please enter a review below:")
    max_chars_length = 3000
    #input_text = st.text_area("", height=300, max_chars=max_chars_length)  # Default height is set to 300 pixels, you can adjust as needed
    input_text = st.text_area("", placeholder="(min 60 chars)", height=300, max_chars=max_chars_length)
    
# In the right column, displaying the output text (initially empty)
with col2:
    st.write("Output:")
    # We'll initialize this with an empty string, but it will be updated later
    output_text_area = st.empty()

# Creating a button below the columns
run = st.button("Check Review")
if run:
    
    # Adding a check for minimum length of review
    if len(input_text) > 60 and input_text.isspace()==False:
        input_text = str(input_text)
        
    else:
        st.error("Review length too short to analyze. Please re-run with longer review. Thanks!")
        st.stop()
    
    # Adding a check for maximum length of review
    if len(input_text) > max_chars_length:
        st.error("Length of you Review exceeds 3000 characters. Please re-run with shorter review. Thanks!")
        st.stop()
    
    
    # 1. Extracting entities from review 
    with st.spinner('Checking presence of entities...'):
        # BELOW line only for testing 
        #input_text =  "I recently purchased the Galaxy S25 from Samsung, and I must say I'm thoroughly impressed. The battery life is phenomenal, and the camera quality is top-notch. However, I did face some issues with the customer support team when I tried reaching out to them at support@samsung.com. I also found that the iPhone 14 has a slightly better user interface." # TESTING
        entities = checkReview_obj.getEntities(input_text) # str
        entities = "Here are detected Entities: \n" + entities

        
    # 2. Getting sentiment of the review 
    with st.spinner('Checking sentiment of the review...'):
        sentiment = checkReview_obj.getSentiment(input_text) # str
        sentiment = "Sentiment: \n" + sentiment
        
        
    # 3. Getting one line summary of the review
    with st.spinner('Getting one line summary of the review...'):
        summary = checkReview_obj.getSummary(input_text) # str
        summary = "Summary: \n" + summary
        
        
    # Updating the output text area with the combined results
    combined_result = entities + "\n \n \n" + sentiment + "\n \n \n" + summary
    output_text_area.text_area("", value=combined_result, height=600)
    