import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT_TEMPLATE = """
You are an expert Software Requirements Engineer.
Analyze the following app idea and provide a comprehensive Software Requirement Specification (SRS) breakdown.

App Idea:
"{idea_text}"

Return ONLY a valid JSON object without markdown block markers (no ```json).
The JSON object must strictly follow this key structure:

{{
  "target_users": ["List of target user roles/personas"],
  "inputs": ["Data or actions the user/system inputs"],
  "outputs": ["Data, alerts, or screens produced"],
  "functional_requirements": ["Core features and operational tasks"],
  "non_functional_requirements": ["Performance, security, scalability, usability specs"],
  "constraints": ["Technical, budgetary, or platform limitations"],
  "potential_challenges": ["Potential operational, technical, or adoption risks"]
}}
"""

def analyze_idea(idea_text):
    if not idea_text or not idea_text.strip():
        return {"error": "App idea cannot be empty."}

    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = PROMPT_TEMPLATE.format(idea_text=idea_text)

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()
        
        # Clean formatting tags if present
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
            
        data = json.loads(raw_text.strip())
        return data
    except Exception as e:
        return {"error": f"Failed to analyze requirements: {str(e)}"}
