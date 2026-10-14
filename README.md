# MATE1134_EID_G07_2026

Video animado con Manim: **Cambio acumulado versus cantidad final**
(MAT1134 - Cálculo Intermedio, Grupo 7).

## Instalación (una sola vez por computador)

1. Instalar **uv**: en PowerShell, `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Instalar **MiKTeX** (LaTeX): `winget install MiKTeX.MiKTeX`. Después, cerrar y abrir VS Code.
   En *MiKTeX Console > Settings* poner la instalación de paquetes faltantes en **Always**.
3. Clonar e instalar dependencias:

```
git clone https://github.com/Benjamin-Alarcon/MATE1134_EID_G07_2026.git
cd MATE1134_EID_G07_2026
uv sync
uv run python verificar_entorno.py
```

## Renderizar

- Baja Calidad
```
uv run manim -pql animacion-manim.py VideoCompleto
```

- Calidad Alta
```
uv run manim -pqh animacion-manim.py VideoCompleto
```

La primera vez tarda varios minutos (se generan las fórmulas y MiKTeX descarga paquetes).

## Estructura y responsables

| Archivo | Responsable |
|---|---|
| `escenas/escena_01_presentacion.py` | Elias |
| `escenas/escena_02_conceptos.py` | Elias |
| `escenas/escena_03_sumas_a_integral.py` | Elias |
| `escenas/escena_04_simbolos_teorema.py` | Elias |
| `escenas/escena_05_aplicado_tema.py` | Elias |
| `escenas/escena_06_problema.py` | Benito |
| `escenas/escena_07_planteamiento.py` | Benito |
| `escenas/escena_08_resolucion.py` | Benito |
| `escenas/escena_12_creditos.py` | Benito |
| `escenas/escena_09_cantidad_final.py` | Benjamin |
| `escenas/escena_10_comparacion.py` | Benjamin |
| `escenas/escena_11_cierre.py` | Benjamin |
| `ajustes.py`, `base_video.py`, `animacion-manim.py` | Benjamin |

## Reglas para no tener conflictos

- Cada uno edita **solo sus archivos**. Si necesitas cambiar uno ajeno, pídelo en el grupo.
- Trabaja en una rama propia, haz `git add archivo` (nunca `git add .`) y un commit por 1 o varios cambio.
- No subas `media/`, `.venv/` ni `marcas_tiempo.txt` (ya están en `.gitignore`).
- Si cambian dependencias (`uv add ...`), avisar: se modifican `pyproject.toml` y `uv.lock`.
