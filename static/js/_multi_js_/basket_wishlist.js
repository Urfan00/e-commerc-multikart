function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


const addProduct = {
    addToWishlist(ProductID) {
        return fetch('http://localhost:8000/api/wishlist/', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('user-access-token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        })
    }
}

const deleteProduct = {
    deleteFromWishlist(ProductID) {
        return fetch('http://localhost:8000/api/wishlist/', {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('user-access-token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        });
    }
}


function functionAddToWishlist(ProductID) {
    addProduct.addToWishlist(ProductID);
}


function removeWishlist(ProductID) {
    deleteProduct.deleteFromWishlist(ProductID)
}


const deleteBasket = {
    deleteProductBasket(ProductID) {
        return fetch('http://localhost:8000/api/basket/', {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('user-access-token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        });
    }
}


function removeBasket(ProductID) {
    deleteBasket.deleteProductBasket(ProductID)
}


const addCart = {
    addProductCart(ProductID, Quantity) {
        return fetch('http://localhost:8000/api/basket/', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('user-access-token')}`
            },
            body: JSON.stringify({
                'product':ProductID,
                'quantity':Quantity
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                window.alert(data.message);
            }
        })
    }
}


function AddToBasket(ProductID) {
    const quantity = 1;
    addCart.addProductCart(ProductID, quantity);
    deleteProduct.deleteFromWishlist(ProductID);
}


function AddToBasketinDetail(ProductID) {
    const quantity = parseInt(document.getElementById('detail-qty').value);
    addCart.addProductCart(ProductID, quantity);
    deleteProduct.deleteFromWishlist(ProductID);
}

const subscribe_form = document.getElementById('subscribeForm')

subscribe_form.addEventListener('submit', function (event) {
    event.preventDefault()
    
    let e_mail = document.getElementById('mce-EMAIL')

    const data = {
        email: e_mail.value
    };

    fetch('http://localhost:8000/api/subscribe/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('user-access-token')}`
        },
        body: JSON.stringify(data),
    })
        .then((response) => {
            if (response.ok){
                alert('Successfully registered !')
            } else {
                alert('Error')
            }
        })
        .then((data) => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });

});
