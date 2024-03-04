from llama_index.core.tools.function_tool import FunctionTool
from Engine import EngineUtils

actionInput_engine = FunctionTool.from_defaults(
    fn=EngineUtils.get_actionInput,
    name="schedule-appointment",
    description="this tool will help you providing appointment, you need to give time and date. "
)
note_engine = FunctionTool.from_defaults(
    fn=EngineUtils.save_note,
    name="note_saver",
    description="this tool can save a text based note t",
)
