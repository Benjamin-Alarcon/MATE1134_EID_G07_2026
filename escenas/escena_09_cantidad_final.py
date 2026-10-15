"""Escena: EscenaCantidadFinal."""
from manim import *
from ajustes import INTEGRANTE_2
from base_video import txt, W


class EscenaCantidadFinal:
    def cantidad_final(self):
        self.seccion("Cantidad final: Q(t)", INTEGRANTE_2)
        titulo = txt("Cantidad final = cantidad inicial + cambio acumulado", 36, YELLOW).to_edge(UP)

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
        grafica = ejes.plot(lambda t: 20 + 1.5 * t, x_range=[0, 5], color=BLUE)
        capacidad = DashedLine(ejes.c2p(0, 30), ejes.c2p(6, 30), color=RED)
        t_capacidad = txt("Capacidad: 30 L", 22, RED).move_to(ejes.c2p(3, 30)).shift(UP * 0.3)
        ref = DashedLine(ejes.c2p(0, 20), ejes.c2p(5, 20), color=GRAY_B)
        punto0 = Dot(ejes.c2p(0, 20), color=GREEN)
        punto5 = Dot(ejes.c2p(5, 27.5), color=YELLOW)
        flecha = DoubleArrow(ejes.c2p(5, 20), ejes.c2p(5, 27.5), buff=0, color=YELLOW)

        p1 = MathTex(r"Q(t) = 20 + 1{,}5\,t").scale(0.7)
        p2 = MathTex(r"Q(0) = 20\ \text{L (inicial)}", color=GREEN).scale(0.7)
        p3 = MathTex(r"\int_0^5 r(t)\,dt = 7{,}5\ \text{L}", color=YELLOW).scale(0.7)
        p4 = MathTex(r"Q(5) = 20 + 7{,}5 = 27{,}5\ \text{L}", color=YELLOW).scale(0.7)
        p5 = txt("27,5 L < 30 L: no se desborda", 24)
        panel = VGroup(p1, p2, p3, p4, p5).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        panel.to_edge(RIGHT, buff=0.4)

        self.play(W(titulo, 1.5))
        self.play(Create(ejes), W(etiquetas))
        self.play(Create(capacidad), FadeIn(t_capacidad))
        self.wait(1)
        cap = self.leyenda("Como Q'(t) = r(t) = 1,5, la cantidad crece en línea recta.")
        self.play(Create(grafica), W(p1), FadeIn(cap))
        self.wait(3)
        cap = self.cambiar(cap, "Partimos de la cantidad inicial: 20 L.", FadeIn(punto0), Create(ref), W(p2))
        self.wait(3)
        cap = self.cambiar(cap, "El cambio acumulado es lo que sube entre t = 0 y t = 5.", Create(flecha), W(p3))
        self.wait(3)
        cap = self.cambiar(cap, "La cantidad final es la inicial más el cambio acumulado.", FadeIn(punto5), W(p4))
        self.wait(3)
        cap = self.cambiar(cap, "Y se respeta la capacidad del estanque.", W(p5))
        self.wait(3.5)
        self.limpiar()
