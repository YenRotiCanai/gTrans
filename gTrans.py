from googletrans import Translator

translator = Translator()

Status = input('Type 1 to open the dict or 0 to exit and bye: ')

while Status == '1':
    enWord = input('English: ')

    zhWord = translator.translate(enWord, src='en', dest='zh-tw')

    print(zhWord.text + '\n')

    if enWord == '0':
        break

print('Bye.')