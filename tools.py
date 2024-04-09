from llama_index.core.tools import QueryEngineTool, ToolMetadata
from pdf import family_medicine_engine
from Engine.engines import schedule_engine
from llama_hub.tools.wikipedia.base import WikipediaToolSpec

wiki_spec = WikipediaToolSpec()

# Update the metadata of the wiki_spec
wiki_spec.metadata = ToolMetadata(
    name="wikipedia_search",
    description="This tool allows you to search Wikipedia for any information."
)

# Get the search Wikipedia tool
tool = wiki_spec.to_tool_list()[1]

# Define the medicine-related tool
medicine_tool = QueryEngineTool(
    query_engine=family_medicine_engine,
    metadata=ToolMetadata(
        name="medicine_data",
        description="This tool provides detailed information about family medicine."
    ),
)

# Create a set of tools
tools = {
    schedule_engine,
    tool,
    medicine_tool,
}
