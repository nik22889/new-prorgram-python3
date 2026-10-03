import customtkinter as ctk
from tkinter import messagebox

#это настройки приложеня

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("blue")

#гланое приложения

class DeliveryApp(ctk.CTk):

    def init(self):
        super().init()

        #окна 
        self.title("Delivery App")
        self.geometry("1100x650")
        self.minsize(900, 550)
        #данные текушего пользоватенля
        self.current_user = None

        #паказывает регистрацию
        self.show_auth()


#очистка экрана после рег

def clear_window(self):

    for widget in self.winfo_children():
        widget.distroy()

#регистрация - вход

def show_auth(self):

    self.clearwindow()

    conteiner = ctk.CTkframe(
        self,
        width=450,
        height=500,
        corner_radius=20
    )

    conteiner.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    title = ctk.CTkLabel(
        conteiner,
        text="Delivery",
        font=("Arial", 32, "bold")
    )

    title.pack(pady=(50, 10))

    #двные email

    self.email_entry = ctk.CTkEntry(
        conteiner,
        width=320,
        height=45,
        placeholder_text="Email"
    )

    self.email_entry.pack(pady=10)

    #пароль 

    self.password_entry = ctk.CTkentry(
        conteiner,
        wight=320,
        height=45,
        placeholder_text="Пароль",
        show="*"
    )

    self.password_entry.pack(pady=10)

    #кнопка для входа

    login_button = ctk.CTkbutton(
        conteiner,
        text='войти',
        wight=320,
        height=45,
        command=self.login
    )

    login_button.pack(pady=(25, 10))


    #регистрация

    register_button = ctk.CTkButton(
        conteiner,
        text="Создать аккаунт",
        height=45,
        fg_color="transparent",
        border_width=1,
        command=self.show_register       
    )

    register_button.pack(pady=10)

    #вход клиента

    def login(self):
        email = self.email_enter.get()
        password = self.password_enter.get()

        if not email or not password:

            messagebox.shorwerror(
                "ошибка",
                "заполняйте все поля"
            )

            return

        #пока временый вход
        self.current_user = {
            "name","клиент",
            "email",email
        }

        self.show_client_panel()


    #регистарация

    def show_register(self):
        self.clear_window()

        conteiner = ctk.CTkFrame(
            self,
            width=450,
            height=550,
            corner_radius=20
        )

        conteiner.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        title = ctk.CTklabel(
            conteiner,
            text = 'создать аккаунт',
            Font=("Arial", 28, "bold")
        )

        title.pack(pady=(45, 25))

        self.name_enter = ctk.CTnenter(
            conteiner,
            width=320,
            height=45,
            placeholder_text="ваше имя: "
        )