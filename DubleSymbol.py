print('Введіть рядок символів:')
string = input()
def double_simv_in_str(s):
    chars = list(s)
    newstr=""
    for i in range(len(s)):
        newstr = newstr+chars[i]+chars[i]
    return newstr

print('Рядок з подвоєнням символів у рядку:')
print(double_simv_in_str(string))
