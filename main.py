import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "what is the diffrent "}
#   ]
# )
#
# print(completion.choices[0].message)

chat_log = []

while True:
    user_message =input()
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
              messages=chat_log
        )
        assistant_response = response['choices'][0]['message']['content']
        print("ChatGPT: ", assistant_response.strip("\n").strip())
        chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})