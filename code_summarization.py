from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
from joern import *
import pandas


if __name__ == "__main__":

    model_id = "deepseek-ai/deepseek-coder-6.7b-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    model.config.temperature = 0.0


    MAX_TOKENS = 1024
    df = pandas.read_csv("data/refactor_deepseek_6.7_java_v2.csv")
    columns =  ["function", "ReverseIf", "ReorderParameter", 'RenameVariable', 'ChangeCondition', 'RemoveConditionStatement', 'ChangeOperator', 'RemoveDefStatement', 'ForWhileConvert']
    for field_name in columns:
        count = 0
        filename = "deepseek-coder-6.7_summarize_"+ field_name +"_java.csv"
        for idx, row in df.iterrows():
            print("analyzing:", idx)
            data = {}
            try:
                source_content = df.at[idx, field_name]
                source_content = source_content
                chat = [
                    {"role": "user", "content": """Summarize the given source code: \n""" + source_content},
                ]
                inputs = tokenizer.apply_chat_template(chat, return_tensors="pt", add_generation_prompt=True).to("cuda")
                output = model.generate(input_ids=inputs, max_new_tokens=MAX_TOKENS)
                output = output[0].to("cpu")
                response = ""
                tmp = tokenizer.decode(output)
                response = tmp
                print(response)
                data[idx] = {"task_id": df.at[idx, "task_id"], "response": response}
    
                if count == 0:
                    pandas.DataFrame.from_dict(data=data, orient='index').to_csv(filename, index=False,
                                                                                 header=True)
                    count += 1
                else:
                    pandas.DataFrame.from_dict(data=data, orient='index').to_csv(filename, index=False,
                                                                                 header=False, mode='a')
                    count += 1

            except:
                print("Exception ", idx)
                continue