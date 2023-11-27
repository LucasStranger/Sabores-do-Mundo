class PerfilAcesso:
    def __init__(self, nome, permissoes):
        self.nome = nome
        self.permissoes = permissoes

    def adicionar_permissao(self, permissao):
        self.permissoes.append(permissao)

    def listar_permissoes(self):
        return self.permissoes


class SistemaCadastroPerfis:
    def __init__(self):
        self.perfis = {}

    def criar_perfil(self, nome, permissoes):
        novo_perfil = PerfilAcesso(nome, permissoes)
        self.perfis[nome] = novo_perfil
        print(f"Perfil '{nome}' criado com sucesso.")

    def salvar_em_txt(self, nome_arquivo):
        with open(nome_arquivo + '.txt', 'w', encoding='utf-8') as file:
            for perfil in self.perfis.values():
                file.write(f"Nome do Perfil: {perfil.nome}\n")
                file.write(f"Permissões: {', '.join(perfil.permissoes)}\n\n")
        print(f"Dados salvos em '{nome_arquivo}.txt'.")

    def salvar_em_csv(self, nome_arquivo):
        import csv

        with open(nome_arquivo + '.csv', 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome do Perfil', 'Permissões'])
            for perfil in self.perfis.values():
                writer.writerow([perfil.nome, ', '.join(perfil.permissoes)])
        print(f"Dados salvos em '{nome_arquivo}.csv'.")


# Função para coletar as permissões do perfil
def coletar_permissoes():
    permissoes = []
    while True:
        permissao = input("Digite uma permissão (ou deixe em branco para terminar): ")
        if not permissao:
            break
        permissoes.append(permissao)
    return permissoes


# Exemplo de Uso:
sistema = SistemaCadastroPerfis()

# Coleta de dados para os perfis
nome_gerente = input("Digite o nome do Gerente: ")
print("Agora, digite as permissões para o Gerente:")
permissoes_gerente = coletar_permissoes()

nome_chef = input("Digite o nome do Chef de Cozinha: ")
print("Agora, digite as permissões para o Chef de Cozinha:")
permissoes_chef = coletar_permissoes()

nome_gerente_filial = input("Digite o nome do Gerente da Filial: ")
print("Agora, digite as permissões para o Gerente da Filial:")
permissoes_gerente_filial = coletar_permissoes()

# Criar perfis
sistema.criar_perfil(nome_gerente, permissoes_gerente)
sistema.criar_perfil(nome_chef, permissoes_chef)
sistema.criar_perfil(nome_gerente_filial, permissoes_gerente_filial)

# Salvar dados em arquivos .txt e .csv
sistema.salvar_em_txt("dados_perfis")
sistema.salvar_em_csv("dados_perfis")
