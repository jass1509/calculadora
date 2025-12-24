import cgi
import re
#vjk
print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
entrada = form.getvalue("operacion", "")

patron = r"^\s*([-+]?\d*\.?\d+)\s*([\+\-\*/])\s*([-+]?\d*\.?\d+)\s*$"

resultado_msg = ""
match = re.match(patron, entrada)

if match:
    num1 = float(match.group(1))
    operador = match.group(2)
    num2 = float(match.group(3))
    
    if operador == '+':
        res = num1 + num2
    elif operador == '-':
        res = num1 - num2
    elif operador == '*':
        res = num1 * num2
    elif operador == '/':
        res = num1 / num2 if num2 != 0 else "Error: División por cero"
    
    resultado_msg = f"<h2>Resultado: {res}</h2>"
else:
    resultado_msg = "<h2 style='color:red;'>Formato inválido. Use 'número operador número'</h2>"

print(f"""
<!DOCTYPE html>
<html lang="es">
<head><title>Resultado</title></head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    {resultado_msg}
    <p>Operación recibida: {entrada}</p>
    <a href="../html/index.html">Volver</a>
</body>
</html>
""")