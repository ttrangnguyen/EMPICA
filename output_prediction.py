from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
from joern import *
import pandas
import re

if __name__ == "__main__":

    model_id = "deepseek-ai/deepseek-coder-6.7b-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    model.config.temperature = 0.0

    MAX_TOKENS = 256
    df = pandas.read_csv("data/refactor_deepseek_6.7_java_v2.csv")
    columns =  ["function", "ReverseIf", "ReorderParameter", 'RenameVariable', 'ChangeCondition', 'RemoveConditionStatement', 'ChangeOperator', 'RemoveDefStatement', 'ForWhileConvert']
    for field_name in columns:
        count = 0
        file_name = "deepseek-coder-6.7_testoutput_"+ field_name +"_java.csv"
        count = 0
        for idx, row in df.iterrows():
            print("analyzing:", idx)
            data = {}
            try:
                source_content = df.at[idx, field_name]
                code = df.at[idx, "code"].split("\n")
                test_cases = []
                for line in code:
                    if line.strip().startswith("assert"):
                        if "==" in line:
                            testinput = line.split("==")[0]
                            testoutput = line.split("==")[1]
                        elif "equals" in line:
                            testinput = line.split(".equals")[0]
                            testoutput = line.split(".equals")[1]
                        testinput = testinput.replace("assert(", "")
                        testoutput = testoutput[:-2]
                        test_cases.append((testinput, testoutput))
                for (tin, tout) in test_cases:

                    chat = [
                        {"role": "user", "content": """Given the function: \n""" + source_content + "\n Predict the output of the given function for the test case " + tin},
                    ]

                    inputs = tokenizer.apply_chat_template(chat, return_tensors="pt", add_generation_prompt=True).to("cuda")
                    output = model.generate(input_ids=inputs, max_new_tokens=MAX_TOKENS)
                    output = output[0].to("cpu")
                    variables = ""
                    tmp = tokenizer.decode(output)

                    variables = tmp
                    print(tmp)
                    data[idx] = {"task_id": df.at[idx, "task_id"], "test input": tin, "expected output": tout, "response": variables}


                    if count == 0:
                        pandas.DataFrame.from_dict(data=data, orient='index').to_csv(file_name, index=False,
                                                                                     header=True)
                        count += 1
                    else:
                        pandas.DataFrame.from_dict(data=data, orient='index').to_csv(file_name, index=False,
                                                                                     header=False, mode='a')
                        count += 1

            except:
                print("Exception ", idx)
                continue