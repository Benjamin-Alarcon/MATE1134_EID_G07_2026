"""Archivo principal: une todas las escenas en orden. Cada escena vive en su propio archivo dentro de la carpeta escenas/."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from manim import *
from base_video import BaseVideo
from escenas.escena_01_presentacion import EscenaPresentacion
from escenas.escena_02_conceptos import EscenaConceptos
from escenas.escena_03_sumas_a_integral import EscenaSumasAIntegral
from escenas.escena_04_simbolos_teorema import EscenaSimbolosTeorema
from escenas.escena_05_aplicado_tema import EscenaAplicadoTema
from escenas.escena_06_problema import EscenaProblema
from escenas.escena_07_planteamiento import EscenaPlanteamiento
from escenas.escena_08_resolucion import EscenaResolucion
from escenas.escena_09_cantidad_final import EscenaCantidadFinal
from escenas.escena_10_comparacion import EscenaComparacion
from escenas.escena_11_cierre import EscenaCierre
from escenas.escena_12_creditos import EscenaCreditos


class VideoCompleto(
    EscenaPresentacion,
    EscenaConceptos,
    EscenaSumasAIntegral,
    EscenaSimbolosTeorema,
    EscenaAplicadoTema,
    EscenaProblema,
    EscenaPlanteamiento,
    EscenaResolucion,
    EscenaCantidadFinal,
    EscenaComparacion,
    EscenaCierre,
    EscenaCreditos,
    BaseVideo,
):
    def construct(self):
        self.marcas = []
        self.presentacion()
        self.conceptos_basicos()
        self.sumas_a_integral()
        self.simbolos_y_teorema()
        self.aplicado_a_tema()
        self.problema()
        self.planteamiento()
        self.resolucion()
        self.cantidad_final()
        self.comparacion()
        self.cierre()
        self.creditos()
        self.informe_tiempos()
