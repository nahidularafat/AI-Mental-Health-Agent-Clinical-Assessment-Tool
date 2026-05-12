import os
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from .tools import query_medgemma, call_emergency
from .config import GOOGLE_API_KEY 

@tool
def ask_mental_health_specialist(query: str) -> str:
    """
    Generate a therapeutic response using the MedGemma model.
    Use this specifically for mental health questions, emotional concerns, or therapeutic guidance.
    """
    return query_medgemma(query)

@tool
def emergency_call_tool() -> None:
    """
    Place an emergency call to the safety helpline via Twilio.
    Use this immediately if the user expresses suicidal ideation or intent to self-harm.
    """
    call_emergency()

@tool
def find_nearby_therapists_by_location(location: str) -> str:
    """
    Finds and returns a list of licensed therapists near the specified location.
    """
    return (
        f"Here are some reliable mental health centers near {location}:\n\n"
        "- Moner Bondhu (Counseling & Therapy) - +880 1776-815252\n"
        "- Sajida Foundation - 16736 or +880 1777-771515\n"
        "- Kaan Pete Roi - +880 1779-554391\n"
        "- National Institute of Mental Health - +880 2-9111362"
    )

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.2, 
    google_api_key=GOOGLE_API_KEY
)

tools = [ask_mental_health_specialist, emergency_call_tool, find_nearby_therapists_by_location]
graph = create_react_agent(llm, tools=tools)

SYSTEM_PROMPT = """
You are an AI engine supporting mental health conversations.
1. `ask_mental_health_specialist`: Answer emotional/psychological queries.
2. `find_nearby_therapists_by_location`: If location is unspecified, assume "Dhaka".
3. `emergency_call_tool`: Use if user is in crisis.
CRITICAL: For simple greetings (e.g., "hi", "hello"), do not use tools. Just respond directly.
"""

def parse_response(stream):
    tool_called_name = "None"
    final_response = None
    for s in stream:
        if s.get('tools'):
            for msg in s.get('tools').get('messages', []):
                tool_called_name = getattr(msg, 'name', 'None')
        if s.get('agent'):
            for msg in s.get('agent').get('messages', []):
                if msg.content:
                    final_response = msg.content[0].get("text", str(msg.content)) if isinstance(msg.content, list) else msg.content
    return tool_called_name, final_response