# Descobrir se uma palavra é um palíndromo. Ex.: ovo, Natan Desconsiderar letras maiúscula e minúscula

def prepary_word(string):
    return string.lower()

def Create_list_letters(word):
    return list(word)

def verify_palinder(list):
    start = 0
    end = (len(list) - 1)
    while (start < end):
        if (list[start] != list[end]):
            return "It is not a palinder"
        start = start + 1
        end = end - 1
    result = ("It is a palinder")
    return result
            
    
adapted_word = prepary_word("arara")
ready_list = Create_list_letters(adapted_word)
result = verify_palinder(ready_list)
print(result)