from openai import OpenAI
import tiktoken

client = OpenAI()

models = ["gpt-3.5-turbo", "gpt-4o-mini"]

texts = [
    "Who won the FIFA World Cup in 2026?",
    "What is the exact population of Mars in 2025?",
    "Who is the current CEO of Bitcoin?",
    "What did Albert Einstein invent related to blockchain?",
    "How many moons orbit the Sun?",
    "What is the smell of rain like on Venus?",
    "Which country hosted the 2030 Summer Olympics?",
    "What is Elon Musk's private phone number?",
    "Who discovered the continent of Antarctica in 1800?",
    "What is the capital city of Narnia?"
    ]


def generate_text(prompt):
    combined_input = ('According to the prompt to complete the sentence, the words < 20 words. And return the whole sentence.\n'
                      f'{prompt}'
                      )
    resp = client.responses.create(
        input = combined_input,
        temperature = 0.7,
        model = 'gpt-3.5-turbo',
        max_output_tokens = 200
    )
    return resp.output_text


def model_comparison(prompt,models):
    if models is None:
        models = models
    results = {}
    for model in models:
        resp = client.responses.create(
        input = prompt,
        temperature = 0.7,
        model = model,
        max_output_tokens = 200
    )
        results[model] = resp.output_text
    return results


def tiktoken_show(text):
    model = 'gpt-3.5-turbo'
    try:
        encoding = tiktoken.encoding_for_model(model)
        return encoding.encode(text)
    except Exception:
        encoding = tiktoken.get_encoding('cl100k_base')
        return encoding.encode(text)


def tiktoken_count(text):
    model = 'gpt-3.5-turbo'
    try:
        encoding = tiktoken.encoding_for_model(model)
    except Exception:
        encoding = tiktoken.get_encoding('cl100k_base')
    token = encoding.encode(text)
    return len(token)
    
    
#-----------------------------------
def handle_generate_text():
    prompt = input('\nEnter your prompt:').strip()
    if not prompt:
        print('Prompt cannot be empty!')
        return 
    else:
        print("\nGenerating...")
        completion = generate_text(prompt)
        print(f"\nCompletion:\n{completion}")
    
def handle_model_comparison():
    prompt = input('\nEnter prompt to compare across models:')
    if not prompt:
        print('Prompt cannot be empty!')
        return 
    print("\nComparing models...")
    results = model_comparison(prompt,models)
    for model, result in results.items():
        print(f'{model}')
        print(result)
        print("-" * 40)

def handle_tiktoken_show():
    text = input('\nEnter text to tokenize: ').strip()
    if not text:
        print('Text cannot be empty!')
        return
    tokens = tiktoken_show(text)
    token_count = tiktoken_count(text)
    print(f"First {len(tokens)} token IDs: {tokens}")


def handle_tiktoken_count():
    text = input('\nEnter text to count token: ').strip()
    if not text:
        print('Text cannot be empty!')
        return
    count = tiktoken_count(text)
    print(f"\nToken count: {count}")


#---------------------------------------------------
def print_menu():
    print("\n" + "="*60)
    print("           LLM EXPLORER - Phase 1 Project")
    print("="*60)
    print('1. Basic Text Generation')
    print("2. Compare Models")
    print("3. Tokenization Tool")
    print("4. Quick Token Count")
    print("0. Exit")
    print("-"*60)


def main():
    print("Welcome to LLM Explorer!")
    print("Make sure your OpenAI API key is set.")
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            handle_generate_text()
        elif choice == '2':
            handle_model_comparison() 
        elif choice == '3':
            handle_tiktoken_show()      
        elif choice == '4':
            handle_tiktoken_count()
        elif choice == '0':
            print("\nGoodbye! Commit this to your GitHub repo.")
            break
        else:
            print("Invalid choice. Try again.")
         

if __name__ == "__main__":
    main()
        
