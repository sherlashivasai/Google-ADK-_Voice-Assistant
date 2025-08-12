from google.adk.agents import Agent
from .template import Bujji_instructions 
from .tools import (
    create_event ,
    delete_event ,
    edit_event ,
    get_current_time ,
    list_events ,
)

root_agent = Agent(
    name = 'Bujji',
    model = 'gemini',
    description = "Agent to help with scheduling and calender operations ",
    instruction = Bujji_instructions,

)