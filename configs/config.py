from configs.prompts import PromptConfig
from openai import OpenAI

import os
from dotenv import load_dotenv

class Config():
    def __init__(self, eval_data_path: str):
        self.eval_data_path = eval_data_path

    def setup_eval_config(self) -> None:
        try:
            api_key = os.getenv('OPENAI_APIKEY')
        
        except Exception as e:
            print(f"Exception occurred, liekly unable to fine environment variable in .env. "
                  "Ensure .env file exists and key is present without quotes or spaces. \nException Caught: {e}")
            raise e
        
        load_dotenv()

        if PromptConfig.eval_prompt:
            eval_prompt = PromptConfig.eval_prompt
        else:
            raise print("Eval prompt not found.")
        
        try:
            eval_client = OpenAI(api_key=api_key)
        except Exception as e:
            print(f"Error connecting to the client with the API key provided: {e}")
            raise e
            
        eval_client.responses.create(
            model="gpt-5.4-mini",
            input=eval_prompt
        )
            