from sys import hash_info

import flet as ft

import database.corso_DAO
from database.corso_DAO import *

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._txt_nome = None
        self._txt_result = None
        self._txt_container = None
        self._corso = None
        self._btn_CercaI = None
        self._txt_cognome = None
        self._txt_matricola = None
        self._btn_iscrivi = None
        self._btn_cercaC = None
        self._btn_cercaS = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)

        #ROW 0
        self._corso=ft.Dropdown(label="corso",width=600, hint_text="Selezionare un corso")
        self._btn_CercaI=ft.ElevatedButton(text="Cerca Iscritti",on_click=self._controller.handleCercaIscritti)

        self.fillCorsi()

        row0=ft.Row([self._corso,self._btn_CercaI],alignment=ft.MainAxisAlignment.CENTER)

        #ROW 1
        self._txt_matricola = ft.TextField(
            label="matricola",
            width=200,
            hint_text="Inserisci la matricola"
        )
        self._txt_nome = ft.TextField(
            label="nome",
            width=300,
            read_only=True
        )
        self._txt_cognome = ft.TextField(
            label="cognome",
            width=300,
            read_only=True
        )
        row1 = ft.Row([self._txt_matricola,self._txt_nome,self._txt_cognome], alignment=ft.MainAxisAlignment.CENTER)

        # ROW 2
        self._btn_cercaS = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handleCercaStudente)
        self._btn_cercaC = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handleCercaCorsi)
        self._btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handleIscrivi)

        row2=ft.Row([self._btn_cercaS,self._btn_cercaC,self._btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)

        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        # Add all the elements
        self._page.add(self._title, row0, row1, row2, self._txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def fillCorsi(self):
        dao = CorsiDAO()  # Create an instance
        corsi = dao.getAllCorsi()  # Call the method
        for i in range(len(corsi)):
            self._corso.options.append(ft.dropdown.Option(key=corsi[i]._codice, text=corsi[i].__str__()))