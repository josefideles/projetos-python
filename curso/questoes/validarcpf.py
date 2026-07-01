import validate_cpf

cpf = input('Insira o seu CPF: ')
if validate_cpf.is_valid(cpf):
    print('CPF válido')
else:
    print('CPD inválido')
