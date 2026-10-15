from manim import *
from ajustes import FACTOR_PAUSA


def txt(texto, size=30, color=WHITE, ancho=12.5):
    """Texto que nunca se sale de la pantalla."""
    t = Text(texto, font_size=size, color=color)
    if t.width > ancho:
        t.scale_to_fit_width(ancho)
    return t


def W(mob, t=1.2):
    """Write con duración fija, para que el tiempo total sea predecible."""
    return Write(mob, run_time=t)


class BaseVideo(Scene):
    def wait(self, duration=1.0, **kwargs):
        super().wait(duration * FACTOR_PAUSA, **kwargs)

    def ahora(self):
        for lectura in (lambda: self.time, lambda: self.renderer.time):
            try:
                return float(lectura())
            except Exception:
                pass
        return 0.0

    def poner_voz(self):
        if getattr(self, "narrador_actual", None):
            etiqueta = Text(f"Voz: {self.narrador_actual}", font_size=18, color=GRAY_B)
            etiqueta.to_corner(UR, buff=0.15)
            self.add(etiqueta)

    def seccion(self, nombre, narrador=None):
        self.marcas.append((self.ahora(), nombre, narrador or "-"))
        self.narrador_actual = narrador
        self.poner_voz()

    def limpiar(self):
        self.play(*[FadeOut(m) for m in self.mobjects])

    def leyenda(self, texto):
        return txt(texto, 28).to_edge(DOWN, buff=0.5)

    def cambiar(self, cap, texto, *extra):
        nueva = self.leyenda(texto)
        self.play(ReplacementTransform(cap, nueva), *extra)
        return nueva

    def bloque_texto(self, nombre, lineas, formula, pausa=6):
        self.poner_voz()
        titulo = txt(nombre, 38, YELLOW).to_edge(UP)
        texto = VGroup(*[txt(l, 30) for l in lineas])
        texto.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        texto.next_to(titulo, DOWN, buff=0.7)
        self.play(W(titulo))
        for linea in texto:
            self.play(FadeIn(linea, shift=RIGHT * 0.3))
            self.wait(1)
        formula.next_to(texto, DOWN, buff=0.8)
        self.play(W(formula, 1.5))
        self.wait(pausa)
        self.limpiar()

    def informe_tiempos(self):
        total = self.ahora()
        lineas = ["MARCAS DE TIEMPO (min:seg) - sirven para sincronizar la voz"]
        for t, nombre, narrador in self.marcas:
            lineas.append(f"{int(t // 60)}:{t % 60:04.1f}  {nombre}  (voz: {narrador})")
        lineas.append(f"DURACION TOTAL: {int(total // 60)}:{total % 60:04.1f}")
        texto = "\n".join(lineas)
        print("\n" + texto + "\n")
        with open("marcas_tiempo.txt", "w", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")
