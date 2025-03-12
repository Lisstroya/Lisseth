def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Calcular el promedio de temperaturas semanales por ciudad.

    Parámetros:
    temperaturas (list): Matriz 3D con temperaturas organizadas por ciudad, semana y día.
    ciudades (list): Lista con los nombres de las ciudades en el mismo orden que la matriz.

    Retorna:
    dict: Diccionario con las ciudades y sus promedios semanales.
    """
    promedios_ciudades = {}

    for i, ciudad in enumerate(ciudades):
        promedios_semana = []
        for semana_idx, semana in enumerate(temperaturas[i]):
            total_temp = sum(dia["temperatura"] for dia in semana)
            promedio = total_temp / len(semana)
            promedios_semana.append(round(promedio, 2))

        promedios_ciudades[ciudad] = promedios_semana

    return promedios_ciudades


# Datos de temperaturas de 4 ciudades durante 6 semanas
temperaturas = [
    [   # Ciudad Ambato
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 66},
            {"dia": "Martes", "temperatura": 69},
            {"dia": "Miércoles","temperatura": 72},
            {"dia": "Jueves", "temperatura": 65},
            {"dia": "Viernes", "temperatura": 68},
            {"dia": "Sábado", "temperatura": 70},
            {"dia": "Domingo", "temperatura": 71}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 63},
            {"dia": "Martes", "temperatura": 67},
            {"dia": "Miércoles","temperatura": 68},
            {"dia": "Jueves", "temperatura": 62},
            {"dia": "Viernes", "temperatura": 69},
            {"dia": "Sábado", "temperatura": 74},
            {"dia": "Domingo", "temperatura": 73}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 66},
            {"dia": "Martes", "temperatura": 67},
            {"dia": "Miércoles", "temperatura": 70},
            {"dia": "Jueves", "temperatura": 68},
            {"dia": "Viernes", "temperatura": 75},
            {"dia": "Sábado", "temperatura": 72},
            {"dia": "Domingo", "temperatura": 74}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temperatura": 68},
            {"dia": "Martes", "temperatura": 69},
            {"dia": "Miércoles", "temperatura": 70},
            {"dia": "Jueves", "temperatura": 63},
            {"dia": "Viernes", "temperatura": 71},
            {"dia": "Sábado", "temperatura": 73},
            {"dia": "Domingo", "temperatura": 72}
        ],
        [   # Semana 5
            {"dia": "Lunes", "temperatura": 70},
            {"dia": "Martes", "temperatura": 68},
            {"dia": "Miércoles", "temperatura": 69},
            {"dia": "Jueves", "temperatura": 64},
            {"dia": "Viernes", "temperatura": 66},
            {"dia": "Sábado", "temperatura": 75},
            {"dia": "Domingo", "temperatura": 74}
        ],
        [   # Semana 6
            {"dia": "Lunes", "temperatura": 59},
            {"dia": "Martes", "temperatura": 67},
            {"dia": "Miércoles", "temperatura": 70},
            {"dia": "Jueves", "temperatura": 62},
            {"dia": "Viernes", "temperatura": 69},
            {"dia": "Sábado", "temperatura": 72},
            {"dia": "Domingo", "temperatura": 73}
        ]
    ],
    [   # Ciudad Esmeraldas
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 76},
            {"dia": "Martes", "temperatura": 84},
            {"dia": "Miércoles", "temperatura": 82},
            {"dia": "Jueves", "temperatura": 79},
            {"dia": "Viernes", "temperatura": 80},
            {"dia": "Sábado", "temperatura": 83},
            {"dia": "Domingo", "temperatura": 86}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 70},
            {"dia": "Martes", "temperatura": 88},
            {"dia": "Miércoles", "temperatura": 83},
            {"dia": "Jueves", "temperatura": 84},
            {"dia": "Viernes", "temperatura": 82},
            {"dia": "Sábado", "temperatura": 85},
            {"dia": "Domingo", "temperatura": 87}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 75},
            {"dia": "Martes", "temperatura": 81},
            {"dia": "Miércoles", "temperatura": 83},
            {"dia": "Jueves", "temperatura": 80},
            {"dia": "Viernes", "temperatura": 84},
            {"dia": "Sábado", "temperatura": 87},
            {"dia": "Domingo", "temperatura": 89}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temperatura": 78},
            {"dia": "Martes", "temperatura": 79},
            {"dia": "Miércoles", "temperatura": 81},
            {"dia": "Jueves", "temperatura": 82},
            {"dia": "Viernes", "temperatura": 83},
            {"dia": "Sábado", "temperatura": 86},
            {"dia": "Domingo", "temperatura": 90}
        ],
        [   # Semana 5
            {"dia": "Lunes", "temperatura": 84},
            {"dia": "Martes", "temperatura": 80},
            {"dia": "Miércoles", "temperatura": 82},
            {"dia": "Jueves", "temperatura": 77},
            {"dia": "Viernes", "temperatura": 85},
            {"dia": "Sábado", "temperatura": 87},
            {"dia": "Domingo", "temperatura": 88}
        ],
        [   # Semana 6
            {"dia": "Lunes", "temperatura": 79},
            {"dia": "Martes", "temperatura": 82},
            {"dia": "Miércoles", "temperatura": 84},
            {"dia": "Jueves", "temperatura": 89},
            {"dia": "Viernes", "temperatura": 83},
            {"dia": "Sábado", "temperatura": 85},
            {"dia": "Domingo", "temperatura": 87}
        ]
    ],
    [   # Ciudad Quito
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 78},
            {"dia": "Martes", "temperatura": 72},
            {"dia": "Miércoles", "temperatura": 71},
            {"dia": "Jueves", "temperatura": 73},
            {"dia": "Viernes", "temperatura": 75},
            {"dia": "Sábado", "temperatura": 79},
            {"dia": "Domingo", "temperatura": 80}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 72},
            {"dia": "Martes", "temperatura": 73},
            {"dia": "Miércoles", "temperatura": 76},
            {"dia": "Jueves", "temperatura": 74},
            {"dia": "Viernes", "temperatura": 77},
            {"dia": "Sábado", "temperatura": 79},
            {"dia": "Domingo", "temperatura": 81}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 76},
            {"dia": "Martes", "temperatura": 80},
            {"dia": "Miércoles", "temperatura": 75},
            {"dia": "Jueves", "temperatura": 73},
            {"dia": "Viernes", "temperatura": 77},
            {"dia": "Sábado", "temperatura": 78},
            {"dia": "Domingo", "temperatura": 80}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temperatura": 70},
            {"dia": "Martes", "temperatura": 73},
            {"dia": "Miércoles", "temperatura": 74},
            {"dia": "Jueves", "temperatura": 75},
            {"dia": "Viernes", "temperatura": 78},
            {"dia": "Sábado", "temperatura": 79},
            {"dia": "Domingo", "temperatura": 80}
        ],
        [   # Semana 5
            {"dia": "Lunes", "temperatura": 72},
            {"dia": "Martes", "temperatura": 74},
            {"dia": "Miércoles", "temperatura": 78},
            {"dia": "Jueves", "temperatura": 75},
            {"dia": "Viernes", "temperatura": 79},
            {"dia": "Sábado", "temperatura": 80},
            {"dia": "Domingo", "temperatura": 82}
        ],
        [   # Semana 6
            {"dia": "Lunes", "temperatura": 72},
            {"dia": "Martes", "temperatura": 75},
            {"dia": "Miércoles", "temperatura": 78},
            {"dia": "Jueves", "temperatura": 76},
            {"dia": "Viernes", "temperatura": 79},
            {"dia": "Sábado", "temperatura": 81},
            {"dia": "Domingo", "temperatura": 84}
        ]
    ],
    [   # Ciudad Manta
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 66},
            {"dia": "Martes", "temperatura": 70},
            {"dia": "Miércoles", "temperatura": 73},
            {"dia": "Jueves", "temperatura": 75},
            {"dia": "Viernes", "temperatura": 79},
            {"dia": "Sábado", "temperatura": 78},
            {"dia": "Domingo", "temperatura": 80}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 69},
            {"dia": "Martes", "temperatura": 73},
            {"dia": "Miércoles", "temperatura": 74},
            {"dia": "Jueves", "temperatura": 78},
            {"dia": "Viernes", "temperatura": 80},
            {"dia": "Sábado", "temperatura": 81},
            {"dia": "Domingo", "temperatura": 85}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 72},
            {"dia": "Martes", "temperatura": 73},
            {"dia": "Miércoles", "temperatura": 79},
            {"dia": "Jueves", "temperatura": 78},
            {"dia": "Viernes", "temperatura": 80},
            {"dia": "Sábado", "temperatura": 82},
            {"dia": "Domingo", "temperatura": 84}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temperatura": 71},
            {"dia": "Martes", "temperatura": 74},
            {"dia": "Miércoles", "temperatura": 76},
            {"dia": "Jueves", "temperatura": 78},
            {"dia": "Viernes", "temperatura": 80},
            {"dia": "Sábado", "temperatura": 82},
            {"dia": "Domingo", "temperatura": 84}
        ],
        [   # Semana 5
            {"dia": "Lunes", "temperatura": 72},
            {"dia": "Martes", "temperatura": 75},
            {"dia": "Miércoles", "temperatura": 77},
            {"dia": "Jueves", "temperatura": 80},
            {"dia": "Viernes", "temperatura": 81},
            {"dia": "Sábado", "temperatura": 83},
            {"dia": "Domingo", "temperatura": 85}
        ],
        [   # Semana 6
            {"dia": "Lunes", "temperatura": 73},
            {"dia": "Martes", "temperatura": 79},
            {"dia": "Miércoles", "temperatura": 78},
            {"dia": "Jueves", "temperatura": 83},
            {"dia": "Viernes", "temperatura": 82},
            {"dia": "Sábado", "temperatura": 85},
            {"dia": "Domingo", "temperatura": 88}
        ]
    ]
]
# Lista de nombres de ciudades
ciudades = ["Ambato", "Esmeraldas", "Quito", "Manta"]

# Llamar a la función y mostrar los resultados
resultados = calcular_promedio_temperaturas(temperaturas, ciudades)

for ciudad, promedios in resultados.items():
    for semana_idx, promedio in enumerate(promedios):
        print(f"Semana {semana_idx + 1}, {ciudad}: {promedio}°F")