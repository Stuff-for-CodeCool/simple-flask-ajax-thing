const rezultat = document.querySelector("#rezultat");

document.querySelector("#posting").addEventListener("submit", async (e) => {
    e.preventDefault();
    const rez = await api.post(e.target.action, {
        name: e.target.ceva.value,
    });
    rezultat.innerText = rez.message;
    e.target.reset();
    // remote(e, "POST", "ceva", e.target.action)
});

document.querySelector("#modify").addEventListener("submit", async (e) => {
    e.preventDefault();
    const rez = await api.put(e.target.action, {
        name: e.target.altceva.value,
    });
    rezultat.innerText = rez.message;
    e.target.reset();
    // remote(e, "PUT", "altceva", e.target.action)
});

document.querySelector("#delete").addEventListener("click", async (e) => {
    e.preventDefault();
    const rez = await api.delete(e.target.href);
    rezultat.innerText = rez.message;
    // remote(e, "DELETE", "altceva", e.target.href)
});

const api = {
    get: async function (url) {
        const request = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
        });

        if (request.ok) {
            return await request.json();
        } else {
            return `Error in GET request`;
        }
    },
    post: async function (url, data) {
        const request = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });

        if (request.ok) {
            return await request.json();
        } else {
            return `Error in POST request`;
        }
    },
    put: async function (url, data) {
        const request = await fetch(url, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });

        if (request.ok) {
            return await request.json();
        } else {
            return `Error in PUT request`;
        }
    },
    delete: async function (url) {
        const request = await fetch(url, {
            method: "DELETE",
            headers: { "Content-Type": "application/json" },
        });

        if (request.ok) {
            return await request.json();
        } else {
            return `Error in DELETE request`;
        }
    },
};

// async function remote(e, method, name, url) {
//     e.preventDefault();

//     const options = {
//         method: method,
//         headers: { "Content-Type": "application/json" },
//     };

//     if (method == "POST" || method == "PUT") {
//         options["body"] = JSON.stringify({
//             name: e.target[name].value,
//         });
//     }

//     const request = await fetch(url, options);

//     if (request.ok) {
//         const response = await request.json();
//         rezultat.innerText = response.message;
//         e.target.reset();
//     } else {
//         rezultat.innetText = `Error in ${method} request`;
//     }
// }
