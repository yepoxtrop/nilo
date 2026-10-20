from enum import Enum

class QuestionMultiple(Enum):
    MULTIPLE1 = (
        "¿Cuál es la representación binaria de 172?",
        ("10101010", False),
        ("10101100", True),
        ("10011100", False),
        ("11001100", False),
    )

    MULTIPLE2 = (
        "¿Cuál es el valor decimal de 11110000?",
        ("224", False),
        ("248", False),
        ("240", True),
        ("252", False),
    )

    MULTIPLE3 = (
        "¿Cuál es el valor decimal del hexadecimal FF?",
        ("15", False),
        ("127", False),
        ("256", False),
        ("255", True),
    )

    MULTIPLE4 = (
        "La dirección 150.30.5.1 pertenece a la clase:",
        ("A", False),
        ("B", True),
        ("C", False),
        ("D", False),
    )

    MULTIPLE5 = (
        "La dirección 224.0.0.9 pertenece a la clase:",
        ("C", False),
        ("B", False),
        ("D", True),
        ("E", False),
    )

    MULTIPLE6 = (
        "La máscara por defecto de una dirección Clase C es:",
        ("255.0.0.0", False),
        ("255.255.0.0", False),
        ("255.255.255.255", False),
        ("255.255.255.0", True),
    )

    MULTIPLE7 = (
        "En la dirección 10.5.6.7 con máscara por defecto, la porción de host es:",
        ("10", False),
        ("5.6.7", True),
        ("6.7", False),
        ("10.5", False),
    )

    MULTIPLE8 = (
        "La máscara /26 equivale a:",
        ("255.255.255.128", False),
        ("255.255.255.192", True),
        ("255.255.255.224", False),
        ("255.255.255.240", False),
    )

    MULTIPLE9 = (
        "La dirección de red de 192.168.1.77/26 es:",
        ("192.168.1.0", False),
        ("192.168.1.32", False),
        ("192.168.1.64", True),
        ("192.168.1.76", False),
    )

    MULTIPLE10 = (
        "La dirección de broadcast de 192.168.1.77/26 es:",
        ("192.168.1.79", False),
        ("192.168.1.127", True),
        ("192.168.1.128", False),
        ("192.168.1.255", False),
    )

    MULTIPLE11 = (
        "¿Cuántos hosts utilizables tiene una subred /28?",
        ("16", False),
        ("30", False),
        ("14", True),
        ("62", False),
    )

    MULTIPLE12 = (
        "¿Cuál de las siguientes direcciones es privada?",
        ("172.32.0.1", False),
        ("192.169.1.1", False),
        ("11.0.0.1", False),
        ("172.20.10.5", True),
    )

    MULTIPLE13 = (
        "El rango de la Clase E (reservado para uso experimental) es:",
        ("224.0.0.0 – 239.255.255.255", False),
        ("240.0.0.0 – 255.255.255.255", True),
        ("192.0.0.0 – 223.255.255.255", False),
        ("128.0.0.0 – 191.255.255.255", False),
    )

    MULTIPLE14 = (
        "La dirección 127.0.0.1 se utiliza para:",
        ("Comunicación multicast", False),
        ("Direccionamiento privado en LAN", False),
        ("Pruebas locales (loopback)", True),
        ("Asignación automática por DHCP", False),
    )

    MULTIPLE15 = (
        "¿Cuál es una dirección de host válida en la subred 192.168.10.64/26?",
        ("192.168.10.64", False),
        ("192.168.10.127", False),
        ("192.168.10.100", True),
        ("192.168.10.128", False),
    )

    MULTIPLE16 = (
        "En FLSM:",
        ("Cada subred puede tener una máscara diferente", False),
        ("Todas las subredes usan la misma máscara y tamaño", True),
        ("Solo se aplica a redes Clase A", False),
        ("No se piden bits prestados", False),
    )

    MULTIPLE17 = (
        "¿Cuántos bits hay que prestar para obtener al menos 5 subredes con FLSM?",
        ("2", False),
        ("4", False),
        ("5", False),
        ("3", True),
    )

    MULTIPLE18 = (
        "Al dividir 192.168.1.0/24 en 8 subredes con FLSM, la nueva máscara es:",
        ("255.255.255.192", False),
        ("255.255.255.224", True),
        ("255.255.255.240", False),
        ("255.255.255.248", False),
    )

    MULTIPLE19 = (
        "Si se subnetea 172.16.0.0/16 usando máscara /24, ¿cuántas subredes se obtienen?",
        ("256", True),
        ("254", False),
        ("128", False),
        ("1024", False),
    )

    MULTIPLE20 = (
        "Un equipo con la dirección 169.254.10.20 indica que:",
        ("Tiene una IP pública válida", False),
        ("No obtuvo respuesta de un servidor DHCP (APIPA)", True),
        ("Pertenece a un grupo multicast", False),
        ("Está en la red privada 10.0.0.0/8", False),
    )

    MULTIPLE21 = (
        "¿Cuál es la principal diferencia entre VLSM y FLSM?",
        ("VLSM usa una misma máscara para todas las subredes", False),
        ("VLSM permite usar máscaras de distinta longitud dentro de la misma red", True),
        ("VLSM solo funciona con direcciones Clase A", False),
        ("VLSM no necesita calcular subredes", False),
    )
    
    MULTIPLE22 = (
        "¿Qué máscara es la más adecuada para una LAN de 25 hosts?",
        ("/26", False),
        ("/27", True),
        ("/28", False),
        ("/25", False),
    )
    
    MULTIPLE23 = (
        "Al aplicar VLSM, ¿en qué orden se recomienda asignar las subredes?",
        ("De menor a mayor cantidad de hosts", False),
        ("En orden alfabético por nombre de LAN", False),
        ("De mayor a menor cantidad de hosts", True),
        ("En orden aleatorio", False),
    )
    
    MULTIPLE24 = (
        "En la red 10.0.0.0/24, ya se asignó la subred 10.0.0.0/25. ¿Cuál es la siguiente dirección de red disponible para una subred /26?",
        ("10.0.0.64", False),
        ("10.0.0.127", False),
        ("10.0.0.128", True),
        ("10.0.0.192", False),
    )

    QUESTION = (
        MULTIPLE1, MULTIPLE2, MULTIPLE3, MULTIPLE4, MULTIPLE5,
        MULTIPLE6, MULTIPLE7, MULTIPLE8, MULTIPLE9, MULTIPLE10,
        MULTIPLE11, MULTIPLE12, MULTIPLE13, MULTIPLE14, MULTIPLE15,
        MULTIPLE16, MULTIPLE17, MULTIPLE18, MULTIPLE19, MULTIPLE20,
        MULTIPLE21, MULTIPLE22, MULTIPLE23, MULTIPLE24,
    )