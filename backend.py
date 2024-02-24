import requests as r
from openai import OpenAI
from llama_index.llms import OpenAI, ChatMessage, LLMMetadata
from llama_index.agent import ReActAgent

#Creds
semicolons_gateway_api_key = "" # Insert the provided API key
semicolons_gateway_base_url = ""

def process_data(text_data):
    # Process data (you can replace this with your specific backend logic)
    #text_data = "My Name is Pawan, I live in Chinchwad, I have completed my Graduation, I am currently working in a company names ABC Limited"
    prompt_data = f"""Please generate 10 questions and answers from the sentences/paragraph given ahead: {text_data}. For each Question that is generated, wirte answer for the that in the next line, Answers should be from the given paragraph / sentences only. This should be generated so that it can be used for exam paper preparation."""
    cleaned_promt =  prompt_data.replace('\n','')
    modelId="amazon.titan-text-express-v1"
    llm = OpenAI(
    model=modelId,
    api_key=semicolons_gateway_api_key,
    api_base=semicolons_gateway_base_url, # api_base represents the endpoint the Llama-Index object will make a call to when invoked
    temperature=0.1
    )   
    # Adjust the below parameters as per the model you've chosen
    llm.__class__.metadata = LLMMetadata(
    context_window=4000, 
    num_output=2000,
    is_chat_model=True,
    is_function_calling_model=False, 
    model_name=modelId,
    )
    response = llm.chat([ChatMessage(role="user",content={cleaned_promt})]).message.content
    result = "The Generated Questions are as below:\n {}".format(response)
    return result

if __name__ == "__main__":
    import sys

    # Retrieve text data from command line arguments
    text_data = sys.argv[1]

    result = process_data(text_data)

    print(result)