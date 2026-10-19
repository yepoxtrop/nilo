from enum import Enum


# Preguntas abiertas
class QuestionSimple(Enum):
    SIMPLE1 = (
        "Convierta el número decimal 172 a binario (8 bits).",
        "10101100",
    )

    SIMPLE2 = (
        "Convierta el número binario 11001011 a decimal.",
        "203",
    )

    SIMPLE3 = (
        "Convierta el número hexadecimal A8 a decimal.",
        "168",
    )

    SIMPLE4 = (
        "Convierta el número decimal 224 a binario (8 bits).",
        "11100000",
    )

    SIMPLE5 = (
        "¿A qué clase (A, B, C, D o E) pertenece la dirección 172.16.45.10?",
        "B",
    )

    SIMPLE6 = (
        "¿Cuál es la máscara de red por defecto, en notación decimal, de la dirección 10.5.6.7?",
        "255.0.0.0",
    )

    SIMPLE7 = (
        "Con su máscara por defecto, ¿cuál es la dirección de red de 172.16.45.10?",
        "172.16.0.0",
    )

    SIMPLE8 = (
        "¿Cuál es la dirección de red de 200.15.30.77/24?",
        "200.15.30.0",
    )

    SIMPLE9 = (
        "¿Cuál es la dirección de broadcast de 200.15.30.77/24?",
        "200.15.30.255",
    )

    SIMPLE10 = (
        "Exprese el prefijo de la máscara 255.255.240.0. ( ej formato: /8).",
        "/20",
    )

    SIMPLE11 = (
        "Escriba la máscara de red /27 en notación decimal.",
        "255.255.255.224",
    )

    SIMPLE12 = (
        "¿Cuántos hosts utilizables tiene una subred con máscara /27?",
        "30",
    )

    SIMPLE13 = (
        "¿Cuál es la dirección de red de 192.168.5.130/26?",
        "192.168.5.128",
    )

    SIMPLE14 = (
        "¿Cuál es la dirección de broadcast de 192.168.5.130/26?",
        "192.168.5.191",
    )

    SIMPLE15 = (
        "¿Cuál es la última dirección de host utilizable de 192.168.5.130/26?",
        "192.168.5.190",
    )

    SIMPLE16 = (
        "¿Cuál es la última dirección del rango privado 172.16.0.0/12?",
        "172.31.255.255",
    )

    SIMPLE17 = (
        "¿A qué clase pertenece la dirección 224.0.0.5?",
        "D",
    )

    SIMPLE18 = (
        "Se divide la red 192.168.10.0/24 en 4 subredes con FLSM. ¿Cuál es el nuevo prefijo de la máscara de red?",
        "/26",
    )

    SIMPLE19 = (
        "Se divide la red 192.168.10.0/24 en 4 subredes con FLSM. ¿cuál es la dirección de red de la segunda subred?",
        "192.168.10.64",
    )

    SIMPLE20 = (
        "A la red 172.16.0.0/16 se le aplica FLSM para obtener al menos 50 subredes. ¿Cuántos bits hay que prestar?",
        "6",
    )

    SIMPLE21 = (
        "¿Cuál es el prefijo de máscara más eficiente para una LAN de 50 hosts? (formato: /8)",
        "/26",
    ) 

    SIMPLE22 = (
        "Con VLSM sobre 192.168.1.0/24 se asigna primero una LAN de 100 hosts y luego una LAN de 50 hosts. ¿Cuál es la dirección de red de la LAN de 50 hosts?",
        "192.168.1.128",
    )

    SIMPLE23 = (
        "Con VLSM sobre 192.168.1.0/24 se asignan, de mayor a menor, una LAN de 100 hosts, una de 50 hosts y una de 20 hosts. ¿Cuál es la dirección de broadcast de la LAN de 20 hosts?",
        "192.168.1.223",
    )

    QUESTION = (
        SIMPLE1, SIMPLE2, SIMPLE3, SIMPLE4, SIMPLE5,
        SIMPLE6, SIMPLE7, SIMPLE8, SIMPLE9, SIMPLE10,
        SIMPLE11, SIMPLE12, SIMPLE13, SIMPLE14, SIMPLE15,
        SIMPLE16, SIMPLE17, SIMPLE18, SIMPLE19, SIMPLE20,
        SIMPLE21, SIMPLE22, SIMPLE23,
    )
