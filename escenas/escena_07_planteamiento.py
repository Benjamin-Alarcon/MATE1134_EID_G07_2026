"""Escena: EscenaPlanteamiento.

Responsable: Benito Carbonell."""
from manim import *
from ajustes import INTEGRANTE_3
from base_video import txt, W


class EscenaPlanteamiento:
    def planteamiento(self):
        self.seccion("Planteamiento", INTEGRANTE_3)
        titulo = txt("Planteamiento", 40, YELLOW).to_edge(UP)
        plan = VGroup(
            MathTex(r"\text{Cantidad inicial: } Q(0) = 20\ \text{L}"),
            MathTex(
                r"\text{Tasa de cambio: } r(t) = \frac{3\ \text{L}}{2\ \text{s}} = 1{,}5\ \text{L/s}"
            ),
            MathTex(r"\text{Cambio acumulado: } \int_0^5 r(t)\,dt"),
            MathTex(r"\text{Cantidad final: } Q(5) = Q(0) + \int_0^5 r(t)\,dt"),
        )
        plan.arrange(DOWN, aligned_edge=LEFT, buff=0.7).scale(0.85).shift(DOWN * 0.4)

        self.play(W(titulo))
        for formula in plan:
            self.play(W(formula, 1.5))
            self.wait(2.5)
        self.wait(1)
        self.limpiar()
