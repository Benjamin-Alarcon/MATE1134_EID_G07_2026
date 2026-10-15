"""Escena: EscenaComparacion."""
from manim import *
from ajustes import INTEGRANTE_2
from base_video import txt, W


class EscenaComparacion:
    def comparacion(self):
        self.seccion("Misma tasa, distinta cantidad inicial", INTEGRANTE_2)
        titulo = txt("Misma tasa, distinta cantidad final", 38, YELLOW).to_edge(UP)

        ejes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 35, 5],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        ejes.to_edge(LEFT, buff=0.5).shift(DOWN * 0.5)
        etiquetas = ejes.get_axis_labels(
            x_label=r"t\ (\text{s})", y_label=r"Q(t)\ (\text{L})"
        )
        gr_a = ejes.plot(lambda t: 20 + 1.5 * t, x_range=[0, 5], color=BLUE)
        gr_b = ejes.plot(lambda t: 10 + 1.5 * t, x_range=[0, 5], color=ORANGE)
        flecha_a = DoubleArrow(ejes.c2p(5, 20), ejes.c2p(5, 27.5), buff=0, color=YELLOW)
        flecha_b = DoubleArrow(ejes.c2p(5, 10), ejes.c2p(5, 17.5), buff=0, color=YELLOW)
        puntos = VGroup(
            Dot(ejes.c2p(0, 20), color=BLUE), Dot(ejes.c2p(5, 27.5), color=BLUE),
            Dot(ejes.c2p(0, 10), color=ORANGE), Dot(ejes.c2p(5, 17.5), color=ORANGE),
        )

        c1 = MathTex(r"\text{Estanque A: } Q(0) = 20\ \text{L}", color=BLUE).scale(0.7)
        c2 = MathTex(r"\text{Estanque B: } Q(0) = 10\ \text{L}", color=ORANGE).scale(0.7)
        c3 = MathTex(r"\int_0^5 r(t)\,dt = 7{,}5\ \text{L (en ambos)}", color=YELLOW).scale(0.7)
        c4 = MathTex(r"A:\ 20 + 7{,}5 = 27{,}5\ \text{L}", color=BLUE).scale(0.7)
        c5 = MathTex(r"B:\ 10 + 7{,}5 = 17{,}5\ \text{L}", color=ORANGE).scale(0.7)
        panel = VGroup(c1, c2, c3, c4, c5).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        panel.to_edge(RIGHT, buff=0.4)

        self.play(W(titulo, 1.5))
        self.play(Create(ejes), W(etiquetas))
        cap = self.leyenda("Dos estanques con la misma manguera, pero que parten con agua distinta.")
        self.play(Create(gr_a), Create(gr_b), FadeIn(puntos), W(c1), W(c2), FadeIn(cap))
        self.wait(3.5)
        cap = self.cambiar(
            cap, "En los dos, el cambio acumulado es el mismo: 7,5 L.",
            Create(flecha_a), Create(flecha_b), W(c3),
        )
        self.wait(3.5)
        cap = self.cambiar(cap, "Pero las cantidades finales son distintas.", W(c4), W(c5))
        self.wait(3.5)
        cap = self.cambiar(cap, "La tasa r(t) no contiene la cantidad inicial.")
        self.wait(3.5)
        self.limpiar()
