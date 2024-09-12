package Clases;

import java.util.Objects;

/**
 * Represents a person with attributes like name, surname, address, and age.
 */
public class Person {
    private String nombre;
    private String apellido;
    private String direccion;
    private int edad;
    
    // Constructor
    public Person(String nombre, String apellido, String direccion, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.direccion = direccion;
        setEdad(edad); // Using setter to include validation
    }

    // Getters and Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        if (edad < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
        this.edad = edad;
    }

    @Override
    public String toString() {
        return "Person{" +
                "nombre='" + nombre + '\'' +
                ", apellido='" + apellido + '\'' +
                ", direccion='" + direccion + '\'' +
                ", edad=" + edad +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return edad == person.edad &&
                nombre.equals(person.nombre) &&
                apellido.equals(person.apellido) &&
                direccion.equals(person.direccion);
    }

    @Override
    public int hashCode() {
        return Objects.hash(nombre, apellido, direccion, edad);
    }
}
