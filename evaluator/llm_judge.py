from configs.config import PromptConfig
from configs.config import Config
from openai import OpenAI

import os
from dotenv import load_dotenv

import pandas as pd

def send_inputs_to_LLM_and_update_df(eval_input_data_path: str):
    """
    Function that takes a csv as an input & sends the input questions to a selected LLM
    URI/Endpoint & returns a csv of the responses.
    """

    client = OpenAI()

    def _send_question_to_model(question):
        response = client.responses.create(
            model="gpt-5.4-mini",
            input= question
        )
        return response.output_text
        
    data = pd.read_csv(rf"{eval_input_data_path}")
    df = data.copy()

    for row in df:
        for q in df['input']: 
            resp = _send_question_to_model(q)
            df.loc[row,'target_llm_output'] = resp

    return df

def llm_judge_evaluator():
    pass

def construct_data_model():
    pass

if __name__ == "__main__":
    load_dotenv()
    path = os.getenv("EVAL_INPUT_DATA_PATH")

    config = Config(path)
    config.setup_eval_config()

    # TODO: Need to set up a data model for the required format of the CSV
    test_df = send_inputs_to_LLM_and_update_df(eval_input_data_path=path)
    print(test_df)
    # Now I just need to have the second llm evaluate the resposnes.