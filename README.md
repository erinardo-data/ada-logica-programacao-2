# 🏫 Sistema de Gerenciamento de Alunos — Ada Tech | Turma 1735

Trabalho final da disciplina de **Lógica de Programação 2** do programa Ada Tech (Turma 1735), desenvolvido em Python puro.

## 📌 Sobre o projeto

O objetivo foi construir um sistema de banco de dados de alunos utilizando estruturas de dados aninhadas — dicionários dentro de dicionários e listas — sem o uso de bibliotecas externas ou bancos de dados relacionais.

O projeto demonstra domínio dos seguintes conceitos:

- Estruturas de dados compostas (dicionários e listas aninhados)
- Criação e organização de funções Python
- Tratamento de exceções com `try/except`
- Persistência de dados com `json` e `with open`
- Boas práticas de legibilidade e organização de código

## ⚙️ Funcionalidades implementadas

| Função | Descrição |
|---|---|
| `criar_escola_vazia()` | Inicializa a estrutura da escola |
| `adicionar_aluno()` | Cadastra um novo aluno com boletim |
| `cadastrar_nota()` | Adiciona nota a uma disciplina |
| `alterar_nota()` | Substitui uma nota por índice |
| `alterar_dado_cadastral()` | Atualiza dados do aluno |
| `visualizar_aluno()` | Exibe todos os dados de um aluno |
| `calcular_media()` | Calcula média e situação (aprovado/reprovado) |
| `apagar_aluno()` | Remove um aluno da escola |
| `analise_geral()` | Relatório agregado por disciplina |
| `contar_alunos()` | Retorna o total de alunos cadastrados |

## 🗂️ Estrutura de dados

```python
escola = {
    "id_01": {
        "nome": "Socrates de Souza",
        "nivel": "PhD",
        "idade": 45,
        "boletim": {
            "gramatica": [9.5, 10.0],
            "musica":    [8.7],
            "ginastica": [9.0]
        }
    }
}
```

## 📁 Arquivos

| Arquivo | Descrição |
|---|---|
| `erinardo_trabalho_ada_1735.ipynb` | Notebook Jupyter com células organizadas e comentadas |
| `erinardo_trabalho_ada_1735.py` | Versão em script Python puro |

## 🛠️ Como executar

```bash
# Clone o repositório
git clone git@github.com:erinardo-data/ada-logica-programacao-2.git

# Execute o script
python erinardo_trabalho_ada_1735.py
```

Ou abra o `.ipynb` no Jupyter e execute célula por célula.

---

Desenvolvido por **Erinardo Moura Araujo**

