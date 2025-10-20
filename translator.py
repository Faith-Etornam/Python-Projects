from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('hello/test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)

except FileNotFoundError as error:
    print('File does not exist')
    print(error)

except IOError as err:
    print('IO error')
    print(err)


# while True:
#     text = input('Please enter text: ')
#     translation = translator.translate(text)
#     print(translation)
#     print('')
#     if text == 'exit':
#         break

