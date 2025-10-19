import google.generativeai as genai

API_KEY = 'AIzaSyA7Y5VBKTnR06z9qyvGh2VqQHwKKMYn4hA'

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

chat = model.start_chat()

while True:
    user_input = input('You: ')
    print('')
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print('Gemini: ', response.text)
