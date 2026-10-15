"""Escena: EscenaCreditos."""
from manim import *
from ajustes import FUENTES, RECURSOS, DECLARACION_IA
from base_video import txt, W


class EscenaCreditos:
    def creditos(self):
        self.seccion("Créditos: fuentes y recursos")
        titulo = txt("Fuentes consultadas", 40, YELLOW).to_edge(UP)
        fuentes = VGroup(*[txt(f, 24, ancho=12) for f in FUENTES])
        fuentes.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        fuentes.next_to(titulo, DOWN, buff=0.6)
        self.play(W(titulo))
        self.play(FadeIn(fuentes))
        self.wait(8)
        self.limpiar()

        titulo2 = txt("Recursos y declaración de IA", 40, YELLOW).to_edge(UP)
        recursos = VGroup(*[txt(r, 24, ancho=12) for r in RECURSOS])
        recursos.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ia = VGroup(*[txt(d, 24, ancho=12) for d in DECLARACION_IA])
        ia.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        bloque = VGroup(recursos, ia).arrange(DOWN, aligned_edge=LEFT, buff=0.8)
        bloque.next_to(titulo2, DOWN, buff=0.6)
        self.play(W(titulo2))
        self.play(FadeIn(bloque))
        self.wait(8)
        self.play(FadeOut(titulo2), FadeOut(bloque))
