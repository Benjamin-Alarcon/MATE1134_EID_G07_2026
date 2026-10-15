"""Escena: EscenaConceptos"""
from manim import *
from ajustes import INTEGRANTE_1
from base_video import txt, W


class EscenaConceptos:
    def conceptos_basicos(self):
        self.seccion("Conceptos: cantidad, tasa y cambio acumulado", INTEGRANTE_1)
        titulo = txt("Tres ideas que no hay que confundir", 40, YELLOW).to_edge(UP)
        self.play(W(titulo))

        filas = [
            ("Cantidad", r"Q(t)", "cuánto hay en el instante t (por ejemplo, litros de agua)"),
            ("Tasa de cambio", r"r(t) = Q'(t)", "qué tan rápido cambia la cantidad (litros por segundo)"),
            ("Cambio acumulado", r"Q(b) - Q(a)", "cuánto cambió la cantidad entre dos instantes a y b (litros)"),
        ]
        bloques = VGroup()
        for nombre, formula, significado in filas:
            cabecera = VGroup(txt(nombre, 34, YELLOW), MathTex(formula)).arrange(RIGHT, buff=0.7)
            bloque = VGroup(cabecera, txt(significado, 28)).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            bloques.add(bloque)
        bloques.arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        bloques.next_to(titulo, DOWN, buff=0.8).to_edge(LEFT, buff=1.0)

        for bloque in bloques:
            self.play(FadeIn(bloque, shift=RIGHT * 0.3))
            self.wait(3)

        aviso = txt("OJO: el cambio acumulado Q(b) - Q(a) NO es la cantidad final Q(b)", 32, RED)
        aviso.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(aviso))
        self.wait(3)
        self.limpiar()
