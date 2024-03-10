
# Example: reuse your existing OpenAI setup

from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")



def chat_with_llm(prompt):

    response = client.chat.completions.create(
        model = "gpt-4-0613",
        messages = [{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("User: ")

        if user_input.lower() in ["quit", "exit", "goodbye", "bye"]:
            break

        response = chat_with_llm(user_input)

        print("Chatbot: ", response)

