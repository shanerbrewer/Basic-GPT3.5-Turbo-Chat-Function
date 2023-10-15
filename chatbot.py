import openai


openai.api_key = "insert OpenAI API key here"

def chat(role,prompt):
  chatcompletion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": role},
        {"role": "user", "content": prompt}
    ]
  )
  return(chatcompletion.choices[0].message.content)

chat_inputs = ["What is an axolotl?",
           "What is an amphibian", 
          ]

chat_role = "You are an expert on amphibians."
responses = []


for chat_input in chat_inputs:
  responses.append(chat(chat_role,chat_input))

for response in responses:
  print(response)

