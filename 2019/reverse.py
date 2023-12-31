def findFrequencyGroups(text: str):
    letters = []
    for letter in text:
        if letter not in letters:
            letters.append(letter)
    for letter in letters:
        print(f"Frequency of {letter}: {text.count(letter)}")

findFrequencyGroups("EAEEABDBFBCDF")