import tkinter as tk
import tkinter.filedialog as tk_dailog

ABOUT_THIS_APP = """
I'm Md Mahi Kaishar.
I'm a begineer coder.
This text editor only for txt file.
I think all of you like my program.
Try to stay with me.
"""
FILE_TYPES = (("All Files", "*"), ("Text File", "*.txt"), ("XML File", "*.xml"))

class Text_Editor():
    def __init__(self, app):
        self.app = app
        self.base_font = "Courier New" #"Copperplate Gothic Bold"
        self.file_path = None

        self.ui()

    def ui(self):
        self.ui_app()
        self.ui_header()
        self.ui_menubar()
        self.ui_main()
        self.ui_statusbar()

    def ui_app(self):
        self.app.title("Basic Text Editor 2020")
        self.app.geometry("600x700+300+5")
        self.app.resizable=True
    
    def ui_header(self):
        title_lbl = tk.Label(self.app, text="Text Editor", font=(self.base_font, '12'),width=16)
        title_lbl.place(x=217, y=0)
    
    def ui_menubar(self):
        open_btn = tk.Button(self.app, text="Open", width=16, bg='black', fg='white', borderwidth=0, command=self.open_file)
        open_btn.place(x=000, y=20)

        new_btn = tk.Button(self.app, text="New", width=16, bg='black', fg='white', borderwidth=0, command=self.make_new_file)
        new_btn.place(x=120, y=20)

        save_btn = tk.Button(self.app, text="Save", width=16, bg='black', fg='white', borderwidth=0, command=self.save_file)
        save_btn.place(x=240, y=20)

        save_as_btn = tk.Button(self.app, text="Save As", width=16, bg='black', fg='white', borderwidth=0, command=self.save_as_file)
        save_as_btn.place(x=360, y=20)

        about_btn = tk.Button(self.app, text="About", width=16, bg='black', fg='white', borderwidth=0, command=self.about)
        about_btn.place(x=480, y=20)

    def ui_main(self): 
        self.content_view = tk.Text(self.app, width=73, height=55)
        self.content_view.place(x=5, y=48)

    def ui_statusbar(self):
        self.status_view = tk.Label(self.app, text="GOOD")
        self.status_view.place(x=0, y=932)

        copyright_lbl = tk.Label(self.app, text="©MahiKaishar2020 ",width=16)
        copyright_lbl.place(x=490, y=932)

    def open_file(self):
        self.file_path = tk_dailog.askopenfilename(title="Open", filetypes=FILE_TYPES)

        try:
            with open(self.file_path, 'r') as file_obj:
                file_contents = file_obj.read()
                
                self.content_view.delete(0.1, tk.END)
                self.content_view.insert(0.1, str(file_contents))

        except Exception as Error:
            self.status_view["text"] = f"Error: {Error}"
    
    def make_new_file(self):
        self.content_view.delete(0.1, tk.END)   

    def save_file(self):
        if self.file_path == None:
            return
        
        try:
            with open(self.file_path, 'w') as file_obj:
                current_text_content = self.content_view.get(0.1, tk.END)
                file_obj.write(str(current_text_content))
        except Exception as Error:
            self.status_view["text"] = f"Error: {Error}"

    def save_as_file(self):
        self.file_path = tk_dailog.asksaveasfilename(title="Save As", filetypes=FILE_TYPES)

        try:
            with open(self.file_path, 'w') as file_obj:
                current_text_content = self.content_view.get(0.1, tk.END)
                file_obj.write(str(current_text_content))
        except Exception as Error:
            self.status_view["text"] = f"Error: {Error}"

    def about(self):
        self.content_view.delete(0.1, tk.END)
        self.content_view.insert(0.1, str(ABOUT_THIS_APP))

if __name__ == "__main__":
    app = tk.Tk()
    Text_Editor(app)
    app.mainloop()