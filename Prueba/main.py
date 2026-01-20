from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            n1 = float(request.form["nota1"])
            n2 = float(request.form["nota2"])
            n3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            if not (10 <= n1 <= 70 and 10 <= n2 <= 70 and 10 <= n3 <= 70):
                error = "Las notas deben estar entre 10 y 70."
            elif not (0 <= asistencia <= 100):
                error = "La asistencia debe estar entre 0 y 100."
            else:
                promedio = (n1 + n2 + n3) / 3
                estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
                resultado = {"promedio": round(promedio, 2), "estado": estado}
        except ValueError:
            error = "Debes ingresar solo números."

    return render_template("ejercicioI.html", resultado=resultado, error=error)

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    resultado = None
    error = None

    if request.method == "POST":
        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        if not nombre1 or not nombre2 or not nombre3:
            error = "Debes ingresar los 3 nombres."
        else:
            mayor = max([nombre1, nombre2, nombre3], key=len)
            resultado = {"mayor": mayor, "largo": len(mayor)}

    return render_template("ejercicioII.html", resultado=resultado, error=error)

if __name__ == "__main__":
    app.run(debug=True)
