import tkinter as tk

class SmallerWindow:
    def __init__(self, parent, title, width, height, resizable=False, icon=None):
        """ Apsibreziam visus mazesnio lango parametrus/kintamuosius, ivardintus __init__ skliaustuose."""
        self.smaller_window = tk.Toplevel(parent)
        self.title = title
        self.width = width
        self.height = height
        self.resizable = resizable
        self.icon = icon
        """ Apsibreziam visus mazesnio lango parametrus/kintamuosius, ivardintus __init__ skliaustuose."""

        """ Naudojam issaugotus klases kintamuosius .smaller_window objekto metoduose """
        self.smaller_window.title(self.title)
        self.smaller_window.geometry(f"{self.width}x{self.height}")

        if self.resizable:
            self.smaller_window.resizable(True, True)

        if self.icon:
            self.smaller_window.iconbitmap(self.icon)
        """ Naudojam issaugotus klases kintamuosius .smaller_window objekto metoduose """
        self.background = tk.PhotoImage(file='red_X.png')
        self.background_label = tk.Label(self.smaller_window, image=self.background,background='black')
        self.background_label.place(relwidth=1, relheight=1)

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