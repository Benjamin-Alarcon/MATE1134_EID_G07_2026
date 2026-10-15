"""Escena: EscenaSumasAIntegral"""
from manim import *
from ajustes import INTEGRANTE_1
from base_video import txt, W


class EscenaSumasAIntegral:
    def sumas_a_integral(self):
        self.seccion("De las sumas de Riemann a la integral", INTEGRANTE_1)
        titulo = txt("De las sumas a la integral", 40, YELLOW).to_edge(UP)

        ejes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 4, 1],
            x_length=8,
            y_length=3.5,
            axis_config={"include_numbers": False},
        )
        ejes.shift(DOWN * 0.3)
        etiquetas = ejes.get_axis_labels(x_label="x", y_label="y")

        def f(x):
            return 0.15 * (x - 3) ** 2 + 1.5

        grafica = ejes.plot(f, x_range=[0, 6], color=BLUE)
        etiqueta_f = MathTex("y = f(x)", color=BLUE).scale(0.8)
        etiqueta_f.move_to(ejes.c2p(5.3, 3.4))
        linea_a = DashedLine(ejes.c2p(1, 0), ejes.c2p(1, f(1)))
        linea_b = DashedLine(ejes.c2p(5, 0), ejes.c2p(5, f(5)))
        txt_a = MathTex("a").next_to(ejes.c2p(1, 0), DOWN, buff=0.25)
        txt_b = MathTex("b").next_to(ejes.c2p(5, 0), DOWN, buff=0.25)
        area = ejes.get_area(grafica, x_range=(1, 5), color=BLUE, opacity=0.5)

        self.play(W(titulo))
        self.play(Create(ejes), W(etiquetas))
        self.play(Create(grafica), W(etiqueta_f))
        cap = self.leyenda("f(x) es una función continua (en nuestro tema, la tasa de cambio).")
        self.play(FadeIn(cap))
        self.wait(3)

        cap = self.cambiar(
            cap,
            "a y b marcan el intervalo [a, b] donde queremos acumular.",
            Create(linea_a), Create(linea_b), W(txt_a), W(txt_b),
        )
        self.wait(3)

        cap = self.cambiar(cap, "El área bajo la curva representa lo que se acumula.", FadeIn(area))
        self.wait(3)

        rect4 = ejes.get_riemann_rectangles(
            grafica, x_range=[1, 5], dx=1, input_sample_type="left",
            color=BLUE, fill_opacity=0.6, stroke_width=1,
        )
        formula = MathTex(r"\Delta x = \frac{b-a}{n} = \frac{5-1}{4} = 1").scale(0.8)
        formula.next_to(titulo, DOWN, buff=0.3)
        cap = self.cambiar(
            cap,
            "Partición: dividimos [a, b] en n pedazos del mismo ancho.",
            FadeOut(area), Create(rect4), W(formula),
        )
        self.wait(3)

        puntos = VGroup(*[Dot(ejes.c2p(x, f(x)), color=YELLOW) for x in [1, 2, 3, 4]])
        formula2 = MathTex(r"\text{altura} \times \text{ancho} = f(x_i^*)\,\Delta x").scale(0.8)
        formula2.next_to(titulo, DOWN, buff=0.3)
        cap = self.cambiar(
            cap,
            "Punto muestra: en cada pedazo medimos una altura f(x*).",
            FadeIn(puntos), ReplacementTransform(formula, formula2),
        )
        self.wait(3)

        formula3 = MathTex(r"S_n = \sum_{i=1}^{n} f(x_i^*)\,\Delta x").scale(0.8)
        formula3.next_to(titulo, DOWN, buff=0.3)
        cap = self.cambiar(
            cap,
            "Suma de Riemann: sumamos el área de todos los rectángulos.",
            ReplacementTransform(formula2, formula3),
        )
        self.wait(3)

        rect8 = ejes.get_riemann_rectangles(
            grafica, x_range=[1, 5], dx=0.5, input_sample_type="left",
            color=BLUE, fill_opacity=0.6, stroke_width=0.8,
        )
        rect32 = ejes.get_riemann_rectangles(
            grafica, x_range=[1, 5], dx=0.125, input_sample_type="left",
            color=BLUE, fill_opacity=0.6, stroke_width=0.3,
        )
        cap = self.cambiar(
            cap,
            "Con más pedazos (n = 8) los rectángulos se ajustan mejor a la curva.",
            FadeOut(puntos), ReplacementTransform(rect4, rect8),
        )
        self.wait(2.5)

        formula4 = MathTex(r"n \to \infty \quad \Rightarrow \quad \Delta x \to 0").scale(0.8)
        formula4.next_to(titulo, DOWN, buff=0.3)
        cap = self.cambiar(
            cap,
            "Con n = 32 casi no se nota la diferencia con la curva.",
            ReplacementTransform(rect8, rect32), ReplacementTransform(formula3, formula4),
        )
        self.wait(3)

        formula5 = MathTex(
            r"\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x"
        ).scale(0.8)
        formula5.next_to(titulo, DOWN, buff=0.3)
        cap = self.cambiar(
            cap,
            "Si f es continua en [a, b], las sumas se acercan a un único número.",
            FadeOut(rect32), FadeIn(area), ReplacementTransform(formula4, formula5),
        )
        self.wait(3)

        cap = self.cambiar(cap, "Ese número es la integral definida de f entre a y b.")
        self.wait(3)
        self.limpiar()
