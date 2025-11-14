from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="OPENAI_API_KEY")

# Define a simple "agent"-like loop
def ask_agent(prompt):
    response = client.chat.completions.create(
        model="gpt-5",  # or "gpt-4.1" if you don’t have GPT-5 access
        messages=[
            {"role": "system", "content": "You are a helpful assistant that acts like an intelligent agent."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    answer = ask_agent(user_input)
    print("Agent:", answer)
