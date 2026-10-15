"""Escena: EscenaProblema."""
from manim import *
from ajustes import INTEGRANTE_3
from base_video import txt, W


class EscenaProblema:
    def problema(self):
        self.seccion("El ejemplo", INTEGRANTE_3)
        titulo = txt("Ejemplo: el problema", 40, YELLOW).to_edge(UP)

        lineas = VGroup(
            txt("Estanque con capacidad total de 30 L", 30),
            txt("Cantidad inicial de agua: 20 L", 30),
            txt("Una manguera echa 3 L cada 2 segundos", 30),
            txt("¿Cuál es el cambio acumulado hasta t = 5 s?", 30, YELLOW),
            txt("¿Cuál es la cantidad final de agua?", 30, YELLOW),
        )
        lineas.arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        lineas.to_edge(LEFT, buff=0.7).shift(DOWN * 0.3)

        estanque = Rectangle(width=2.2, height=3.6, color=WHITE)
        estanque.shift(RIGHT * 4.6 + DOWN * 0.6)
        agua = Rectangle(
            width=2.2, height=3.6 * 20 / 30, stroke_width=0,
            fill_color=BLUE, fill_opacity=0.6,
        )
        agua.move_to(estanque.get_bottom(), aligned_edge=DOWN)
        t_agua = txt("20 L", 28).move_to(agua)
        t_cap = txt("30 L", 26).next_to(estanque.get_corner(UR), RIGHT, buff=0.15)
        manguera = Arrow([2.4, 2.2, 0], [4.6, 1.5, 0], buff=0, color=GRAY_B)
        t_manguera = txt("3 L cada 2 s", 24, GRAY_B).next_to(manguera, UP, buff=0.1)

        self.play(W(titulo))
        self.play(Create(estanque), FadeIn(agua), W(t_agua), W(t_cap))
        self.wait(1)
        for i, linea in enumerate(lineas):
            self.play(FadeIn(linea, shift=RIGHT * 0.3))
            if i == 2:
                self.play(Create(manguera), FadeIn(t_manguera))
            self.wait(2)
        self.wait(2)
        self.limpiar()
