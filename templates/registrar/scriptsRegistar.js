// Agregar funcionalidad para cambiar entre el formulario de login y el formulario de registro
document.getElementById("go-register").addEventListener("click", function() {
    document.getElementById("login-form").style.display = "none";
    document.getElementById("register-form").style.display = "block";
});

document.getElementById("go-login").addEventListener("click", function() {
    document.getElementById("register-form").style.display = "none";
    document.getElementById("login-form").style.display = "block";
});
