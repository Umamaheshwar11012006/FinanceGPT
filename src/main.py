from app.model_loader import load_model
from app.chatbot import generate_response

print("Loading FinanceGPT...")

pipe = load_model()

print("FinanceGPT Ready!")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = generate_response(
        pipe,
        user_input
    )

    print("\nFinanceGPT:")
    print(response)