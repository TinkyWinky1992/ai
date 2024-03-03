from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
import utils
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from note_engine import note_engine
from pdf import family_medicine_engine
import openai

file = os.path.join("data", "ai-description.txt")
context = utils.readfile(file)
openai.api_key = os.environ.get("KEY")
print(os.environ.get("KEY"))
llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=openai.api_key)

healthcare_datasets = os.path.join("data", "healthcare_dataset.csv")
healthcare_df = pd.read_csv(healthcare_datasets)
healthcare_query = PandasQueryEngine(df=healthcare_df, verbose=True, instruction_str=instruction_str, llm=llm)

healthcare_query.update_prompts({"pandas_prompt": new_prompt})

tools = {
    note_engine,

    QueryEngineTool(query_engine=family_medicine_engine, metadata=ToolMetadata(
        name="family medicine data",
        description=" this gives information and details about family medicine "
    )),
}


agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompts := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompts)
    print(result)
# if __name__ == '__main__':
# pass;
