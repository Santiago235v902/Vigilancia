<?php
include("base.php");

if (isset($_POST['register'])) {
    if (strlen($_POST['name']) >= 1 && strlen($_POST['contraseña']) >= 1 && strlen($_POST['dni']) >= 1) {
        $name = $_POST['name'];
        $dni = $_POST['dni'];  // Corregido: uso de corchetes en lugar de paréntesis
        $contraseña = $_POST['contraseña'];  // Obtener la contraseña del formulario
        $contraseña_hash = password_hash($contraseña, PASSWORD_DEFAULT);  // Encriptar la contraseña
        
        // Insertar la contraseña encriptada en la base de datos
        $consulta = "INSERT INTO `empleados`(Nombre, Contraseña, DNI) 
                     VALUES ('$name', '$contraseña_hash', '$dni')";
        
        // Ejecutar la consulta y verificar el resultado
        $resultados = mysqli_query($conexion, $consulta);
        if ($resultados) {
            echo "Registro exitoso!";
        } else {
            echo "Error en el registro: " . mysqli_error($conexion);
        }
    } else {
        echo "Todos los campos deben ser llenados.";
    }
}
?>
