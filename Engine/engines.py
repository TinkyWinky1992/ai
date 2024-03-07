from llama_index.core.tools.function_tool import FunctionTool
from Engine import EngineUtils

#date_engine = FunctionTool.from_defaults(
 #   fn=EngineUtils.get_current_date_and_time(),
 #   name="date",
#    description="this tool provide date and time when the user ask for appointment "
#)
actionInput_engine = FunctionTool.from_defaults(
    fn=EngineUtils.save_note,
    name="schedule",
    description="this tool will help you providing appointment, write the problem of the user if he have , "
                "if not write {nothing}. "
)

