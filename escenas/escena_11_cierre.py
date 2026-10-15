"""Escena: EscenaCierre."""
from manim import *
from ajustes import INTEGRANTE_2
from base_video import txt, W


class EscenaCierre:
    def cierre(self):
        self.seccion("Respuesta a la pregunta central y cierre", INTEGRANTE_2)
        titulo = txt("Respuesta a la pregunta central", 40, YELLOW).to_edge(UP)
        lineas = VGroup(
            txt("La integral de la tasa mide el cambio: es una resta, Q(b) - Q(a).", 30),
            txt("La tasa dice cómo cambia la cantidad, pero no con cuánta partió.", 30),
            txt("Por eso hay que sumar la cantidad inicial:", 30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        lineas.next_to(titulo, DOWN, buff=0.6)

        formula = MathTex(r"Q(b) = Q(a) + \int_a^b r(t)\,dt")
        formula.next_to(lineas, DOWN, buff=0.6)
        caja = SurroundingRectangle(formula, color=YELLOW, buff=0.25)

        nota = txt("Solo coinciden cuando la cantidad inicial es 0.", 28)
        nota.next_to(caja, DOWN, buff=0.5)
        ejemplo = txt("En nuestro estanque: cambio acumulado 7,5 L y cantidad final 27,5 L.", 28, GREEN)
        ejemplo.next_to(nota, DOWN, buff=0.3)

        self.play(W(titulo))
        for linea in lineas:
            self.play(FadeIn(linea, shift=RIGHT * 0.3))
            self.wait(2)
        self.play(W(formula, 1.5), Create(caja))
        self.wait(2.5)
        self.play(FadeIn(nota))
        self.wait(2)
        self.play(FadeIn(ejemplo))
        self.wait(3)
        self.limpiar()
        self.poner_voz()

        # Cadena de ideas: conexión final con el concepto de integral
        titulo2 = txt("Conexión con la integral", 40, YELLOW).to_edge(UP)
        pasos = [
            txt("suma de Riemann", 30),
            txt("límite", 30),
            txt("integral definida", 30),
            txt("cambio acumulado", 30, YELLOW),
        ]
        cadena = VGroup()
        for i, paso in enumerate(pasos):
            cadena.add(paso)
            if i < len(pasos) - 1:
                cadena.add(Arrow(LEFT * 0.4, RIGHT * 0.4, buff=0))
        cadena.arrange(RIGHT, buff=0.3)
        if cadena.width > 12.5:
            cadena.scale_to_fit_width(12.5)
        cadena.shift(UP * 0.3)
        final = txt("Cantidad final = cantidad inicial + cambio acumulado", 34, GREEN)
        final.next_to(cadena, DOWN, buff=1.0)
        self.play(W(titulo2))
        self.play(FadeIn(cadena))
        self.wait(3)
        self.play(FadeIn(final))
        self.wait(4.5)
        self.limpiar()
