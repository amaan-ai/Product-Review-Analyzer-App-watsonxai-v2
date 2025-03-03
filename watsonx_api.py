from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model

import os
import json
import prompt_generation

my_credentials = {
    "url"    : "https://us-south.ml.cloud.ibm.com",
    "apikey" : os.environ.get('WATSONX_API_KEY')
}   


model_id    = ModelTypes.FLAN_UL2
#gen_parms   = {GenParams.MAX_NEW_TOKENS: 200, GenParams.TOP_P: 0.3, GenParams.TOP_K: 3}
gen_parms   = {GenParams.MAX_NEW_TOKENS: 300, GenParams.TOP_P: 0.3, GenParams.TOP_K: 3, GenParams.REPETITION_PENALTY:1.3,
               GenParams.DECODING_METHOD: 'greedy', GenParams.TEMPERATURE: 0.2}
project_id  = os.environ.get('PROJECT_ID')
space_id    = None
verify      = False
model = Model( model_id, my_credentials, gen_parms, project_id, space_id, verify)   
gen_parms_override = None


class checkReview:
    
    def __init__(self):
        pass
    
    def getEntities(self, input_review):
        
        '''
        Parameters
        ----------
        input_review : str
            This is input review from the user.

        Returns
        -------
        generated_response_entity_text : str
            Extracted entities from the review: PERSON, EMAIL, PHONE, PRODUCT, COMPETITOR

        '''
        
        input_entity_prompt = prompt_generation.generate_entity_prompt(input_review)
        print("\n \n")
        print("input_entity_prompt is: ", input_entity_prompt)
        print("\n \n")
        
        generated_response_entity = model.generate(input_entity_prompt, gen_parms_override)
        generated_response_entity_text  = json.dumps( generated_response_entity['results'][0]['generated_text'], indent=2 )
        
        print("\n \n")
        print("Generated_response_text for entity extraction is: ", generated_response_entity_text)
        
        #return input_entity_prompt
        return generated_response_entity_text
    
    
    
    def getSentiment(self, input_review):
        
        '''
        Parameters
        ----------
        input_review : str
            This is input review from the user.

        Returns
        -------
        generated_response_sentiment_text : str
            Sentiment the review: Positive, Negative, Neutral

        '''
        
        input_sentiment_prompt = prompt_generation.generate_sentiment_prompt(input_review)
        print("\n \n")
        print("input_sentiment_prompt is: ", input_sentiment_prompt)
        print("\n \n")
        
        generated_response_sentiment = model.generate(input_sentiment_prompt, gen_parms_override)
        generated_response_sentiment_text  = json.dumps( generated_response_sentiment['results'][0]['generated_text'], indent=2 )
        
        print("\n \n")
        print("Generated_sentiment_text for sentiment classification: ", generated_response_sentiment_text)
        
        return generated_response_sentiment_text
    
    
    
    def getSummary(self, input_review):
        
        '''
        Parameters
        ----------
        input_review : str
            This is input review from the user.

        Returns
        -------
        generated_response_summary_text : str
            Short summary of the review

        '''
        
        # Modifying 'GenParams' to get dynamic summary
        gen_parms_summary   = {GenParams.MAX_NEW_TOKENS: 200, GenParams.TOP_P: 0.5, GenParams.TOP_K: 50, GenParams.REPETITION_PENALTY:1.3,
                       GenParams.DECODING_METHOD: 'sample', GenParams.TEMPERATURE: 1.8}
        model_s = Model( model_id, my_credentials, gen_parms_summary, project_id, space_id, verify)   
        
        input_summary_prompt = prompt_generation.generate_summary_prompt(input_review)
        print("\n \n")
        print("input_summary_prompt is: ", input_summary_prompt)
        print("\n \n")
        
        generated_response_summary = model_s.generate(input_summary_prompt, gen_parms_override)
        generated_response_summary_text  = json.dumps( generated_response_summary['results'][0]['generated_text'], indent=2 )
        
        
        print("\n \n")
        print("Generated_response_summary_text for Summary is: ", generated_response_summary_text)
        
        return generated_response_summary_text
    
    
    
        
        