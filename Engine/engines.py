from llama_index.core.tools.function_tool import FunctionTool

from Engine.EngineUtils import save_schedule

schedule_engine = FunctionTool.from_defaults(
    fn=save_schedule,
    name="schedule",
    description="This tool will help you provide an appointment. Write the problem of the user if he has one, "
                "if not, write {nothing}. This tool will be activated only when the user requests an appointment."
)
