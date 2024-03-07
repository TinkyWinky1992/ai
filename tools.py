from argparse import Action

from llama_index.core.tools import QueryEngineTool, ToolMetadata
from pdf import family_medicine_engine
from Engine.engines import actionInput_engine
from llama_hub.tools.wikipedia.base import WikipediaToolSpec


wiki_spec = WikipediaToolSpec()

# Get the search Wikipedia tool
tool = wiki_spec.to_tool_list()[1]
# Define the medicine-related tool
medicine_tool = QueryEngineTool(
    query_engine=family_medicine_engine,
    metadata=ToolMetadata(
        name="medicine_data",
        description="this gives detailed information about family medicine"
    ),
)


tools = {
    tool,
    actionInput_engine,
    medicine_tool,
}