let cartItems = []; // Array para almacenar los productos en el carrito

// Función para agregar productos al carrito
function addToCart(productName, price) {
    cartItems.push({ name: productName, price: price });
    updateCart(); // Actualiza la vista del carrito
}

// Función para actualizar el carrito
function updateCart() {
    let total = 0;
    cartItems.forEach(item => {
        total += item.price;
    });

    // Actualiza el contador de productos en el carrito
    document.getElementById("cart-count").textContent = cartItems.length;

    // Actualiza el total del carrito
    document.getElementById("total-carrito").textContent = `$${total.toFixed(2)}`;
}
// Función para filtrar los productos según las categorías seleccionadas

function filterProducts() {
    // Obtener todos los productos
    const products = document.querySelectorAll('.producto');
    
    // Obtener todas las categorías seleccionadas
    const electronics = document.getElementById('electronica').checked;
    const bathAndKitchen = document.getElementById('bano-cocina').checked;
    const tools = document.getElementById('herramientas').checked;
    const garden = document.getElementById('jardin').checked;
    const construction = document.getElementById('construccion').checked;
    
    // Si no hay ninguna categoría seleccionada, mostrar todos los productos
    if (!electronics && !bathAndKitchen && !tools && !garden && !construction) {
        products.forEach(product => {
            product.style.display = 'block'; // Muestra todos los productos
        });
        return;
    }

    // Si hay categorías seleccionadas, mostrar solo los productos de esas categorías
    products.forEach(product => {
        const category = product.classList[1]; // Obtiene la categoría de la clase del producto

        // Mostrar el producto solo si la categoría está seleccionada
        if (
            (electronics && category.includes('electronica')) ||
            (bathAndKitchen && category.includes('bano-cocina')) ||
            (tools && category.includes('herramientas')) ||
            (garden && category.includes('jardin')) ||
            (construction && category.includes('construccion'))
        ) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
}

// Función para limpiar los filtros y mostrar todos los productos
function clearFilters() {
    // Deseleccionar todos los checkboxes
    document.querySelectorAll('.filter input[type="checkbox"]').forEach(checkbox => {
        checkbox.checked = false;
    });

    // Mostrar todos los productos
    const products = document.querySelectorAll('.producto');
    products.forEach(product => {
        product.style.display = 'block';
    });
}
