#rafael castillo
#cs50 python
#program problems set 1 #1 

def main():
    # Prompt the user for their answer
    user_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    # Convert the user's answer to lowercase for case-insensitive comparison
    user_answer_lower = user_answer.lower()

    # Check if the answer is 42, "forty-two," or "forty two" (case-insensitively)
    if user_answer_lower == "42" or user_answer_lower == "forty-two" or user_answer_lower == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()

