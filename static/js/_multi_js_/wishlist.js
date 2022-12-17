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