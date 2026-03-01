# Complexidade do Algortimo: IMPOSSIVEL ; 
class Livro :
    def __init__(self, nome_livro: str, nome_autor: str):
        self.titulo = nome_livro
        self.autor = nome_autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:        
            self.disponivel = False
            return True
        else: 
            return False
            
    def devolver(self) :
        if not self.disponivel: 
            self.disponivel = True
            return True
        return False
        
    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Disponibilidade: {self.disponivel}"

class Usuario :
    def __init__(self, num_ra :int, nome_aluno: str):
        self.ra = num_ra
        self.nome = nome_aluno
        self.lista_livro_emprestado = []

    def emprestar_livro(self,livro: object) :
        if livro.emprestar() == True :
            self.lista_livro_emprestado.append(livro)
            return f"Emprestimo realizado com sucesso "
        else:
           return f"O livro '{livro.titulo}' não esta disponivel para emprestimo"

    def devolver_livro(self,livro: object) :
        if livro not in self.lista_livro_emprestado:
            return "O usuário não possui esse livro."

        livro.devolver()
        self.lista_livro_emprestado.remove(livro)
        return f"O livro {livro.titulo} foi removido"
        
    def listar_livros(self):
        for i in self.lista_livro_emprestado :
            print(i)

class Biblioteca: 
    def __init__(self):
        self.lista_livro_cadastrado = []
        self.lista_usuarios_cadastrados = []

    def cadastrar_livro(self,livro:object) :
        for i in self.lista_livro_cadastrado:
            if i.titulo == livro.titulo:
              return f"O livro já foi cadastrado"
             
        self.lista_livro_cadastrado.append(livro)
        return f'Livro cadastrado'
    
    def cadastrar_usuario(self,usuario:object) :
        for i in self.lista_usuarios_cadastrados :
            if i.ra == usuario.ra :
                return f"O usuario já foi cadastrado"
        self.lista_usuarios_cadastrados.append(usuario)
        return 'usuario Cadastrado'
    
    def realizar_emprestimo(self,ra:int, titulo_livro:str) :
        usuario = None
        livro_escolhido = None

        for i in self.lista_usuarios_cadastrados :
            if i.ra == ra :
                usuario = i
                break
        
        for i in self.lista_livro_cadastrado: 
            if i.titulo == titulo_livro :
                livro_escolhido = i
                break

        if usuario == None: 
            return f'Usuario não encontrado.'
        elif livro_escolhido == None :
            return f'livro não encontrado.'
        else:

            if livro_escolhido.disponivel:
                return usuario.emprestar_livro(livro_escolhido)
            else: 
              return f"Não foi possivel pegar o livro emprestado"

    def realizar_devolucao(self, ra:int, titulo_livro:str) :
        usuario = None
        livro_escolhido = None

        for i in self.lista_usuarios_cadastrados :
            if i.ra == ra :
                usuario = i
                break
        
        for i in self.lista_livro_cadastrado: 
            if i.titulo == titulo_livro :
                livro_escolhido = i
                break
        
        if usuario == None: 
            return f'Usuario não encontrado.'
        elif livro_escolhido == None :
            return f'livro não encontrado.'
        else: 
          if livro_escolhido.disponivel == False :
            return usuario.devolver_livro(livro_escolhido)
          else: 
             return f"Não foi possivel devolver o livro emprestado"

    def listar_livros_disponiveis(self) :
        for i in self.lista_livro_cadastrado:
            if i.disponivel == True: 
                print(f"O livro {i.titulo} esta disponivel")
            else:
                continue

    def listar_livros_emprestados_usuario(self, ra: int) :
        usuario = None
        for i in self.lista_usuarios_cadastrados :
            if i.ra == ra :
                usuario = i
        if usuario == None: 
            return f'Usuario não encontrado.'
        else:
            print(f"Livros do usuario: {usuario.nome}\n")
            for i in usuario.lista_livro_emprestado:
                print(f"{i}\n")

biblioteca=Biblioteca()

while True:
    opcao = int(input(" 1 - Cadastrar livro \n 2 - Cadastrar usuário \n 3 - Emprestar \n 4 - Devolver \n 5 - Listar livros disponíveis \n 6- Listar livros emprestados ao usuário \n 7 - Sair \nEscolha: "))

    match opcao:
        case 1:
            nome_livro = input("Digite o Nome do livro: ")
            nome_autor = input("Digite o Nome do autor: ")

            livro = Livro(nome_livro,nome_autor)

            print(biblioteca.cadastrar_livro(livro))
        case 2:
            num_ra = int(input("Digite o Numero do seu RA: "))
            nome_aluno = input("Digite o seu Nome: ")

            usuario = Usuario(num_ra, nome_aluno)

            print(biblioteca.cadastrar_usuario(usuario))
        case 3:
            ra = int(input("Digite o Numero do seu RA: "))
            titulo_livro = input("Digite o Nome do livro: ")

            print(biblioteca.realizar_emprestimo(ra, titulo_livro))
        case 4:
            ra = int(input("Digite o Numero do seu RA: "))
            titulo_livro = input("Digite o Nome do livro: ")

            print(biblioteca.realizar_devolucao(ra,titulo_livro))

        case 5:

            biblioteca.listar_livros_disponiveis()
        
        case 6: 
            ra = int(input("Digite o Numero do seu RA: "))

            biblioteca.listar_livros_emprestados_usuario(ra)

        case 7:
            print("Finalizando...")
            break
        case _:
            print("Opção inválida")
