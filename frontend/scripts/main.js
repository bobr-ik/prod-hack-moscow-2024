async function req(){
    a = await fetch('http://localhost:5000/?id=1')
    a = await a.json()
    console.log(a)
    document.getElementById('res').innerHTML = a['site']
    console.log(a['data'])
}

function move_to_place(key) {
    switch (key) {
        case 1:
            window.location.href = "add.html";
            break;
        case 2:
            window.location.href = "owe.html";
            break;
        case 3:
            window.location.href = "debtors.html";
            break;
    }
}