import tkinter as tk
from victoryWindow import SmallerWindow
from PIL import Image, ImageTk
from VeliavosDB import *
from io import BytesIO
from random import choice, sample, shuffle


class MainWindow:
    def __init__(self, root, title, width, height, resizable=True, icon=None):

        """ Apsibreziam visus lango parametrus/kintamuosius, ivardintus __init__ skliaustuose."""
        self.root = root
        self.title = title
        self.width = width
        self.height = height
        self.resizable = resizable
        self.icon = icon
        self.countries = []
        self.current_country = None
        self.flag_images = {}
        self.gyvybes = 3
        self.taskai = 0
        """ Apsibreziam visus lango parametrus/kintamuosius, ivardintus __init__ skliaustuose."""

        """ Naudojam issaugotus klases kintamuosius .root objekto metoduose """
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")

        if not self.resizable:
            self.root.resizable(False, False)

        if self.icon:
            self.root.iconbitmap(self.icon)
        """ Naudojam issaugotus klases kintamuosius .root objekto metoduose """

        self.widget_frame = tk.Frame(self.root)   # sukuriam FRAME

        """ Widgetai """
        self.background = tk.PhotoImage(file='Images/Earth.png')
        self.background_label = tk.Label(self.widget_frame, image=self.background)

        self.country_flag_label = tk.Label(self.widget_frame, bd=0)

        self.choice_var = tk.StringVar(value='')
        self.option1 = tk.Radiobutton(self.widget_frame, variable=self.choice_var, value="Option 1", padx=10)
        self.option2 = tk.Radiobutton(self.widget_frame, variable=self.choice_var, value="Option 2", padx=10)
        self.option3 = tk.Radiobutton(self.widget_frame, variable=self.choice_var, value="Option 3", padx=10)

        self.button = tk.Button(self.widget_frame, text="Patvirtinti pasirinkimą", font=('Helvetica', 10), command=self.show_choice, height=2, width=20)
        self.label = tk.Label(self.widget_frame, text='Kokios šalies ši vėliava?', bg='white', wraplength=200, font=('Helvetica', 15), height=3, width=14)

        self.gyvybes_button = tk.Label(self.widget_frame, text=f"Gyvybės: {self.gyvybes}", font=('Helvetica', 10), height=1, width=11)
        self.taskai_button = tk.Label(self.widget_frame, text=f"Taškai: {self.taskai} ", font=('Helvetica', 10), height=1, width=11)
        """ Widgetai """

    def draw_widgets(self):
        frame = self.widget_frame
        frame.pack(ipadx=300, ipady=150)

        self.label.grid(row=0, column=0, padx=100, pady=10)
        self.background_label.place(relwidth=1, relheight=1)
        self.country_flag_label.grid(row=0, column=1, padx=0, pady=50)
        self.button.grid(row=3, column=0, columnspan=2, sticky='w', padx=170, pady=10)
        self.gyvybes_button.grid(row=3, column=3, columnspan=1, sticky='w', padx=0, pady=10)
        self.taskai_button.grid(row=4, column=3, columnspan=1, sticky='w', padx=0, pady=0)
        self.option1.grid(row=2, column=1, sticky='w', padx=10, pady=5)
        self.option2.grid(row=3, column=1, sticky='w', padx=10, pady=5)
        self.option3.grid(row=4, column=1, sticky='w', padx=10, pady=5)


    # sitas metodas bus aktyvuojamas, kai paspaudziamas mygtukas, kuris patvirtina pasirinkta atsakyma
    def show_choice(self):
        chosen_option_value = self.choice_var.get()
        if chosen_option_value:
            chosen_option_text = ""
            if chosen_option_value == "Option 1":
                chosen_option_text = self.option1.cget("text")
            elif chosen_option_value == "Option 2":
                chosen_option_text = self.option2.cget("text")
            elif chosen_option_value == "Option 3":
                chosen_option_text = self.option3.cget("text")
            if chosen_option_text == self.current_country[0]:
                print('TEISINGAI!')
                self.taskai += 1
                self.update_taskai_button()
                self.show_new_question()                # kvieciame funkcija, kad rodytu kita klausima, nes sitas jau atsakytas.
            else:
                self.open_wrong_answer_window()         # jei atsakymas neteisingas, naujo klausimo nekvieciame, ir ismetame lentele su X.
                print('NETEISINGAI! -1 gyvybė.')
                self.gyvybes -= 1
                self.update_gyvybes_button()
                if self.gyvybes == 0:
                    self.open_game_over_window()
        else:
            print("Nieko nepasirinkote.")

    def update_taskai_button(self):
        if hasattr(self, 'taskai_button'):
            self.taskai_button.config(text=f"Taškai: {self.taskai}")

    def update_gyvybes_button(self):
        if hasattr(self, 'gyvybes_button'):
            self.gyvybes_button.config(text=f"Gyvybės: {self.gyvybes}")

    def show_new_question(self):
        # Generate a new question
        self.current_country = choice(self.countries)
        correct_country_name = self.current_country[0]
        random_country_names = [country[0] for country in self.countries if
                                country[0] != correct_country_name]
        random_options = [correct_country_name] + sample(random_country_names, k=2)

        # Shuffle the options randomly
        shuffle(random_options)

        # Update the Radiobutton options
        self.option1.config(text=random_options[0])
        self.option2.config(text=random_options[1])
        self.option3.config(text=random_options[2])

        # Display the flag image on the country_flag_label
        flag_image = self.current_country[1]

        # Resize the flag image to 300x150 using the PIL Image class
        resized_flag_image = flag_image.resize((300, 150))

        # Convert the resized image to PhotoImage
        flag_tk = ImageTk.PhotoImage(resized_flag_image)

        # Check if the ImageTk.PhotoImage is already in self.flag_images
        if correct_country_name in self.flag_images:
            self.flag_images[correct_country_name] = flag_tk
        else:
            self.flag_images[correct_country_name] = flag_tk

        self.country_flag_label.config(image=flag_tk)
        self.country_flag_label.image = flag_tk

    def open_game_over_window(self):
        game_over_window = SmallerWindow(self.root, title="GAME OVER", width=250, height=200, text=f'GAME OVER\n Jūsų rezultatas:{self.taskai}', game_over=True, main_window_instance=self)

    def open_wrong_answer_window(self):
        wrong_answer_window = SmallerWindow(parent=self.root, title="-1 LIFE", width=220, height=150, bg_image='Images/red_X.png', icon='Images/sad.ico')

    def close_program(self):
        self.root.destroy()
        self.root.quit()

    def restart_program(self):
        # Reset variables and widget states here

        self.gyvybes = 3
        self.taskai = 0
        self.update_taskai_button()
        self.update_gyvybes_button()
        self.show_new_question()



