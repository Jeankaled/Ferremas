let cartItems = []; // Array para almacenar los productos en el carrito
let cartCount = 0; // Contador de productos en el carrito
let totalAmount = 0; // Total del carrito

// Función para agregar productos al carrito
function addToCart(productName, productPrice) {
    let existingProduct = cartItems.find(item => item.name === productName);

    if (existingProduct) {
        existingProduct.quantity++;
        existingProduct.totalPrice += productPrice;
    } else {
        cartItems.push({ name: productName, price: productPrice, quantity: 1, totalPrice: productPrice });
    }

    updateCart(); // Actualiza la vista del carrito
}

// Función para actualizar el carrito en el HTML
function updateCart() {
    let cartItemsContainer = document.getElementById("cart-items");
    cartItemsContainer.innerHTML = "";

    let total = 0;
    cartItems.forEach(item => {
        total += item.totalPrice;

        let productDiv = document.createElement("div");
        productDiv.classList.add("cart-item");
        productDiv.innerHTML = `
            <p>${item.name} - $${item.price} x ${item.quantity} = $${item.totalPrice.toFixed(2)}</p>
            <button onclick="removeItem('${item.name}')">Eliminar</button>
        `;
        cartItemsContainer.appendChild(productDiv);
    });

    cartCount = cartItems.length;
    document.getElementById("cart-count").textContent = cartCount;
    totalAmount = total;
    document.getElementById("total-carrito").textContent = `$${totalAmount.toFixed(2)}`;
}

function removeItem(productName) {
    cartItems = cartItems.filter(item => item.name !== productName);
    updateCart(); 
}

function clearCart() {
    cartItems = []; 
    updateCart(); 
}

function proceedToCheckout() {
    alert("Procediendo al pago...");
}
