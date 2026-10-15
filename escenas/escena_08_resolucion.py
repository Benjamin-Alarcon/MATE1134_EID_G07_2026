"""Escena: EscenaResolucion.

Responsable: Benito Carbonell."""
from manim import *
from ajustes import INTEGRANTE_3
from base_video import txt, W


class EscenaResolucion:
    def resolucion(self):
        self.seccion("Resolución: cambio acumulado", INTEGRANTE_3)
        titulo = txt("Resolución: cambio acumulado", 40, YELLOW).to_edge(UP)

        ejes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 3, 1],
            x_length=7,
            y_length=3.4,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        ejes.to_edge(LEFT, buff=0.5).shift(DOWN * 0.4)
        etiquetas = ejes.get_axis_labels(
            x_label=r"t\ (\text{s})", y_label=r"r(t)\ (\text{L/s})"
        )
        grafica = ejes.plot(lambda t: 1.5, x_range=[0, 5], color=BLUE)
        rect = ejes.get_riemann_rectangles(
            grafica, x_range=[0, 5], dx=1, input_sample_type="left",
            color=BLUE, fill_opacity=0.6, stroke_width=1.5,
        )
        area = ejes.get_area(grafica, x_range=(0, 5), color=BLUE, opacity=0.5)

        f1 = MathTex(r"\Delta t = \frac{5-0}{5} = 1\ \text{s}").scale(0.7)
        f2 = MathTex(r"1{,}5\ \text{L/s} \times 1\ \text{s} = 1{,}5\ \text{L}").scale(0.7)
        f3 = MathTex(r"S_5 = 5 \times 1{,}5 = 7{,}5\ \text{L}").scale(0.7)
        f4 = MathTex(r"\int_0^5 1{,}5\,dt = 1{,}5 \cdot 5 = 7{,}5\ \text{L}").scale(0.7)
        panel = VGroup(f1, f2, f3, f4).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        panel.to_edge(RIGHT, buff=0.5).shift(UP * 0.6)

        self.play(W(titulo))
        self.play(Create(ejes), W(etiquetas))
        self.wait(1)
        self.play(Create(grafica), run_time=1.5)
        cap = self.leyenda("La tasa r(t) = 1,5 L/s es constante entre t = 0 y t = 5.")
        self.play(FadeIn(cap))
        self.wait(3)

        cap = self.cambiar(
            cap, "Partición: n = 5 rectángulos, cada uno de ancho 1 s.",
            Create(rect), W(f1),
        )
        self.wait(3)
        cap = self.cambiar(cap, "Cada rectángulo es tasa por tiempo: litros que entran.", W(f2))
        self.wait(3)
        cap = self.cambiar(cap, "Suma de Riemann: sumamos el aporte de los 5 rectángulos.", W(f3))
        self.wait(3)
        cap = self.cambiar(
            cap, "En el límite, la suma se convierte en la integral definida.",
            FadeOut(rect), FadeIn(area), W(f4),
        )
        self.wait(3)
        cap = self.cambiar(cap, "Como la tasa es constante, la suma ya es exacta con cualquier n.")
        self.wait(3)

        resultado = MathTex(r"\text{Cambio acumulado} = 7{,}5\ \text{L}", color=YELLOW).scale(0.7)
        resultado.next_to(panel, DOWN, buff=0.5).align_to(panel, LEFT)
        caja = SurroundingRectangle(resultado, color=YELLOW, buff=0.2)
        cap = self.cambiar(cap, "Resultado: el estanque ganó 7,5 L entre t = 0 y t = 5.", W(resultado), Create(caja))
        self.wait(3.5)
        self.limpiar()