# run() funkcija, kurioje nurodome kokia eiles tvarka vyksta programa.
    def run(self):
        self.draw_widgets()             # 1. sustatom pradinius mygtukus ir layouta visa.
        self.show_new_question()        # 2. generuojame ir rodome nauja klausima.
        self.root.mainloop()            # 3. paleidziama pagrindini loop, kur jau leidziama vartotojui daryti dalykus.

def main():
    """ Sukuriamas tk.Tk() klases objektas, kuris leidzia mums naudoti metodus kaip .geometry, .resizable ir pan.
        Tuos veiksmus atliekame automatiskai, sukure MainWindow klases objekta, pavadinimu 'app'.
        Ir galiausiai paleidziame run() metoda ant app objekto."""

    root = tk.Tk()
    app = MainWindow(root, "Vėliavos", 800, 400, resizable=False, icon='Images/Globe.ico')   # sukuria Pagrindini programos langa.

    """Viskas vienoje eiluteje atrodytu taip: * MainWindow(tk.Tk(), "Main Window", 500, 400).run() *
        Isskirstome veiksmus, del aiskumo."""

    conn = connect_database('veliavosDB.db')                                                # prisijungiame duomenu baze
    countries_and_flags = fetch_countries_and_flags(conn)                                   # istraukiame veliavu ir saliu info is duomenu bazes ir priskiriame kintamajam 'countries_and_flags'

    for country_name, flag_blob in countries_and_flags:
        flag_image = Image.open(BytesIO(flag_blob))
        app.countries.append((country_name, flag_image))

    conn.close()                                                                            # iskart uzdarome duomenu baze
    app.run()                                                                               # paleidziame programa


if __name__ == "__main__":                      # leidzia aktyvuoti main() tiktai, jei paleidziama programa is sio failo, ne kaip modulis.
    main()

