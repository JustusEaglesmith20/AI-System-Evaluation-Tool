from configs.config import PromptConfig
from configs.config import Config
from openai import OpenAI

import os
from dotenv import load_dotenv

import pandas as pd

def send_inputs_to_LLM(eval_input_data_path: str):
    """
    Function that takes a csv as an input & sends the input questions to a selected LLM
    URI/Endpoint & returns a csv of the responses.
    """

    client = OpenAI()

    def _send_question_to_model(question) -> str:
        response = client.responses.create(
            model="gpt-5.4-mini",
            input= question
        )
        return response.output_text
        
    data = pd.read_csv(rf"{eval_input_data_path}")

    answers:dict[str,str] = {}
    question = ""
    data

    qa_dict = {q: _send_question_to_model(q) for q in data['input']}

    return qa_dict

if __name__ == "__main__":
    load_dotenv()
    path = os.getenv("EVAL_INPUT_DATA_PATH")

    config = Config(path)
    config.setup_eval_config()

    qa_dict = send_inputs_to_LLM(eval_input_data_path=path)

    # Now I just need to have the second llm evaluate the resposnes.