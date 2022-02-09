from translate import Translator

translator = Translator(to_lang='ja', from_lang='en')

with open('translate.txt') as f:
    text = f.read()

translation = translator.translate(text)

print(text)
print(translation)


