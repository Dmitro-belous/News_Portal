from django import template


register = template.Library()


SWEAR_WORDS = {
    'редиска': 'р******',
    'идиот': 'и****',
    'говно': 'г****'
}


@register.filter()
def censor(text):
    try:
        str(text)
        word_list = text.split()
        for swear in SWEAR_WORDS:
            for i, word in enumerate(word_list):
                if swear[1:] in word:  # проверка со второй буквы, чтобы учесть верхний регистр
                    word_list[i] = word_list[i].replace(word, SWEAR_WORDS[swear])
        return ' '.join(word_list)
    except ValueError:
        print("Ошибка, невозможно применить фильтр к не строковым данным")
