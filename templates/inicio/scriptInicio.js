let cartItems = []; // Array para almacenar los productos en el carrito
let cartCount = 0; // Contador de productos en el carrito

// Función para agregar productos al carrito
function addToCart(productName, productPrice) {
    // Verifica si el producto ya está en el carrito
    let product = cartItems.find(item => item.name === productName);

    if (product) {
        product.quantity++; // Si ya está, aumenta la cantidad
    } else {
        // Si el producto no está, agrega un nuevo producto
        product = {
            name: productName,
            price: productPrice,
            quantity: 1
        };
        cartItems.push(product);
    }

    cartCount++; // Aumenta el contador de productos en el carrito
    document.getElementById("cart-count").textContent = cartCount; // Actualiza el contador en el carrito
    updateCartPopup(); // Actualiza la ventana emergente del carrito
}