"""Escena: EscenaPresentacion."""
from manim import *
from ajustes import INTEGRANTE_1, INTEGRANTE_2, INTEGRANTE_3, CURSO, GRUPO
from base_video import txt, W


class EscenaPresentacion:
    def presentacion(self):
        self.seccion("Presentación", INTEGRANTE_1)
        titulo = txt("Cambio acumulado versus cantidad final", 44, YELLOW)
        titulo.shift(UP * 2.4)
        curso = txt(f"{CURSO}   |   {GRUPO}", 28, GRAY_B).next_to(titulo, DOWN, buff=0.4)
        integrantes = txt(
            f"{INTEGRANTE_1}   -   {INTEGRANTE_2}   -   {INTEGRANTE_3}", 28
        ).next_to(curso, DOWN, buff=0.3)

        pregunta = VGroup(
            txt("Pregunta central", 30, YELLOW),
            txt("¿Por qué integrar una tasa de cambio", 36),
            txt("no entrega necesariamente la cantidad final?", 36),
        ).arrange(DOWN, buff=0.3)
        pregunta.shift(DOWN * 1.3)

        self.play(W(titulo, 1.5))
        self.play(FadeIn(curso), FadeIn(integrantes))
        self.wait(2.5)
        self.play(FadeIn(pregunta))
        self.wait(5)
        self.limpiar()
