# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Dados do aluno e curso** </font>
# 
# </div>

# %%
# Erinardo Moura Araujo;
# Turma 1735;  
# Trabalho ADA 1735.

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Escola com alunos** </font>
# 
# </div>

# %%
# Célula de rascunho — usado apenas para visualizar a estrutura
# A escola real é criada pela função criar_escola_vazia() abaixo

escola = {
    "id_01":{"nome": "Socrates de Souza", "nível": "PhD", "idade": 45, "boletim": {"gramatica": [9.5, 9.2, 8.6], "musica": [9.4, 8.3, 9.8], "ginastica": [8.5, 9.2, 9.4]}},
    "id_02":{"nome": "Platao do Prado", "nível": "PhD", "idade": 45, "boletim": {"gramatica": [9.5, 9.2, 8.6], "musica": [9.4, 8.3, 9.8], "ginastica": [8.5, 9.2, 9.4]}},
    "id_03":{"nome": "Aristoteles Alves", "nível": "PhD", "idade": 45, "boletim": {"gramatica": [9.5, 9.2, 8.6], "musica": [9.4, 8.3, 9.8], "ginastica": [8.5, 9.2, 9.4]}}
    }

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testanndo a busca nas camadas da função"** </font>
# 
# </div>

# %%
print(len(escola))

# %%
print(escola["id_01"])


# %%

print(escola["id_01"]["boletim"])


# %%

print(escola["id_01"]["boletim"]["musica"])


# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Escola vazia** </font>
# 
# </div>

# %%
def criar_escola_vazia():
    escola_vazia = {}
    return escola_vazia

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Criando a função "adicionar_aluno"** </font>
# 
# </div>

# %%
def adicionar_aluno(escola, matricula, nome, nivel, idade, turmas=None):
    
    if turmas is None:
        boletim = {}
    else:
        boletim = {disciplina: [] for disciplina in turmas}
    
    escola[matricula] = {
        "nome": nome,
        "nivel": nivel,
        "idade": idade,
        "boletim": boletim
    }

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testanndo a função"** </font>
# 
# </div>

# %%
# Uma solução para a falta de quebra de linha nesse código foi utilizar a lib "pprint", em vez de a "json". Embora "json" pareça uma solução mais elegante, preferi a "pprint", pela praticidade.
from pprint import pprint

minha_escola = criar_escola_vazia()

adicionar_aluno(minha_escola, "id_01", "Socrates de Souza", "PhD", 45, ["gramatica", "musica", "ginastica"])

adicionar_aluno(minha_escola, "id_02", "Platao do Prado", "Mestrado", 38,["gramatica","musica", "ginastica"])

adicionar_aluno(minha_escola, "id_03", "Aristoteles Alves", "Graduação", 32,
["gramatica", "musica", "ginastica"])

pprint(minha_escola)

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Criando a função "cadastrar_nota"** </font>
# 
# </div>
# 
# 

# %%
def cadastrar_nota(escola, matricula, disciplina, nota):
    try:
        escola[matricula]["boletim"][disciplina].append(nota)
    except KeyError:
        print(f"Matrícula '{matricula}' ou disciplina '{disciplina}' não encontrada.")
        

# %% [markdown]
# 
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testando a função"** </font>
# 
# </div>

# %%
cadastrar_nota(minha_escola, "id_01", "gramatica", 9.5)
cadastrar_nota(minha_escola, "id_01", "musica", 8.7)
cadastrar_nota(minha_escola, "id_01", "ginastica", 9.0)
cadastrar_nota(minha_escola, "id_01", "natacao", 8.0) # propositalmente para disparar o except

cadastrar_nota(minha_escola, "id_02", "gramatica", 7.5)
cadastrar_nota(minha_escola, "id_02", "musica", 8.0)
cadastrar_nota(minha_escola, "id_02", "ginastica", 7.8)

cadastrar_nota(minha_escola, "id_03", "gramatica", 8.5)
cadastrar_nota(minha_escola, "id_03", "musica", 9.1)
cadastrar_nota(minha_escola, "id_03", "ginastica", 8.9)

cadastrar_nota(minha_escola, "id_04", "musica", 7.8)  # propositalmente para disparar o except
pprint(minha_escola)


# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Criando a função "alterar_nota"** </font>
# 
# </div>

# %%
def alterar_nota(escola, matricula, disciplina, indice, nova_nota):
    try:
        escola[matricula]["boletim"][disciplina][indice] = nova_nota
    except KeyError:
        print(f"Matrícula '{matricula}' ou disciplina '{disciplina}' não encontrada.")
    except IndexError:
        print(f"Índice {indice} não existe na disciplina '{disciplina}'.")

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testando a função "alterar_nota"** </font>
# 
# </div>

# %%
alterar_nota(minha_escola, "id_01", "gramatica", 0, 10.0)
alterar_nota(minha_escola, "id_01", "gramatica", 99, 10.0)  # dispara IndexError
pprint(minha_escola["id_01"]["boletim"])

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Criando a função "alterar_dado_cadastral"** </font>
# 
# </div>

# %%
def alterar_dado_cadastral(escola, matricula, campo, novo_valor):
    try:
        if campo == "boletim":
            print("O boletim não pode ser alterado por esta função.")
            return
        escola[matricula][campo] = novo_valor
    except KeyError:
        print(f"Matrícula '{matricula}' ou campo '{campo}' não encontrado.")

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testando a função "alterar_dado_cadastral"** </font>
# 
# </div>

