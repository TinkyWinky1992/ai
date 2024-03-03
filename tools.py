from llama_index.core.tools import QueryEngineTool, ToolMetadata
from pdf import family_medicine_engine
from note_engine import note_engine

tools = {
    note_engine,

    QueryEngineTool(query_engine=family_medicine_engine, metadata=ToolMetadata(
        name="family medicine data",
        description=" this gives information and details about family medicine "
    )),
}