
const formulario = document.getElementById("formulario");
const btn = document.getElementById("btn");

formulario.addEventListener("submit", async (e) => {
    e.preventDefault();

    btn.disabled = true;

    const name = document.getElementById("nombre").value;
    const email = document.getElementById("correo").value;
    const password = document.getElementById("contra").value;
    const edad = Number(document.getElementById("edad").value);

    const datos = {
        nombre: name,
        email: email,
        contra: password,
        edad: edad
    };

    console.log("Datos enviados:", datos);

    try {
        const respuesta = await fetch("http://127.0.0.1:8000/usuarios", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(datos)
        });

        const res = await respuesta.json();

        if (!respuesta.ok) {
            console.error("Error del backend:", res);
            return;
        }

        console.log("Respuesta del servidor:", res);
        formulario.reset();

        document.getElementById("mensaje").textContent = "Usuario creado exitosamente, verifica tu DB";

    } catch (error) {
        console.error("Error de conexión:", error);
    } finally {
        btn.disabled = false;
    }
});
