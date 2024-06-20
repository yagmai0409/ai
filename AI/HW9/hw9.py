import sys
from groq import Groq

def main():
    if len(sys.argv) < 3:
        print("Please provide language and question")
        return
    
    language = sys.argv[1].lower()
    if language not in ['ch', 'en']:
        print("Language option must be 'ch' or 'en'")
        return
    
    question = " ".join(sys.argv[2:]) + " Please answer in the chosen language"
    print(f"Selected language: {language}")
    print("Question:", question)

    # Initialize Groq client
    client = Groq(
        api_key="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",
    )

    # Send question and get completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )

    # Print the response
    print(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    main()
