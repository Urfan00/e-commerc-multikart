let form = document.getElementById("login-form")


form.addEventListener('submit', async function(event) {

    let postData = {
        username: form.username.value,
        password: form.password.value
    }

    let response = await fetch('/api/login/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(postData)
    })

    if (response.ok) {
        let data = await response.json()
        localStorage.setItem('user-detail', JSON.stringify(data))
        localStorage.setItem('user-access-token', data.access)
    }

})