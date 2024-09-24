def count_a_in_string(string):
    count = string.lower().count('a')
    return count


string = input("Informe uma string: ")


count_a = count_a_in_string(string)
if count_a > 0:
    print(f"A letra 'a' (maiúscula ou minúscula) aparece {count_a} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
