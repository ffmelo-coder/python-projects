# ZIP Password Cracker

**ZIP Password Cracker** é uma ferramenta moderna com interface gráfica para quebra de senha de arquivos ZIP protegidos utilizando wordlists. Desenvolvido em Python com interface amigável usando Tkinter e algoritmo de força bruta.

## Funcionalidades

- **Interface Gráfica Intuitiva** - Seleção fácil de arquivos através de botões verdes personalizados
- **Seletor de Arquivos** - Escolha o ZIP e wordlist através de diálogos nativos
- **Progresso em Tempo Real** - Barra de progresso com contadores detalhados e percentual
- **Controle de Execução** - Botões para pausar/retomar e parar o processo
- **Monitoramento Ativo** - Visualização da senha sendo testada no momento
- **Feedback Visual** - Interface responsiva com design moderno
- **Threading Seguro** - Interface não trava durante o processo
- **Relatórios Claros** - Notificações de sucesso, erro ou senha não encontrada

## Pré-requisitos

- **Python 3.7+**
- Instalar dependências:

```bash
pip install tqdm
```

## Como Funciona

O projeto utiliza um **algoritmo de força bruta** para tentar desbloquear arquivos ZIP protegidos por senha. O programa testa cada senha da wordlist `rockyou.txt` até encontrar a senha correta que permite extrair os arquivos contidos no ZIP.

### Algoritmo de Força Bruta

**Força bruta** é uma técnica de quebra de senha que tenta todas as combinações possíveis até encontrar a correta. Embora essa abordagem seja garantida para encontrar a senha (se ela estiver na wordlist), ela pode ser lenta dependendo do tamanho da lista e complexidade da senha.

## Como Usar

1. **Execute o programa:**

   ```bash
   python main.py
   ```

2. **Selecione os arquivos:**

   - Clique em "Browse" para escolher a wordlist (.txt)
   - Clique em "Browse" para escolher o arquivo ZIP protegido

3. **Inicie o processo:**

   - Clique no botão verde "Iniciar Crack"
   - Acompanhe o progresso em tempo real

4. **Controles durante execução:**

   - **Pausar/Retomar:** Clique em "Pausar" para interromper temporariamente
   - **Parar:** Clique em "Parar" para cancelar completamente

5. **Resultados:**
   - **Sucesso:** Senha será exibida na área de resultado
   - **Falha:** Mensagem informando que senha não foi encontrada
   - **Erro:** Detalhes do problema encontrado

## Interface

## Características Técnicas

- **zipfile** - Biblioteca nativa Python para manipulação de arquivos ZIP
- **Threading** - Interface responsiva durante processamento
- **Tkinter** - Interface gráfica nativa multiplataforma
- **tqdm** - Biblioteca para controle de progresso
- **Tratamento de Erros** - Validação de arquivos e exceções
- **Fonte Monospace** - Display estável das senhas sendo testadas

## Design

- **Botões Verdes** - Design moderno e intuitivo (#4CAF50)
- **Layout Responsivo** - Elementos bem organizados com grid
- **Progresso Detalhado** - Contador de tentativas e percentual
- **Feedback Imediato** - Status em tempo real
- **Controles Intuitivos** - Pausar/retomar/parar com estados visuais

## Código Principal

### Funcionalidades Principais

- **Interface Responsiva**: Threading para não travar a GUI
- **Progresso em Tempo Real**: Barra de progresso com contadores
- **Controle de Execução**: Pausar, retomar e parar processo
- **Validação de Arquivos**: Verificação antes de iniciar
- **Tratamento de Erros**: Exceções tratadas adequadamente

## Ambiente Virtual

1. **Crie o ambiente virtual:**

```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

- **Windows:**

```bash
.venv\Scripts\activate
```

- **Linux/macOS:**

```bash
source .venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install tqdm
```

## Execução

1. Coloque o arquivo ZIP protegido no diretório do projeto
2. Baixe e coloque uma wordlist (rockyou.txt) no projeto
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Use a interface gráfica para selecionar arquivos e iniciar o processo

## Exemplo de Saída

```
[+] Total de senhas para testar: 14,344,391
1,523,891/14,344,391 testados, 10.6% completo
Testando: admin123

[+] Senha encontrada: mypassword2023
Arquivos extraídos com sucesso!
```

## Arquivo de Teste

O projeto inclui:

- **[secret.zip](ZipCracker/secret.zip)** - Arquivo ZIP protegido para testes
- **[secret.txt](ZipCracker/secret.txt)** - Conteúdo: "You've cracked this zip file, yay!"
- **[rockyou.txt](ZipCracker/rockyou.txt)** - Wordlist com milhões de senhas comuns

## Uso Ético

Esta ferramenta deve ser usada apenas em:

- Arquivos ZIP próprios que você esqueceu a senha
- Testes de segurança autorizados
- Propósitos educacionais

## Instalação e Execução

1. **Clone o repositório:**

   ```bash
   git clone <repository-url>
   cd ZipCracker
   ```

2. **Instale as dependências:**

   ```bash
   pip install tqdm
   ```

3. **Execute o programa:**
   ```bash
   python main.py
   ```

## Aviso

Este projeto é **para fins didáticos** apenas. O uso deste código para tentar quebrar senhas de arquivos sem permissão é **ilegal** e não é incentivado de forma alguma. O autor não se responsabiliza pelo uso indevido deste código.

## Licença

Este projeto está licenciado sob a **Licença MIT**.

---

**Desenvolvido usando Python + Tkinter + zipfile**

### Contribuições

Agradecimentos ao professor Aramuni:
https://github.com/joaopauloaramuni
