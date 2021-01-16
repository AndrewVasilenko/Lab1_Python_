print('Введіть рядок символів:')
string = input()

def rev_str(s):
    return "".join(reversed(s))

print('Рядок символів вистроїних в зворотньому порядку:')
print(rev_str(string)) 
   
