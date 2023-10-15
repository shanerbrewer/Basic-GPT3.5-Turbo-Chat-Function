import openai


openai.api_key = "insert OpenAI API key here"



def chat(role,prompt):
  textstuff = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": role},
        {"role": "user", "content": prompt}
    ]
  )
  return(textstuff.choices[0].message.content)




chat_qs = ["What is an axolotl?",
           "What is an amphibian", 
          ]

chat_roles = ["You are an expert on amphibians."]
outputs = []

for x in chat_roles:
  for i in chat_qs:
    outputs.append(chat(x,i))

for p in outputs:
  print(p)
