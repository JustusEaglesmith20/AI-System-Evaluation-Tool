from configs.config import PromptConfig
from configs.config import Config
from openai import OpenAI

import os
from dotenv import load_dotenv

import pandas as pd

from abc import ABC, abstractmethod
from typing import List, Dict

'''
TODO:
Finish refactoring into interface -> adapter -> eval design
write code to load in csv into records struct
finish send_question_to_llm method refactor

'''

class TargetAIClient(ABC):    
    # TODO: Need to convert to async
    @abstractmethod
    def send_question_to_llm(records) -> str:
        ...


class OpenAIAdapter(TargetAIClient):
    def __init__(self, api_key: str, model:str = "gpt-5.4-mini"):
        self.api_key = api_key
        self.model = model
    
    def load_records() -> List[Dict]:
        pass


    def send_question_to_llm(records):
        openai_client = OpenAI(api_key=api_key)

        response = openai_client.responses.create(
                    model= model,
                    input= question
                )
            
    def send_question_to_llm(records):
        for q in records['question']:

            return response.output_text
            
         
        




class Evaluator(target_llm_client, llm_judge_client):
    
    def __init__(self, target_llm_client, llm_judge_client):
        self.target_llm_client = target_llm_client
        self.llm_judge_client = llm_judge_client

    def send_inputs_to_LLM_and_update_df(self, eval_input_data_path: str):
        """
        Function that takes a csv as an input & sends the input questions to a selected LLM
        URI/Endpoint & returns a csv of the responses.
        """
        client = OpenAI()
        

            
        data = pd.read_csv(eval_input_data_path)
        df = data.copy()
        target_llm_output = []
        for q in df['input']:
            resp = _send_question_to_model(q)
            target_llm_output.append(resp)

        df['target_llm_output'] = target_llm_output
        return df

    def llm_judge_evaluator(self, eval_output_data_path: str):
        """
        Function instantiates to update output dataset with judge analysis
        """
        judgeclient = OpenAI()        
        results = pd.read_csv(eval_output_data_path)

        def _evaluate_target_llm_qs(self, q):
            response = judgeclient.responses.create(
                model="gpt-5.4-mini",
                input= q
            )
            return response.output_text
            
        eval = []
        for q in results['target_llm_output']:
            resp = _evaluate_target_llm_qs(q)
            eval.append(resp)

        results['evaluation'] = eval
        return results

    def construct_data_model():
        pass

if __name__ == "__main__":
    load_dotenv()
    input_path = os.getenv("EVAL_INPUT_DATA_PATH")
    output_path = os.getenv("EVAL_OUTPUT_DATA_PATH")

    config = Config(input_path)
    config.setup_eval_config()

    try:
        test_df = send_inputs_to_LLM_and_update_df(eval_input_data_path=input_path)
    except Exception as e:
        print(f"Exception {e}: Failure when running send_inputs_to_LLM_and_update_df function.")

    test_df.to_csv(output_path)
    print (f"Results stored & writted to {output_path}")

    # Now I just need to have the second llm evaluate the responses.
    df_w_eval = llm_judge_evaluator(output_path)
    df_w_eval.to_csv(output_path)
