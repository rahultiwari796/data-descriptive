import json
from difflib import get_close_matches


data = json.load(open('data.json','r'))


def translate(word):
    word=word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        isMean = input("Did you mean %s instead of %s ? if Yes enter Y , or if no enter N: " % (get_close_matches(word, data.keys())[0],word)).upper()
        if isMean == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif isMean == "N":
            return "Word doesn't exist. Please double check it !!"
        else:
            return "We didn't understand your entry"
    else:
        return "Word doesn't exist. Please double check it !!"


word = input("Enter the word: ")
response = translate(word)
if type(response) == list:
    for item in response:
        print(item)
else:
    print(response)
