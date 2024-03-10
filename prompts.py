from llama_index.core.prompts.base import PromptTemplate


new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print (df.head())`:
    {df_str}
    
    Follow these instruction:
    {instruction_str}
    Query: {query_str}
    
    Expression: """
)

