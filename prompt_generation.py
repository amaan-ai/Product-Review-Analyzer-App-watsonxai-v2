import json
    
def generate_entity_prompt(input_review):

    '''
    Parameters
    ----------
    input_review : str
        This is input review from the user.

    Returns
    -------
    entity_prompt : str
        prompt to be used as input to LLM for entity extraction.

    '''
    # Loading example entity data from the file
    with open('examples/examples_NER.json', 'r') as file:
        examples_data_NER = json.load(file)
    
    examples_data_NER_str = ""
    for item in examples_data_NER:
        i_examples_data_NER_str = str(item) + "\n"
        examples_data_NER_str = examples_data_NER_str + i_examples_data_NER_str + "\n"

    entity_prompt = f"""Given a product review as input. You have to extract the following entities from it, (only if they are present): 1) Person, 2) Email, 3) Phone, 4) Product, 5) Competitor. \n
    You can consider the following examples of reviews and corresponing extracted entities to see how it should be done. Here are examples: \n <start of examples> \n {examples_data_NER_str} \n <end of examples> \n
    Now, here's the review enclosed within 3 backticks from which you have to extract entities: \n <start of review> ``` {input_review} ``` <end of review> 
    Most Important point to note: a) Aways keep the structure of your 'Entities' response as illutrated in examples i.e. {{'Person':[<extracted entities>], 'Email':[<extracted entities>], 'Phone':[<extracted entities>], 'Product': [<extracted entities>], 'Competitor':[<extracted entities>]}} . b) In your response, only give extracted entities from the review and not from any examples. c) If entities are not present, do not hallucinate, can keep it blank.
    """

    return entity_prompt




def generate_sentiment_prompt(input_review):
    
    '''
    Parameters
    ----------
    input_review : str
        This is input review from the user.

    Returns
    -------
    entity_prompt : str
        prompt to be used as input to LLM for sentiment classification.

    '''
    
    sentiment_prompt = f"""Provide the sentiment (Positive / Negative / Neutral) of this product review: ```{input_review}``` """
    
    return sentiment_prompt



def generate_summary_prompt(input_review):

    '''
    Parameters
    ----------
    input_review : str
        This is input review from the user.

    Returns
    -------
    entity_prompt : str
        prompt to be used as input to LLM to generate summary.

    '''
    
    # Loading example summary data from the file
    with open('examples/examples_summary.json', 'r') as file:
        examples_data_summary = json.load(file)

    examples_data_summary_str = ""
    for item in examples_data_summary:
        i_examples_data_summary_str = str(item) + "\n"
        examples_data_summary_str = examples_data_summary_str + i_examples_data_summary_str + "\n"
        
        
    summary_prompt = f"""Given a product review as input. You have to generate a shorter summary of that review.
    You can consider the following examples of reviews and their corresponing summary to see how it should be done. Here are examples: \n <start of examples> \n {examples_data_summary_str} \n <end of examples> \n 
    Now, here's the review enclosed within 3 backticks from which you have to generate a short summary: \n <start of review> ``` {input_review} ``` <end of review>  
    Important point to note: a) Only provide generated summary in your response. b) Strictly do not exceed the summary by 200 characters.
    """
    
    return summary_prompt





     
     