from configs.config import PromptConfig
from configs.config import Config
from openai import OpenAI

import os
from dotenv import load_dotenv

import pandas as pd
from typing import List

def send_inputs_to_LLM(eval_input_data_path: str):
    """
    Function that takes a csv as an input & sends the input questions to a selected LLM
    URI/Endpoint & returns a csv of the responses.
    """
    def _setup_test_config():
        
        load_dotenv()
        api_key = os.getenv('OPENAI_APIKEY')


        test_prompt = PromptConfig.test_prompt
        target_client = OpenAI(api_key=api_key)

    def _send_question_to_model(target_client, test_prompt):
        response = target_client.responses.create(
            model="gpt-5.4-mini",
            input= test_prompt
        )
        return response
        
            
    data = pd.read_csv(rf"{eval_input_data_path}")
    
    # responses = List[str]
    questions_and_responses = dict[str:str]
    
    _ = data['input'].map(lambda row: _send_question_to_model(row))

    print(_)

    # for each row in df > wait 2 seconds > async send to LLM > append to respective key > write to csv


def main():

    load_dotenv()
    path = os.getenv("EVAL_INPUT_DATA_PATH")

    config = Config(path)
    config.setup_eval_config()

    send_inputs_to_LLM(eval_input_data_path=path)

    # api_key = os.getenv('OPENAI_APIKEY')
    # load_dotenv()

    # eval_prompt = PromptConfig.eval_prompt
    # client = OpenAI(api_key=api_key)

    # response = client.responses.create(
    #     model="gpt-5.4-mini",
    #     input= eval_prompt
    # )

    # print(response.output_text)

if __name__ == "__main__":
    main()