from pathlib import Path
import pikepdf
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading


class PDFCrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Password Cracker")
        self.root.geometry("450x500")
        self.root.resizable(False, False)

        self.pdf_path = tk.StringVar(value="protected.pdf")
        self.wordlist_path = tk.StringVar(value="rockyou.txt")
        self.progress_var = tk.DoubleVar()
        self.status_var = tk.StringVar(value="Pronto para iniciar")

        self.setup_ui()

    def create_green_button(self, parent, text, command):
        """Botão verde personalizado"""
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg="#5CB85C",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            bd=0,
            padx=15,
            pady=8,
            activebackground="#449D44",
            activeforeground="white",
            cursor="hand2",
        )

    def setup_ui(self):
        # Principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Titulo
        ttk.Label(
            main_frame, text="PDF Password Cracker", font=("Arial", 16, "bold")
        ).pack(pady=(0, 20))

        # Arquivo PDF
        pdf_frame = ttk.LabelFrame(main_frame, text="Arquivo PDF", padding="10")
        pdf_frame.pack(fill=tk.X, pady=5)

        pdf_entry_frame = ttk.Frame(pdf_frame)
        pdf_entry_frame.pack(fill=tk.X)

        ttk.Entry(pdf_entry_frame, textvariable=self.pdf_path).pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10)
        )
        self.create_green_button(pdf_entry_frame, "Selecionar", self.select_pdf).pack(
            side=tk.RIGHT
        )

        # Wordlist
        wordlist_frame = ttk.LabelFrame(main_frame, text="Wordlist", padding="10")
        wordlist_frame.pack(fill=tk.X, pady=5)

        wordlist_entry_frame = ttk.Frame(wordlist_frame)
        wordlist_entry_frame.pack(fill=tk.X)

        ttk.Entry(wordlist_entry_frame, textvariable=self.wordlist_path).pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10)
        )
        self.create_green_button(
            wordlist_entry_frame, "Selecionar", self.select_wordlist
        ).pack(side=tk.RIGHT)

        # Progresso
        progress_frame = ttk.LabelFrame(main_frame, text="Progresso", padding="10")
        progress_frame.pack(fill=tk.X, pady=15)

        self.progress_bar = ttk.Progressbar(
            progress_frame, mode="determinate", variable=self.progress_var
        )
        self.progress_bar.pack(fill=tk.X, pady=(0, 5))

        # Status Separado em duas linhas
        self.status_label = ttk.Label(
            progress_frame, textvariable=self.status_var, justify="center"
        )
        self.status_label.pack()

        # Frame para "Testando:"
        self.testing_frame = ttk.Frame(progress_frame)

        # Label fixo "Testando:"
        ttk.Label(self.testing_frame, text="Testando:", font=("Arial", 9)).pack(
            side=tk.LEFT
        )

        # Label só para a senha (com fonte monospace)
        self.testing_var = tk.StringVar(value="")
        self.testing_label = ttk.Label(
            self.testing_frame,
            textvariable=self.testing_var,
            font=("Courier New", 9),
            width=20,
        )
        self.testing_label.pack(side=tk.LEFT, padx=(5, 0))

        # Botao Iniciar
        self.start_button = self.create_green_button(
            main_frame, "Iniciar Crack", self.start_crack
        )
        self.start_button.pack(pady=20)
        self.start_button.config(font=("Arial", 12, "bold"), padx=30, pady=10, width=20)

    def select_pdf(self):
        filename = filedialog.askopenfilename(
            title="Selecionar PDF", filetypes=[("PDF files", "*.pdf")]
        )
        if filename:
            self.pdf_path.set(filename)

    def select_wordlist(self):
        filename = filedialog.askopenfilename(
            title="Selecionar Wordlist", filetypes=[("Text files", "*.txt")]
        )
        if filename:
            self.wordlist_path.set(filename)

    def start_crack(self):
        if not Path(self.pdf_path.get()).exists():
            messagebox.showerror("Erro", "Arquivo PDF não encontrado")
            return
        if not Path(self.wordlist_path.get()).exists():
            messagebox.showerror("Erro", "Wordlist não encontrada")
            return

        self.start_button.config(state="disabled", text="Processando...")
        self.progress_var.set(0)

        # MOSTRAR o frame "Testando:" quando iniciar
        self.testing_frame.pack()

        threading.Thread(target=self.crack_pdf_password, daemon=True).start()

    def crack_pdf_password(self):
        word_list = Path(self.wordlist_path.get())
        pdf_file_path = Path(self.pdf_path.get())

        try:
            # Contar palavras
            self.root.after(0, lambda: self.status_var.set("Contando palavras..."))
            with open(word_list, "rb") as f:
                n_words = sum(1 for _ in f)

            self.root.after(
                0, lambda: self.status_var.set(f"Total de senhas: {n_words:,}")
            )

            # Testar senhas
            with open(word_list, "rb") as wordlist:
                for i, word in enumerate(wordlist, 1):
                    password = word.strip().decode(errors="ignore")
                    progress = (i / n_words) * 100

                    # Progresso
                    self.root.after(0, lambda p=progress: self.progress_var.set(p))
                    self.root.after(
                        0,
                        lambda count=i, total=n_words, pct=progress: self.status_var.set(
                            f"{count:,}/{total:,} testados, {pct:.1f}% completo"
                        ),
                    )

                    # Senha sendo testada
                    self.root.after(
                        0, lambda pwd=password: self.testing_var.set(f"{pwd:<20}")
                    )

                    try:
                        with pikepdf.open(pdf_file_path, password=password):
                            self.root.after(
                                0, lambda p=password: self.password_found(p)
                            )
                            return
                    except pikepdf.PasswordError:
                        continue

            self.root.after(0, self.password_not_found)

        except Exception as e:
            self.root.after(0, lambda: self.show_error(str(e)))

    def password_found(self, password):
        self.status_var.set(f"Senha encontrada: {password}")
        self.start_button.config(state="normal", text="Iniciar Crack")

        # Esconder o frame "Testando:" quando terminar
        self.testing_frame.pack_forget()

        messagebox.showinfo("Sucesso!", f"Senha encontrada: {password}")

    def password_not_found(self):
        self.status_var.set("Senha não encontrada")
        self.start_button.config(state="normal", text="Iniciar Crack")

        # Esconder o frame "Testando:" quando terminar
        self.testing_frame.pack_forget()

        messagebox.showwarning(
            "Resultado", "Senha não encontrada. Tente outra wordlist."
        )

    def show_error(self, error_msg):
        self.status_var.set("Erro durante o processamento")
        self.start_button.config(state="normal", text="Iniciar Crack")

        # Esconder o frame "Testando:" em caso de erro
        self.testing_frame.pack_forget()

        messagebox.showerror("Erro", f"Erro: {error_msg}")


def main():
    root = tk.Tk()
    app = PDFCrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# pip install pikepdf
