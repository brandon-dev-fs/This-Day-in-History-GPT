import os

def model_prompt():
    openai = os.environ.get("OPENAI_MODEL")
    anthropic = os.environ.get("ANTHROPIC_MODEL")
    
    prompt = f"""
Please select which gen ai model you would like to use:
1 = {openai}
2 = {anthropic}
"""
    i = 0
    while (i != 1 and i != 2):
        j = input(prompt)
        if(j.isdigit()):
            i = int(j)
    
    return i