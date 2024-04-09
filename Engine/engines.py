from llama_index.core.tools.function_tool import FunctionTool
from wikipedia import cache

from appointment import getAppointment


def handle_schedule( problem, level):
    if not level:
        return "you have to rate the problem, if you don't have information ask more details"
    if not problem:
        return "describe your problem"
    print(type(level))
    try:
        level = int(level)
        getAppointment(level, problem)
        return "appointment saved"
    except Exception as e:
        print("PROBLEM: ", e)
        return "encountered a problem with the appointment"


schedule_engine = FunctionTool.from_defaults(
    fn=handle_schedule,
    name="schedule",
    description="this tool will provide you to make appointment to the user."

)
