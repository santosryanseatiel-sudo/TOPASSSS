try:
    note1 = input("Enter a short note: ")
    with open("notes.txt", "w") as file:
        file.write(note1 + "\n")

    print("\n--- File Content ---")
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)

    note2 = input("\nEnter another note: ")
    with open("notes.txt", "a") as file:
        file.write(note2 + "\n")

    print("\n--- Updated File Content ---")
    with open("notes.txt", "r") as file:
        updated_content = file.read()
        print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print("An error occurred:", e)