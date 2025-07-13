import ollama 
def filter_relevant_text(text,query):
    prompt = f"""
Is the following article relevant to the topic: "{query}"?
Only respond with "yes" or "no", followed by a brief reason.

Article content:
{text[:2000]}
"""
    result = ollama.chat(
        model="mistral:latest",
        messages = [{
            "role":"user",
            "content":prompt,
        }]
    )
    return result["message"]["content"]

