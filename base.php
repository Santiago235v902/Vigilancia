<?php
$host = 'localhost';
$usuario = 'root';
$contraseña = '';
$baseDeDatos = 'prueba1';
$puerto = 3307; // Especifica el puerto correcto

// Conexión a la base de datos
$conexion = mysqli_connect($host, $usuario, $contraseña, $baseDeDatos, $puerto);

// Verificar la conexión
if (!$conexion) {
    die("Error al conectar a la base de datos: " . mysqli_connect_error());
}

?>
