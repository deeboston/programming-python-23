class Estudiante {
    constructor(cedula, nombre, apellido, correo, telefono) {
        this.cedula = cedula;
        this.nombre = nombre;
        this.apellido = apellido;
        this.correo = correo;
        this.telefono = telefono;
    }

    obtenerNombreCompleto() {
        return `${this.nombre} ${this.apellido}`;
    }

    obtenerCedula() {
        return this.cedula;
    }

    obtenerCorreo() {
        return this.correo;
    }

    obtenerTelefono() {
        return this.telefono;
    }
}

// Example usage:
let estudiante1 = new Estudiante("1228805", "D'Andre Ryan", "Boston", "dandreboston707@gmail.com", "321-570-0940");
console.log("Nombre completo:", estudiante1.obtenerNombreCompleto());
console.log("Cédula:", estudiante1.obtenerCedula());
console.log("Correo electrónico:", estudiante1.obtenerCorreo());
console.log("Teléfono:", estudiante1.obtenerTelefono());
