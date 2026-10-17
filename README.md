# MATE1134_EID_G07_2026

Video animado con Manim: **Cambio acumulado versus cantidad final**
(MAT1134 - Cálculo Intermedio, Grupo 7).

## Datos del grupo

| | |
|---|---|
| **Curso** | MAT1134 - Cálculo Intermedio - sección 1|
| **Grupo** | 7 |
| **Año** | 2026 |
| **Tema** | ¿Cambio acumulado versus cantidad final? |
| **Repositorio** | https://github.com/Benjamin-Alarcon/MATE1134_EID_G07_2026 |

### Integrantes y cuentas de GitHub

| Integrante | Cuenta de GitHub |
|---|---|
| Elias Cayuqueo | [@elias-cv](https://github.com/elias-cv) |
| Benjamin Alarcón | [@Benjamin-Alarcon](https://github.com/Benjamin-Alarcon) |
| Benito Carbonell | [@elbno](https://github.com/elbno) |

## Pregunta central

**¿Por qué integrar una tasa de cambio no necesariamente entrega la cantidad final?**

La integral definida de la tasa `r(t)` entre `a` y `b` mide el **cambio acumulado**: cuánto cambió la cantidad en ese intervalo. La cantidad final también depende de la cantidad con la que se partió:

```
Q(b) = Q(a) + ∫ r(t) dt   (desde a hasta b)
```

Las dos coinciden solo cuando la cantidad inicial es 0.

## Ejemplo del video

Un estanque tiene capacidad total de 30 L y parte con 20 L de agua. Una manguera echa 3 L cada 2 segundos, es decir, una tasa constante `r(t) = 1,5 L/s`. Se estudia el intervalo de `t = 0` a `t = 5` s.

- Cambio acumulado: `∫ 1,5 dt` de 0 a 5 `= 7,5 L`
- Cantidad final: `Q(5) = 20 + 7,5 = 27,5 L`, que es menor que 30 L, por lo que no se desborda.

## Versiones y dependencias

| Herramienta | Versión |
|---|---|
| Python | 3.12 (fijada en `.python-version`) |
| Manim Community | 0.22.0 |
| uv (gestor de entorno) | cualquier versión reciente |
| LaTeX (MiKTeX en Windows) | necesario para las fórmulas; incluye `latex` y `dvisvgm` |

Las dependencias de Python están declaradas en `pyproject.toml` y sus versiones exactas en `uv.lock`. No hay que instalarlas a mano: las instala `uv sync`.

## Instalación (una sola vez por computador)

1. **Instalar uv.** En PowerShell:

   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   Después, cerrar y volver a abrir VS Code, y comprobar con `uv --version`.

2. **Instalar MiKTeX (LaTeX):**

   ```
   winget install MiKTeX.MiKTeX
   ```

   Después, cerrar y volver a abrir VS Code. En *MiKTeX Console > Settings > General* dejar la instalación de paquetes faltantes en **Always**.

3. **Clonar el repositorio e instalar las dependencias:**

   ```
   git clone https://github.com/Benjamin-Alarcon/MATE1134_EID_G07_2026.git
   cd MATE1134_EID_G07_2026
   uv sync
   uv run python verificar_entorno.py
   ```

   `verificar_entorno.py` revisa Python, Manim, `latex` y `dvisvgm`. Todo debe salir en `[OK]`. uv descarga solo la versión de Python que pide el proyecto.

## Cómo renderizar el video

Siempre desde la carpeta del repositorio.

Vista previa rápida (480p, 15 fps):

```
uv run manim -pql animacion-manim.py VideoCompleto
```

Calidad final (1080p, 60 fps):

```
uv run manim -pqh animacion-manim.py VideoCompleto
```

El archivo queda en `media/videos/animacion-manim/<calidad>/VideoCompleto.mp4`.

- La primera vez tarda varios minutos: se generan las fórmulas y MiKTeX descarga los paquetes que falten.
- Cada render genera `marcas_tiempo.txt`, con el minuto de cada sección. Sirve para sincronizar la grabación de voz con el video.
- Para acortar o alargar todas las pausas, se cambia `FACTOR_PAUSA` en `ajustes.py`.

## Escenas

El video completo es la clase `VideoCompleto` (en `animacion-manim.py`), que une las 12 escenas en este orden:

| N.º | Archivo | Contenido |
|---|---|---|
| 1 | `escenas/escena_01_presentacion.py` | Presentación: integrantes, tema y pregunta central |
| 2 | `escenas/escena_02_conceptos.py` | Conceptos básicos |
| 3 | `escenas/escena_03_sumas_a_integral.py` | De las sumas de Riemann a la integral |
| 4 | `escenas/escena_04_simbolos_teorema.py` | Símbolos de la integral y Teorema Fundamental del Cálculo |
| 5 | `escenas/escena_05_aplicado_tema.py` | Aplicación al tema: cambio acumulado y cantidad final |
| 6 | `escenas/escena_06_problema.py` | Ejemplo: el problema del estanque |
| 7 | `escenas/escena_07_planteamiento.py` | Planteamiento con la tasa `r(t)` |
| 8 | `escenas/escena_08_resolucion.py` | Resolución: cálculo del cambio acumulado |
| 9 | `escenas/escena_09_cantidad_final.py` | Cantidad final `Q(t) = 20 + 1,5 t` |
| 10 | `escenas/escena_10_comparacion.py` | Comparación entre cambio acumulado y cantidad final |
| 11 | `escenas/escena_11_cierre.py` | Respuesta a la pregunta central y cierre |
| 12 | `escenas/escena_12_creditos.py` | Créditos: fuentes, recursos y declaración de IA |

### Archivos de apoyo

| Archivo | Para qué sirve |
|---|---|
| `animacion-manim.py` | Une las 12 escenas en `VideoCompleto` |
| `base_video.py` | Funciones comunes: pausas, texto, voz, marcas de tiempo |
| `ajustes.py` | Datos del grupo, fuentes, recursos y declaración de IA que aparecen en el video |
| `verificar_entorno.py` | Comprueba que el computador está listo para renderizar |
| `pyproject.toml`, `uv.lock`, `.python-version` | Entorno reproducible |

Cada escena es una clase con un solo método. `base_video.py` define `BaseVideo`, y `VideoCompleto` combina todas las escenas con `BaseVideo`.

## Reparto del trabajo

| Integrante | Escenas | Archivos |
|---|---|---|
| Elias Cayuqueo | 1 a 5 | `escena_01` a `escena_05`  `ajustes.py`, `base_video.py`, `animacion-manim.py` |
| Benito Carbonell | 6, 7, 8 y 12 | `escena_06`, `escena_07`, `escena_08`|
| Benjamin Alarcón | 9, 10 y 11, y la integración | `escena_09`, `escena_10`, `escena_11`, `escena_12`, |

Cada integrante subió su parte desde una rama propia mediante un Pull Request, revisado y mergeado por otro integrante. No se subió código directamente a `main`.

## Referencias
1. Apunte base: “Introducción a la integral”, Cálculo Intermedio, Ingeniería Civil Informática, 2026.

2. Stewart, J. (2012). Cálculo de una variable. Trascendentes tempranas (7.ª ed.). Cengage Lear
ning. Sec. 5.4, Teorema del cambio neto, p. 401. ISBN: 978-607-481-881-9

3. Larson, R. y Edwards, B. H. (2016). Cálculo (Tomo 1). Cengage Learning. Sec. 4.3, pp. 271 - 272. eISBN: 978-607-522-016-1

4. Manim Community. *Manim Community Documentation*, (v0.22.0). 
- https://docs.manim.community/

No se adaptó código externo.

## Declaración de uso de IA

- **Herramienta:** Claude (Anthropic).
- **Finalidad y partes apoyadas:** apoyo en la escritura y organización del código de Manim (división del video en escenas) y ayuda para escribir informe con Latex.

- **Verificación:** cada escena se ejecutó y se revisó en el video. Los cálculos del ejemplo se comprobaron a mano contra el apunte y los libros citados, y el contenido matemático fue revisado por los tres integrantes.

## Versión entregada

El SHA del commit final entregado se indica en la ficha PDF. Para consultarlo en el repositorio, con la última versión de `main`:

```
git rev-parse HEAD
```

## Reglas para no tener conflictos

- Cada uno edita **solo sus archivos**. Si necesitas cambiar uno ajeno, pídelo en el grupo.
- Trabaja en una rama propia, haz `git add archivo` (nunca `git add .`) y un commit por 1 o varios cambios.
- No subas `media/`, `.venv/` ni `marcas_tiempo.txt` (ya están en `.gitignore`).
- Si cambian dependencias (`uv add ...`), avisar: se modifican `pyproject.toml` y `uv.lock`.