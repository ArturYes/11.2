def uppercase_string(text):
    return text.upper()


def capitalize_words(text):
    """
    Функция принимает строку и возвращает ее с заглавными первыми буквами каждого слова.

    Args:
        text (str): Входная строка.

    Returns:
        str: Строка с заглавными первыми буквами каждого слова.
    """
    return ' '.join(word.capitalize() for word in text.split())