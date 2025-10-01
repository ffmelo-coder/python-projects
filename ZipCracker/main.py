import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from zipfile import ZipFile, BadZipFile
from tqdm import tqdm
import threading


class ZipCrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ZIP Password Cracker")
        self.root.geometry("600x400")

        # Variables
        self.wordlist_path = tk.StringVar()
        self.zipfile_path = tk.StringVar()
        self.cracking = False
        self.paused = False

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
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Titulo
        ttk.Label(
            main_frame, text="ZIP Password Cracker", font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Wordlist
        ttk.Label(main_frame, text="Arquivo Wordlist:").grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        ttk.Entry(main_frame, textvariable=self.wordlist_path, width=50).grid(
            row=1, column=1, padx=5, pady=5
        )
        self.create_green_button(main_frame, "Browse", self.browse_wordlist).grid(
            row=1, column=2, padx=5, pady=5
        )

        # ZIP
        ttk.Label(main_frame, text="Arquivo ZIP:").grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        ttk.Entry(main_frame, textvariable=self.zipfile_path, width=50).grid(
            row=2, column=1, padx=5, pady=5
        )
        self.create_green_button(main_frame, "Browse", self.browse_zipfile).grid(
            row=2, column=2, padx=5, pady=5
        )

        # Progress bar
        ttk.Label(main_frame, text="Progresso:").grid(
            row=3, column=0, sticky=tk.W, pady=5
        )

        # Frame para progress bar e porcentagem
        progress_frame = ttk.Frame(main_frame)
        progress_frame.grid(
            row=3, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=5
        )
        progress_frame.columnconfigure(0, weight=1)

        self.progress = ttk.Progressbar(progress_frame, mode="determinate")
        self.progress.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))

        # Porcentagem
        self.percentage_label = ttk.Label(progress_frame, text="0%", width=6)
        self.percentage_label.grid(row=0, column=1)

        # Status
        self.status_label = ttk.Label(main_frame, text="Pronto para crackear...")
        self.status_label.grid(row=4, column=0, columnspan=3, pady=5)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=3, pady=10)

        self.crack_button = self.create_green_button(
            button_frame, "Iniciar Cracking", self.start_cracking
        )
        self.crack_button.pack(side=tk.LEFT, padx=5)
        self.crack_button.config(font=("Arial", 12, "bold"), padx=30, pady=10, width=20)

        self.stop_button = self.create_green_button(
            button_frame, "Pausar", self.toggle_pause
        )
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.stop_button.config(state=tk.DISABLED)

        # Resultados text area
        ttk.Label(main_frame, text="Resultados:").grid(
            row=6, column=0, sticky=tk.W, pady=(10, 5)
        )

        text_frame = ttk.Frame(main_frame)
        text_frame.grid(
            row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5
        )

        self.result_text = tk.Text(text_frame, height=10, width=70)
        scrollbar = ttk.Scrollbar(
            text_frame, orient=tk.VERTICAL, command=self.result_text.yview
        )
        self.result_text.configure(yscrollcommand=scrollbar.set)

        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(7, weight=1)

    def update_progress(self, current, total):
        self.progress["value"] = current
        percentage = (current / total) * 100 if total > 0 else 0
        self.percentage_label.config(text=f"{percentage:.1f}%")

    def browse_wordlist(self):
        filename = filedialog.askopenfilename(
            title="Selecionar arquivo de Wordlist",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if filename:
            self.wordlist_path.set(filename)

    def browse_zipfile(self):
        filename = filedialog.askopenfilename(
            title="Selecionar arquivo ZIP",
            filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")],
        )
        if filename:
            self.zipfile_path.set(filename)

    def log_message(self, message):
        self.result_text.insert(tk.END, message + "\n")
        self.result_text.see(tk.END)
        self.root.update_idletasks()

    def start_cracking(self):
        if not self.wordlist_path.get() or not self.zipfile_path.get():
            messagebox.showerror(
                "Error", "Por favor, selecione tanto a wordlist quanto o arquivo ZIP!"
            )
            return

        if not Path(self.wordlist_path.get()).exists():
            messagebox.showerror("Error", "Wordlist não encontrada!")
            return

        if not Path(self.zipfile_path.get()).exists():
            messagebox.showerror("Error", "Arquivo ZIP não encontrado!")
            return

        self.cracking = True
        self.paused = False
        self.crack_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL, text="Pausar")
        self.result_text.delete(1.0, tk.END)

        # Reset progress
        self.progress["value"] = 0
        self.percentage_label.config(text="0%")

        thread = threading.Thread(target=self.crack_password)
        thread.daemon = True
        thread.start()

    def stop_cracking(self):
        self.cracking = False
        self.crack_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Cracking parado pelo usuário.")

    def toggle_pause(self):
        if self.paused:
            # Voltar
            self.paused = False
            self.stop_button.config(text="Pausar")
            self.status_label.config(text="Continuando...")
            self.log_message("[->] Cracking retomado pelo usuário")
        else:
            # Pausar
            self.paused = True
            self.stop_button.config(text="Voltar")
            self.status_label.config(text="Pausado - Clique em Voltar para continuar")
            self.log_message("[||] Cracking pausado pelo usuário")

    def crack_password(self):
        try:
            word_list = Path(self.wordlist_path.get())
            zip_file_path = Path(self.zipfile_path.get())

            zip_file = ZipFile(zip_file_path)

            with open(word_list, "rb") as f:
                n_words = sum(1 for _ in f)

            self.log_message(f"[+] Total de senhas para testar: {n_words:,}")
            self.progress["maximum"] = n_words

            password_found = False

            with open(word_list, "rb") as wordlist:
                for i, word in enumerate(wordlist):
                    if not self.cracking:
                        break

                    # Wait while paused
                    while self.paused and self.cracking:
                        import time

                        time.sleep(0.1)
                        if not self.cracking:
                            break

                    if not self.cracking:
                        break

                    try:
                        zip_file.extractall(pwd=word.strip())
                        password_found = True
                        password = word.decode().strip()
                        self.log_message(f"\n[+] SENHA ENCONTRADA: {password}")
                        self.status_label.config(text=f"Senha encontrada: {password}")
                        self.update_progress(n_words, n_words)
                        messagebox.showinfo("Sucesso!", f"Senha encontrada: {password}")
                        break

                    except (BadZipFile, RuntimeError):
                        pass

                    # Update progress
                    if i % 100 == 0:
                        self.update_progress(i, n_words)
                        if not self.paused:
                            self.status_label.config(
                                text=f"Testando senha {i+1}/{n_words}"
                            )
                        self.root.update_idletasks()

            if not password_found and self.cracking:
                self.log_message("\n[!] Senha não encontrada. Tente outra wordlist.")
                self.status_label.config(text="Senha não encontrada")
                self.update_progress(n_words, n_words)
                messagebox.showinfo(
                    "Completo", "Senha não encontrada. Tente outra wordlist."
                )

        except Exception as e:
            self.log_message(f"[!] Error: {str(e)}")
            messagebox.showerror("Error", f"Ocorreu um erro: {str(e)}")

        finally:
            self.cracking = False
            self.paused = False
            self.crack_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED, text="Pausar")


def main():
    root = tk.Tk()
    app = ZipCrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# pip install tqdm
