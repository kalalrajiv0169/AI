
#Write a program to identify the type of AI (Narrow, General, Super) based on input description.
while True:
    description = input("Enter description: ").lower()

    if "single task" in description or "one task" in description:
        print("This is Narrow AI")
    elif "multi task" in description or "human like" in description:
        print("This is General AI")
    elif "superior to human" in description or "better than human" in description:
        print("This is Super AI")
        break
    else:
        print("Type of AI could not be determined")
