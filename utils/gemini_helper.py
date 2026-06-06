from google import genai
import os, time
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-2.5-flash" 

def get_gemini_response(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            return response.text

        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                wait_time = 30 * (attempt + 1)
                print(f"Rate limit hit. Waiting {wait_time}s...")
                time.sleep(wait_time)
            elif "404" in error_msg or "NOT_FOUND" in error_msg:
                return "❌ Model not found. Please check available models."
            else:
                return f"❌ Error: {error_msg}"
    return "⚠️ Max retries reached. Try again later."