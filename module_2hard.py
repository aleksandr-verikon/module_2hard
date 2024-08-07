import random
def gen_code(num):
    code = ''
    for i in range(1,num):
        for j in range(1,num):
            if num%(i+j) == 0 and i<j:
                code += f'{i}{j}'
    return code
num = random.randint(3, 20)
code = gen_code(num)
print(f'{num} - {code}')