from Prac07.programminglanguage import ProgrammingLanguage


def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    print(ruby)

    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    print(python)

    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(vb)

    list_languages = [ruby, python, vb]

    print("The dynamically typed languages are:")

    for language in list_languages:
        if language.is_dynamic():
            print(language.name)

main()
