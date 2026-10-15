import shutil
import sys

problemas = 0

print("Python:", sys.version.split()[0])
if sys.version_info < (3, 12):
    print("  [ERROR] Se necesita Python 3.12 o superior. Usa: uv sync")
    problemas = problemas + 1
else:
    print("  [OK]")

print("Manim:")
try:
    import manim
    print("  [OK] versión", manim.__version__)
except ImportError:
    print("  [ERROR] Manim no está instalado. Ejecuta: uv sync")
    problemas = problemas + 1

programas = ["latex", "dvisvgm"]
for programa in programas:
    print(programa + ":")
    ruta = shutil.which(programa)
    if ruta is None:
        print("  [ERROR] No se encuentra. Instala MiKTeX y reinicia VS Code.")
        problemas = problemas + 1
    else:
        print("  [OK]", ruta)

if problemas == 0:
    print("\nTodo listo. Puedes renderizar.")
else:
    print("\nHay", problemas, "problema(s). Revisa los mensajes [ERROR] de arriba.")
