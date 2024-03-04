from llama_index.core.tools import QueryEngineTool, ToolMetadata
from pdf import family_medicine_engine
from Engine.engines import note_engine, actionInput_engine
from llama_hub.tools.wikipedia.base import WikipediaToolSpec

wiki_spec = WikipediaToolSpec()
# Get the search wikipedia tool
tool = wiki_spec.to_tool_list()[1]
tools = {
    tool,
    note_engine,
    actionInput_engine,
    QueryEngineTool(query_engine=family_medicine_engine, metadata=ToolMetadata(
        name="medicine-data",
        description=" this gives information and details about family medicine "
    )),

}