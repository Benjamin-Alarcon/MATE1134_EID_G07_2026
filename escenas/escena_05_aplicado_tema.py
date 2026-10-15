"""Escena: EscenaAplicadoTema"""
from manim import *
from ajustes import INTEGRANTE_1
from base_video import txt, W


class EscenaAplicadoTema:
    def aplicado_a_tema(self):
        etiqueta = Text(f"Voz: {INTEGRANTE_1}", font_size=18, color=GRAY_B)
        etiqueta.to_corner(UR, buff=0.15)
        self.add(etiqueta)

        titulo = txt("Aplicado a nuestro tema", 38, YELLOW).to_edge(UP)
        linea = txt("Como Q'(t) = r(t), en el Teorema: Q(t) hace de F(x) y r(t) hace de f(x):", 32)
        linea.next_to(titulo, DOWN, buff=0.6)

        ecuacion = MathTex(r"\int_a^b r(t)\,dt", "=", r"Q(b) - Q(a)")
        ecuacion[0].set_color(YELLOW)
        ecuacion.scale(1.1).next_to(linea, DOWN, buff=0.7)
        nombre_ecuacion = txt("cambio acumulado", 24, YELLOW)
        nombre_ecuacion.next_to(ecuacion[0], DOWN, buff=0.2)

        def columna(nombre, simbolo, numero, color):
            return VGroup(
                txt(nombre, 24, color),
                MathTex(simbolo, color=color),
                MathTex(numero, color=color),
            ).arrange(DOWN, buff=0.25)

        final = columna("cantidad final", r"Q(b)", r"27{,}5\ \text{L}", BLUE)
        inicial = columna("cantidad inicial", r"Q(a)", r"20\ \text{L}", GREEN)
        cambio = columna("cambio acumulado", r"\int_a^b r(t)\,dt", r"7{,}5\ \text{L}", YELLOW)
        fila = VGroup(final, MathTex("="), inicial, MathTex("+"), cambio)
        fila.arrange(RIGHT, buff=0.5)
        fila.move_to([0, -1.9, 0])

        self.play(W(titulo, 1.0))
        self.play(FadeIn(linea, run_time=0.8))
        self.wait(3.1)
        self.play(FadeIn(ecuacion, run_time=1.0), FadeIn(nombre_ecuacion, run_time=1.0))
        self.wait(4.4)
        self.play(FadeIn(fila, run_time=1.2))
        self.wait(3.2)
        self.limpiar()
