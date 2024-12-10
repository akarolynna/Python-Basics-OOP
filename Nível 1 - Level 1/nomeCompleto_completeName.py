# Faça um programa que imprima o nome completo de um usuário 
# Make a program that writes the user's full name to the terminal

class Usuario :
    def __init__(self, nome=None, sobrenome =None, idade =None, sexo =None, rg =None, cpf =None, dataNascimento=None, estadoCivil=None):
     self._nome = nome
     self._sobrenome = sobrenome
     self._idade = idade
     self._sexo = sexo
     self._rg = rg
     self._cpf = cpf
     self._dataNascimento= dataNascimento
     self._estadoCivil = estadoCivil
    
    def usuarioNomeCompleto(self):
        print("\n Informações sobre a usuária XXXXXX: \n")
        print(f"Nome do usuário: {self._nome} {self._sobrenome}\n")


if __name__ == "__main__":
    #usuario = Usuario(nome = "Anna", sobrenome = "Willians",idade =  21, sexo = "feminino", rg = "1954623897", cpf = "254445455", dataNascimento="07/01/2003", estadoCivil="solteira")
    #usuario.usuarioNomeCompleto()
    
    usuario = Usuario()
    usuario._nome = input("Escreva o seu nome: ")
    usuario._sobrenome = input("Escreva o seu sobrenome: ")
    usuario.usuarioNomeCompleto()