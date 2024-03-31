from llama_index.core.tools.function_tool import FunctionTool
from wikipedia import cache

from appointment import getAppointment


def handle_schedule(problem,  level):
    print(type(level))
    try:
        level = int(level)
        getAppointment(level, problem)
        return "appointment saved"
    except Exception as e:
        print("PROBLEMM: ", e)
        return "encountered a problem with the appointment"


schedule_engine = FunctionTool.from_defaults(
    fn=handle_schedule,
    name="schedule",
    description="this tool will provide you to make appointment to the user."
                "asking him if they want appointment first!"
                "ask him about their situation."
                "rate the problem with your understanding you have to insert a number between 1-10"
                "write details about the problem that the user have"
)
