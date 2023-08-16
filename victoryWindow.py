import tkinter as tk


class SmallerWindow:
    def __init__(self, parent, title, width, height, main_window_instance=None, resizable=False, icon=None, text = '', bg_image=None, game_over=False):
        """ Apsibreziam visus mazesnio lango parametrus/kintamuosius, ivardintus __init__ skliaustuose."""
        self.main_window_instance = main_window_instance
        self.smaller_window = tk.Toplevel(parent)
        self.title = title
        self.width = width
        self.height = height
        self.resizable = resizable
        self.icon = icon
        self.text = text
        self.bg_image = bg_image
        """ Apsibreziam visus mazesnio lango parametrus/kintamuosius, ivardintus __init__ skliaustuose."""

        """ Naudojam issaugotus klases kintamuosius .smaller_window objekto metoduose """
        self.smaller_window.title(self.title)
        self.smaller_window.geometry(f"{self.width}x{self.height}")

        if self.resizable:
            self.smaller_window.resizable(True, True)

        if self.icon:
            self.smaller_window.iconbitmap(self.icon)
        """ Naudojam issaugotus klases kintamuosius .smaller_window objekto metoduose """
        if bg_image:
            self.background = tk.PhotoImage(file=bg_image)
            self.background_label = tk.Label(self.smaller_window, image=self.background, background='black')
            self.background_label.place(relwidth=1, relheight=1)
        if game_over:
            self.label = tk.Label(self.smaller_window, text=self.text, font=("Helvetica", 12))
            self.label.pack(anchor='center', expand=True)
            self.button_Close = tk.Button(self.smaller_window, text="Uždaryti", font=('Helvetica', 10), height=2, width=20, command=self.main_window_instance.close_program)
            self.button_Try_again = tk.Button(self.smaller_window, text="Bandyti dar kartą", font=('Helvetica', 10), height=2, width=20, command=self.restart_me)
            self.button_Highscore = tk.Button(self.smaller_window, text="Išsaugoti rezultatą", font=('Helvetica', 10), height=2, width=20)
            self.button_Close.pack(pady=5)
            self.button_Try_again.pack(pady=5)
            self.button_Highscore.pack(pady=5)



        """ Uzrasas mazesniame lange """
        # label = tk.Label(self.smaller_window, text="naujo lango informacija")
        # label.pack()
        """ Uzrasas mazesniame lange """

        self.focus()

        """ focus funkcija 'sufokusuoja' langa"""
    def focus(self):
        self.smaller_window.grab_set()          # neleidzia pasiekti kitu langu, kol esamas langas nebus uzdarytas
        self.smaller_window.focus_set()         # sufokusuoja KLAVIETUROS ivedimus i esama langa
        self.smaller_window.wait_window()       # sustabdo visa programos darba, kol nebus uzdarytas esamas langas

        """ focus funkcija 'sufokusuoja' langa"""

    def restart_me(self):
        if self.main_window_instance:
            self.main_window_instance.restart_program()
        self.smaller_window.destroy()


