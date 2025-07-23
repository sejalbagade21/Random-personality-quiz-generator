import random

# List of quirky questions and answer options
questions = [
    {
        'question': "What's your favorite way to spend a lazy Sunday?",
        'options': ['Napping', 'Binge-watching shows', 'Eating snacks', 'Inventing new hobbies']
    },
    {
        'question': "Pick a superpower:",
        'options': ['Invisibility', 'Flying', 'Talking to animals', 'Making perfect coffee']
    },
    {
        'question': "Which animal do you vibe with most?",
        'options': ['Sloth', 'Panda', 'Cat', 'Otter']
    },
    {
        'question': "Choose a snack:",
        'options': ['Pizza', 'Sushi', 'Ice cream', 'Tacos']
    },
    {
        'question': "What’s your spirit beverage?",
        'options': ['Coffee', 'Bubble tea', 'Smoothie', 'Hot chocolate']
    }
]

# List of funny personality ingredients
ingredients = [
    'panda', 'coffee', 'sloth', 'pizza', 'cat', 'bubble tea', 'otter', 'ice cream', 'taco', 'smoothie'
]

def ask_questions():
    print("Welcome to the Random Personality Quiz!\n")
    answers = []
    for idx, q in enumerate(questions):
        print(f"Q{idx+1}: {q['question']}")
        for i, opt in enumerate(q['options']):
            print(f"  {i+1}. {opt}")
        while True:
            try:
                choice = int(input("Your choice (1-4): "))
                if 1 <= choice <= 4:
                    answers.append(choice)
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        print()
    return answers

def generate_result(answers):
    # Pick two random ingredients for the personality
    ing1, ing2 = random.sample(ingredients, 2)
    # Randomly assign percentages
    percent1 = random.randint(20, 80)
    percent2 = 100 - percent1
    result = f"You are {percent1}% {ing1} and {percent2}% {ing2}!"\
             f"\nThat's a unique combo!"
    return result

def export_certificate(result):
    filename = "personality_certificate.txt"
    with open(filename, 'w') as f:
        f.write("*** Your Random Personality Certificate ***\n\n")
        f.write(result + "\n")
        f.write("\nShare your result with friends!")
    print(f"\nCertificate saved as '{filename}'.")

def main():
    answers = ask_questions()
    result = generate_result(answers)
    print("\n--- Your Personality Result ---")
    print(result)
    export = input("\nWould you like to export your certificate? (y/n): ").strip().lower()
    if export == 'y':
        export_certificate(result)
    else:
        print("No certificate exported. Have a great day!")

if __name__ == "__main__":
    main() 
