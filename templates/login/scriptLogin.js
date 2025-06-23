// Acceder a los elementos del formulario
const goRegisterBtn = document.getElementById("go-register");  // Botón para ir al registro
const goLoginBtn = document.getElementById("go-login");  // Botón para volver al login
const loginForm = document.getElementById("login-form");  // Formulario de login
const registerForm = document.getElementById("register-form");  // Formulario de registro

// Cuando se hace click en "Regístrate", mostrar el formulario de registro
goRegisterBtn.addEventListener("click", () => {
    loginForm.style.display = "none";  // Ocultar el formulario de login
    registerForm.style.display = "block";  // Mostrar el formulario de registro
});

// Cuando se hace click en "Inicia sesión", mostrar el formulario de login
goLoginBtn.addEventListener("click", () => {
    registerForm.style.display = "none";  // Ocultar el formulario de registro
    loginForm.style.display = "block";  // Mostrar el formulario de login
});

// Función para manejar el inicio de sesión (esto puede ser extendido para validar con backend)
const login = document.getElementById("login");
login.addEventListener("submit", (e) => {
    e.preventDefault();  // Prevenir el comportamiento por defecto (recargar la página)
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    // Validar los campos
    if (email && password) {
        alert("Iniciaste sesión con éxito!");
        // Aquí se puede agregar la lógica para validar el login con el backend
    } else {
        alert("Por favor, completa todos los campos.");
    }
});

// Función para manejar el registro de usuario (esto puede ser extendido para registrar con backend)
const register = document.getElementById("register");
register.addEventListener("submit", (e) => {
    e.preventDefault();  // Prevenir el comportamiento por defecto (recargar la página)
    const name = document.getElementById("register-name").value;
    const email = document.getElementById("register-email").value;
    const password = document.getElementById("register-password").value;
    const confirmPassword = document.getElementById("register-confirm-password").value;

    // Validar los campos
    if (name && email && password && confirmPassword) {
        if (password === confirmPassword) {
            alert("Registro exitoso!");
            // Aquí se puede agregar la lógica para registrar al usuario con el backend
        } else {
            alert("Las contraseñas no coinciden.");
        }
    } else {
        alert("Por favor, completa todos los campos.");
    }
});
