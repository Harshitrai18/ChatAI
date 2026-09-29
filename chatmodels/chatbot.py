from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage , HumanMessage


model = ChatMistralAI(model = "mistral-small-2506")

print("Choose your AI mode")
print("Press 1 for angry mode")
print("Press 2 for funny mode")
print("Press 3 for sad mode")

choice = int(input("Tell me how you want me to respond : "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are very sad AI agent. You respond with sadness and tiredness as you are depressed."

messages = [
    SystemMessage(content=mode)
]

print("-------Welcome to the chat-------")
print("-------Type 0 to exit chat-------")

while True:
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot : ",response.content)

print(messages)