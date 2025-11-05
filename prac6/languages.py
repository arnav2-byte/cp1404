from programming_language import ProgrammingLanguages
def main():   # creates the main display for languages
    python = ProgrammingLanguages("python", "Dynamic", "True", 1991)
    ruby = ProgrammingLanguages("ruby", "Dynamic", "False", 1991)
    visual_basic = ProgrammingLanguages("Visual Basic", "Static", False, 1991)

    print(python)
    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
           print(language.name)

if __name__ == "__main__":
    main()