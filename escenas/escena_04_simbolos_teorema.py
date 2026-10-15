"""Escena: EscenaSimbolosTeorema"""
from manim import *
from ajustes import INTEGRANTE_1
from base_video import txt, W


class EscenaSimbolosTeorema:
    def simbolos_y_teorema(self):
        self.seccion("Símbolos y Teorema Fundamental del Cálculo", INTEGRANTE_1)
        titulo = txt("Símbolos de la integral", 40, YELLOW).to_edge(UP)
        self.play(W(titulo))
        filas = [
            (r"\int", "Integral: suma de infinitos pedacitos"),
            (r"a,\ b", "Límites: dónde empieza y dónde termina el intervalo"),
            (r"f(x)", "Integrando: la función (aquí, la tasa de cambio)"),
            (r"dx", "Ancho de un pedacito muy pequeño; x es la variable"),
            (r"\sum", "Suma de todos los rectángulos"),
            (r"\Delta x", "Delta x: Ancho de cada pedazo: (b - a) / n"),
        ]
        for i, (simbolo, significado) in enumerate(filas):
            y = 2.0 - 0.8 * i
            s = MathTex(simbolo, color=YELLOW).move_to([-5, y, 0])
            t = txt(significado, 26).move_to([-3.6, y, 0], aligned_edge=LEFT)
            self.play(W(s, 1), FadeIn(t, shift=RIGHT * 0.3))
            self.wait(1)
        self.wait(1)
        self.limpiar()

        self.bloque_texto(
            "Teorema Fundamental del Cálculo",
            [
                "Une dos ideas: derivar e integrar.",
                "Si f(x) es continua en [a, b] y F'(x) = f(x),",
                "la integral de f(x) se calcula con una resta:",
            ],
            MathTex(r"\int_a^b f(x)\,dx = F(b) - F(a)"),
            pausa=5,
        )
