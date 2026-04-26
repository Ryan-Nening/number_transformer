import tkinter
from tkinter import filedialog, font, messagebox

class NumberTransformerGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Number Transformer Pro")
        self.main_window.geometry("500x450")
        self.main_window.configure(bg="#2d3436")

    def build_user_interface(self):
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        normal_font = font.Font(family="Helvetica", size=11)
        
        self.title_label = tkinter.Label(self.main_window, text="⚡ Number Transformer Pro", font=title_font, bg="#2d3436", fg="#00cec9") 
        self.title_label.pack(pady=(20, 10))
        
        self.instruction_label = tkinter.Label(self.main_window, text="Upload an integer file to generate squares and cubes.", font=normal_font, bg="#2d3436", fg="#dfe6e9")
        self.instruction_label.pack(pady=5)
        
        self.process_button = tkinter.Button(self.main_window, text="🚀 Select File & Transform", font=normal_font, bg="#0984e3", fg="#ffffff", activebackground="#74b9ff", activeforeground="#ffffff", relief="flat", cursor="hand2", command=self.process_files)
        self.process_button.pack(pady=15, ipadx=10, ipady=5)

        self.preview_label = tkinter.Label(self.main_window, text="Live Processing Preview:", font=normal_font, bg="#2d3436", fg="#fdcb6e") 
        self.preview_label.pack(pady=(10, 5))
        
        self.preview_box = tkinter.Listbox(self.main_window, width=50, height=8, bg="#1e272e", fg="#ffffff", relief="flat", highlightthickness=0, font=("Courier", 10))
        self.preview_box.pack(pady=5)

    def process_files(self):
        input_file_name = filedialog.askopenfilename(title="Select Numbers File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        
        if input_file_name != "":
            try:
                input_file = open(input_file_name, "r")
                squares_file = open("squares.txt", "w")
                cubes_file = open("cubes.txt", "w")
                
                self.preview_box.delete(0, tkinter.END)