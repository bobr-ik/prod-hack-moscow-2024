async function req(){
    a = await fetch('http://localhost:5000/?id=1')
    a = await a.json()
    console.log(a)
    document.getElementById('res').innerHTML = a['site']
    console.log(a['data'])
}