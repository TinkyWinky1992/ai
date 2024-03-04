from llama_index.core.tools.function_tool import FunctionTool
from Engine import EngineUtils

actionInput_engine = FunctionTool.from_defaults(
    fn=EngineUtils.get_actionInput,
    name="get action input",
    description="this tool use for getting the action input when you need a tool to help with your assist"
)
note_engine = FunctionTool.from_defaults(
    fn=EngineUtils.save_note,
    name="note_saver",
    description="this tool can save a text based note t",
)
