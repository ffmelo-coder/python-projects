# PDF Password Cracker

**PDF Password Cracker** é uma ferramenta moderna com interface gráfica para quebra de senha de arquivos PDF protegidos utilizando wordlists. Desenvolvido em Python com interface amigável usando Tkinter.

## Funcionalidades

- **Interface Gráfica Intuitiva** - Seleção fácil de arquivos através de botões
- **Seletor de Arquivos** - Escolha o PDF e wordlist através de diálogos
- **Progresso em Tempo Real** - Barra de progresso com contadores detalhados
- **Monitoramento Ativo** - Visualização da senha sendo testada no momento
- **Feedback Visual** - Botões com design moderno e responsivo
- **Threading Seguro** - Interface não trava durante o processo
- **Relatórios Claros** - Notificações de sucesso, erro ou senha não encontrada

## Pré-requisitos

- **Python 3.7+**
- Instalar dependências:
```bash
pip install pikepdf
```

## Como Usar

1. **Execute o programa:**
   ```bash
   python main.py
   ```

2. **Selecione os arquivos:**
   - Clique em "Selecionar" para escolher o PDF protegido
   - Clique em "Selecionar" para escolher sua wordlist (.txt)

3. **Inicie o processo:**
   - Clique no botão verde "Iniciar Crack"
   - Acompanhe o progresso em tempo real

4. **Resultados:**
   - **Sucesso:** Senha será exibida em popup
   - **Falha:** Mensagem informando que senha não foi encontrada
   - **Erro:** Detalhes do problema encontrado

## Interface

<img width="450" height="531" alt="image" src="https://github.com/user-attachments/assets/f2f6f6c7-31ac-4a21-a906-65b8eeddfd36" />



## Características Técnicas

- **pikepdf** - Performance superior ao PyPDF2
- **Threading** - Interface responsiva durante processamento
- **Tkinter** - Interface nativa multiplataforma
- **Tratamento de Erros** - Validação de arquivos e exceções
- **Fonte Monospace** - Display estável das senhas sendo testadas

## Design

- **Botões Verdes** - Design moderno e intuitivo (#5CB85C)
- **Layout Responsivo** - Elementos bem organizados
- **Progresso Detalhado** - Contador de tentativas e percentual
- **Feedback Imediato** - Status em tempo real

## 📈 Exemplo de Uso

```
Total de senhas: 14,344,391
1,523,891/14,344,391 testados, 10.6% completo
Testando: admin123

Senha encontrada: mypassword2023
```

## 💻 Código Principal

### Estrutura da Classe

```python
class PDFCrackerGUI:
    def __init__(self, root):
        # Configuração da janela principal
        self.root.title("PDF Password Cracker")
        self.root.geometry("450x500")
        
    def create_green_button(self, parent, text, command):
        # Botões verdes personalizados
        
    def setup_ui(self):
        # Interface gráfica completa
        
    def crack_pdf_password(self):
        # Lógica principal de quebra de senha
```

### Funcionalidades Principais

- **Interface Responsiva**: Threading para não travar a GUI
- **Progresso em Tempo Real**: Barra de progresso com contadores
- **Validação de Arquivos**: Verificação antes de iniciar
- **Tratamento de Erros**: Exceções tratadas adequadamente

## Uso Ético

Esta ferramenta deve ser usada apenas em:
- PDFs próprios que você esqueceu a senha
- Testes de segurança autorizados
- Propósitos educacionais

## Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone <repository-url>
   cd PdfCracker
   ```

2. **Instale as dependências:**
   ```bash
   pip install pikepdf
   ```

3. **Execute o programa:**
   ```bash
   python main.py
   ```

## Licença

Este projeto está licenciado sob a **Licença MIT**.

---

**Desenvolvido usando Python + Tkinter**

### Contribuições

Agradecimentos ao professor Aramuni:
https://github.com/joaopauloaramuni
