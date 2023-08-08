def caps_string(input_string):
<<<<<<< HEAD
    return input_string.upper()

def capitalize_words(input_string):
    '''
    Новая функция, которая делает заглавными первые буквы каждого слова в строке, поступившей на вход функции.
    '''
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

