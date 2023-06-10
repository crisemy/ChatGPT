import openai
## My API Key generated from here >> https://platform.openai.com/account/api-keys
openai.api_key = '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'

messages = [ {"role": "system", "content":
    "You are a intelligent assistant."} ]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})