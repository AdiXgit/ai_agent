import ollama
def summarise_article(text):
    prompt = f"""
Summarise the following article into 5-6 bullet points:
{text[:8000]} # Truncate to 6000 characters to avoid exceeding token limits
"""
    result = ollama.chat(
        model = "mistral:latest",
        messages = [{
            "role":"user",
            "content":prompt
        }]
    )
    return result["message"]["content"]

