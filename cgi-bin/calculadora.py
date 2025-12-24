
import cgi
import re

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
operacion = form.getvalue("operacion", "")

html = """
<html>
<head>
    <title>Resultado</title>
</head>
<body>
<h1>Resultado</h1>
"""

patron = r'^(\d+)\s*([\+\-\*/])\s*(\d+)$'
match = re.match(patron, operacion)

if match:
    num1 = int(match.group(1))
    operador = match.group(2)
    num2 = int(match.group(3))

    try:
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2

        html += f"<p>{num1} {operador} {num2} = <strong>{resultado}</strong></p>"

    except ZeroDivisionError:
        html += "<p>Error: División por cero</p>"
else:
    html += "<p>Error: Operación no válida</p>"

html += """
<br>
<a href="/html/index.html">Volver</a>
</body>
</html>
"""

print(html)
