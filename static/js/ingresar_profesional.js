function guardar() {
    let nombre_ingresado = document.getElementById("nombre").value //input
    let apellido_ingresado = document.getElementById("apellido").value 
    let especialidad_ingresada = document.getElementById("especialidad").value 
    let imagen_ingresada = document.getElementById("imagen").value

    console.log(nombre_ingresado,apellido_ingresado,especialidad_ingresada,imagen_ingresada,genero_ingresado);
    // Se arma el objeto de js 
    let datos = {
        nombre: nombre_ingresado,
        apellido:apellido_ingresado,
        especialidad:especialidad_ingresada,
        imagen:imagen_ingresada
    }
    console.log(datos);
    
    let url = "https://codogrupo22.pythonanywhere.com/registro"
    var options = {
        body: JSON.stringify(datos),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "../templates/staff.html";  
            
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}

function modificar() {
    let id = document.getElementById("id").value
    let nombre_ingresado = document.getElementById("nombre").value
    let apellido_ingresado = document.getElementById("apellido").value 
    let especialidad_ingresada = document.getElementById("especialidad").value 
    let imagen_ingresada = document.getElementById("imagen").value 

    let datos = {
        nombre: nombre_ingresado,
        apellido:apellido_ingresado,
        especialidad:especialidad_ingresada,
        imagen:imagen_ingresada
    }

    console.log(datos);

    let url = "https://codogrupo22.pythonanywhere.com/update/"+id
    var options = {
        body: JSON.stringify(datos),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        // el navegador seguirá automáticamente las redirecciones y
        // devolverá el recurso final al que se ha redirigido.
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            
            //Puedes utilizar window.location.href para obtener la URL actual, redirigir a otras páginas
           window.location.href = "../templates/staff.html";
          
        })
        .catch(err => {
            this.error = true
            console.error(err);
            alert("Error al Modificar")
        })      
}