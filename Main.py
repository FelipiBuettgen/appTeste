from kivymd.app import MDApp
from kivymd.uix.button import *
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.icon_definitions import md_icons
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import *


class TelaInit(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.theme_cls.theme_style == "Light":
            self.icone = 'moon-waning-crescent'
        else:
            self.icone = 'lightbulb'
        self.name = "inicial"
        self.fl = MDFloatLayout(
            pos_hint={"center_x": 0.5, "center_y": 0.5},

        )
        self.card = MDCard(

            orientation="vertical",
            padding=(20),
            size_hint=(0.9, 0.9),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            elevation=4,
            shadow_radius=6,
            shadow_offset=(0, 2),
            spacing=25,
        )
        self.bt_thema = MDIconButton(
            icon=self.icone,
            on_release=self.switch_theme_style,
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            icon_size="35dp"
        )
        self.bt_back = MDFlatButton(text="Voltar!",
                                    on_release=self.voltar,
                                    pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.fl.add_widget(self.bt_thema)
        self.fl.add_widget(self.bt_back)
        self.card.add_widget(self.fl)
        self.add_widget(self.card)

    def voltar(self, *args):
        self.manager.switch_to(TelaLogin())

    def switch_theme_style(self, *args):
        self.theme_cls.primary_palette = (
            "Green" if self.theme_cls.primary_palette == "Blue" else "Blue"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        self.bt_thema.icon = (
            "moon-waning-crescent" if self.bt_thema.icon ==
            'lightbulb' else 'lightbulb')


class TelaLogin(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.theme_cls.theme_style == "Light":
            self.icone = 'moon-waning-crescent'
        else:
            self.icone = 'lightbulb'
        self.id = 'telaLogin'
        self.name = 'login'
        self.lb_login = MDLabel(
            text="teste",

            halign='center',
            pos_hint={"center_x": 0.5, "center_y": 0.4})
        self.lb_login.id = "lbLogin"
        self.bt_login = MDRectangleFlatIconButton(
            text="Logar",
            icon="login",
            pos_hint={"center_x": 0.5, "center_y": 0.51},
            icon_size="25dp",
            on_press=self.login
        )
        self.bt_login.id = 'bt_login'
        self.txt_senha = MDTextField(
            hint_text="Senha",
            helper_text="Sua senha",
            radius=[0, 0, 15, 15],
            mode="round",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            password=True
        )
        self.txt_senha.id = "textSenha"
        self.txt_user = MDTextField(
            hint_text="Nome",
            helper_text="Nome completo",
            radius=[0, 0, 15, 15],
            mode="round",
            pos_hint={"center_x": 0.5, "center_y": 0.71},
        )
        self.txt_user.id = "textName"
        self.bt_thema = MDIconButton(

            icon=self.icone,
            on_release=self.switch_theme_style,
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            icon_size="35dp"
        )
        self.bt_thema.id = "iconBT"
        self.fl = MDFloatLayout(
            pos_hint={"center_x": 0.5, "center_y": 0.5},

        )
        self.fl.id = "fl1"
        self.card = MDCard(

            orientation="vertical",
            padding=(20),
            size_hint=(0.9, 0.9),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            elevation=4,
            shadow_radius=6,
            shadow_offset=(0, 2),
            spacing=25,
        )
        self.card.id = "card"
        self.fl.add_widget(self.bt_thema)
        self.fl.add_widget(self.txt_user)
        self.fl.add_widget(self.txt_senha)
        self.fl.add_widget(self.bt_login)
        self.fl.add_widget(self.lb_login)
        self.card.add_widget(self.fl)
        self.add_widget(self.card)

    def switch_theme_style(self, *args):
        self.theme_cls.primary_palette = (
            "Green" if self.theme_cls.primary_palette == "Blue" else "Blue"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        self.bt_thema.icon = (
            "moon-waning-crescent" if self.bt_thema.icon ==
            'lightbulb' else 'lightbulb')

    def login(self, *args):
        self.manager.switch_to(TelaInit())


class Example(MDApp):
    def build(self):
        Window.size = (350, 680)
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.sm = MDScreenManager()
        self.sm.transition = MDFadeSlideTransition()
        tela_login = TelaLogin(name='login')
        self.sm.add_widget(tela_login)
        self.sm.current = 'login'
        # Defina a tela de login como a atual
        return self.sm


if __name__ == "__main__":
    app = Example()
    app.run()
