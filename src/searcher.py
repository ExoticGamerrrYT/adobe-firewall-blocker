import os


def buscar_programas_adobe(directorio_base):
    programas_adobe = []
    programas_principales = (
        "Photoshop.exe",
        "Adobe Premiere Pro.exe",
        "Adobe Media Encoder.exe",
        "Adobe Audition.exe",
    )

    # Verify that the base directory exists
    if not os.path.exists(directorio_base):
        print(f"El directorio {directorio_base} no existe.")
        return programas_adobe

    # Traverse all folders within the base directory
    for carpeta in os.listdir(directorio_base):
        ruta_carpeta = os.path.join(directorio_base, carpeta)

        # Check if it is a folder
        if os.path.isdir(ruta_carpeta):
            # Traverse files within the folder
            for archivo in os.listdir(ruta_carpeta):
                if archivo in programas_principales:
                    ruta_archivo = os.path.join(directorio_base, carpeta, archivo)
                    programas_adobe.append(ruta_archivo)

    return programas_adobe
