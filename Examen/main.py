from flask import Flask, render_template, request

app = Flask(__name__)
#según lo solicitado son 9000
PRECIO_TARRO = 9000

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            nombre = request.form.get("nombre", "").strip()
            edad_str = request.form.get("edad", "").strip()
            tarros_str = request.form.get("tarros", "").strip()

            if not nombre:
                error = "Debes ingresar tu nombre."
            else:
                edad = int(edad_str)
                tarros = int(tarros_str)

                if edad < 0:
                    error = "La edad no puede ser negativa."
                elif tarros <= 0:
                    error = "La cantidad de tarros debe ser mayor a 0."
                else:
                    total_sin_descuento = tarros * PRECIO_TARRO

                    # Descuento según edad:
                    # si es menor a 18 no hay descuento
                    # si es mayor o igual a 18 y menor o igual a 30 el descuento es de 15
                    # si es mayor a 30 el descuento es de 25
                    if 18 <= edad <= 30:
                        porc_desc = 0.15
                    elif edad > 30:
                        porc_desc = 0.25
                    else:
                        porc_desc = 0.0

                    monto_desc = total_sin_descuento * porc_desc
                    total_pagar = total_sin_descuento - monto_desc

                    resultado = {
                        "nombre": nombre,
                        "total_sin_descuento": total_sin_descuento,
                        "porc_desc": int(porc_desc * 100),
                        "monto_desc": monto_desc,
                        "total_pagar": total_pagar
                    }

        except ValueError:
            error = "Edad y cantidad de tarros deben ser números enteros."

    return render_template("ejercicioI.html", resultado=resultado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    error = None

    # Usuarios registrados
    users = {
        "juan": "admin",
        "pepe": "user"
    }

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        password = request.form.get("password", "").strip()

        if usuario in users and users[usuario] == password:
            if usuario == "juan":
                mensaje = "Bienvenido Administrador juan"
            elif usuario == "pepe":
                mensaje = "Bienvenido Usuario pepe"
        else:
            error = "Usuario o contraseña incorrectos"

    return render_template("ejercicioII.html", mensaje=mensaje, error=error)


if __name__ == "__main__":
    app.run(debug=True)