# %%
alterar_dado_cadastral(minha_escola, "id_01", "idade", 50)
alterar_dado_cadastral(minha_escola, "id_04", "idade", 50)  # dispara KeyError
pprint(minha_escola["id_01"])

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Criando a função "visualizar_aluno"** </font>
# 
# </div>

# %%
def visualizar_aluno(escola, matricula):
    try:
        aluno = escola[matricula]
        print(f"Matrícula : {matricula}")
        print(f"Nome      : {aluno['nome']}")
        print(f"Nível     : {aluno['nivel']}")
        print(f"Idade     : {aluno['idade']}")
        print("Boletim   :")
        for disciplina, notas in aluno["boletim"].items():
            print(f"  {disciplina}: {notas}")
    except KeyError:
        print(f"Matrícula '{matricula}' não encontrada.")

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testando a função "visualizar_aluno"** </font>
# 
# </div>

# %%
visualizar_aluno(minha_escola, "id_01")
visualizar_aluno(minha_escola, "id_04")  # dispara KeyError

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Criando a função "calcular_media"** </font>
#  </div>

# %%
def calcular_media(escola, matricula, disciplina, nota_minima=6.0):
    try:
        notas = escola[matricula]["boletim"][disciplina]
        nome = escola[matricula]["nome"]
        if len(notas) == 0:
            print("Nenhuma nota cadastrada para esta disciplina.")
            return
        media = sum(notas) / len(notas)
        situacao = f"Parabéns! Você foi APROVADO" if media >= nota_minima else "Você precisa estudar um pouco mais, pois foi infelizmente REPROVADO nessa disciplina!"
        print(f"Média em {disciplina}: {media:.2f} — {situacao}, {nome}!")
        return media, situacao
    except KeyError:
        print(f"Matrícula '{matricula}' ou disciplina '{disciplina}' não encontrada.")

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testando a função "calcular_media"** </font>
# 
# </div>

# %%
calcular_media(minha_escola, "id_01", "gramatica", 6.0)
calcular_media(minha_escola, "id_01", "musica", 6.0)
calcular_media(minha_escola, "id_01", "ginastica", 6.0)
calcular_media(minha_escola, "id_02", "gramatica", 6.0)
calcular_media(minha_escola, "id_02", "musica", 6.0)
calcular_media(minha_escola, "id_02", "ginastica", 6.0)
calcular_media(minha_escola, "id_03", "gramatica", 6.0)
calcular_media(minha_escola, "id_03", "musica", 6.0)
calcular_media(minha_escola, "id_03", "ginastica", 6.0)
calcular_media(minha_escola, "id_04", "musica")  # dispara KeyError

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Criando a função "apagar_aluno"** </font>
# 
# </div>

# %%
def apagar_aluno(escola, matricula):
    try:
        escola.pop(matricula)
        print(f"Aluno '{matricula}' removido com sucesso.")
    except KeyError:
        print(f"Matrícula '{matricula}' não encontrada.")

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testando a função "apagar_aluno"** </font>
# 
# </div>

# %%
apagar_aluno(minha_escola, "id_03")
apagar_aluno(minha_escola, "id_04")  # dispara KeyError
pprint(minha_escola)

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Criando a função "analise_geral"** </font>
# 
# </div>

# %%
def analise_geral(escola, nota_minima=6.0):
    resumo = {}
    for aluno in escola.values():
        for disciplina, notas in aluno["boletim"].items():
            if disciplina not in resumo:
                resumo[disciplina] = {"notas": [], "reprovados": 0, "total_alunos": 0}
            resumo[disciplina]["notas"].extend(notas)
            resumo[disciplina]["total_alunos"] += 1
            if len(notas) > 0 and (sum(notas) / len(notas)) < nota_minima:
                resumo[disciplina]["reprovados"] += 1

    for disciplina, dados in resumo.items():
        total = len(dados["notas"])
        media = sum(dados["notas"]) / total if total > 0 else 0
        taxa = dados["reprovados"] / dados["total_alunos"] * 100 if dados["total_alunos"] > 0 else 0
        print(f"{disciplina}: média={media:.2f} | avaliações={total} | reprovação={taxa:.1f}%")

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testando a função "analise_geral"** </font>
# 
# </div>

# %%
analise_geral(minha_escola)

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Criando a função "contar_alunos"** </font>
# 
# </div>

# %%
def contar_alunos(escola):
    return len(escola)

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Testando a função "contar_alunos"** </font>
# 
# </div>

# %%
print(f"Total de alunos remanescentes na escola = {contar_alunos(minha_escola)}")

# %% [markdown]
# <div style="border-left: 12px solid #fffb00; padding-left: 20px;">
# 
# ### <font color="#fffb00"> 🟢 **Salvando e carregando a escola em arquivo"** </font>
# 
# </div>

# %%
import json

# Salvar
with open("escola.json", "w", encoding="utf-8") as arquivo:
    json.dump(minha_escola, arquivo, ensure_ascii=False, indent=4)
    print("Escola salva em 'escola.json'.")

# Carregar
with open("escola.json", "r", encoding="utf-8") as arquivo:
    escola_carregada = json.load(arquivo)
    print("Escola carregada com sucesso.")
    pprint(escola_carregada)


