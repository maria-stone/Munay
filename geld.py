import tkinter as tk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Fensta")

        # Label
        self.label = tk.Label(root, text="Gib deinen Betrag ein:")
        self.label.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Button
        self.button = tk.Button(root, text="€", command=self.nacheuro)
        self.button.pack(pady=10)


        self.button = tk.Button(root, text="$", command=self.nachusd)
        self.button.pack(pady=10)

        self.button = tk.Button(root, text="Sprache", command=self.sprache)
        self.button.pack(pady=10)

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def sprache(self):
        if self.label.cget("text") == "Gib deinen Betrag ein:":
            self.label.config(text="Enter Your Ammount:")
        elif self.label.cget("text") == "Enter Your Ammount:":
            self.label.config(text="Gib deinen Betrag ein:")


    def nacheuro(self):
        text=self.entry.get()
        ergebniss = int(text.replace("$", ""))
        self.output_label.config(text=ergebniss*0.85)

    def nachusd(self):
        text=self.entry.get()
        ergebniss = int(text.replace("€", ""))
        self.output_label.config(text=ergebniss * 1.18)

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()

