# Matriz 3D con datos de temperaturas por ciudad, semana y día
temperaturas = [
    [   # Ciudad Cuenca
        [   # Semana 1
            {"dia": "Lunes", "temp": 70},
            {"dia": "Martes", "temp": 79},
            {"dia": "Miércoles", "temp": 82},
            {"dia": "Jueves", "temp": 78},
            {"dia": "Viernes", "temp": 84},
            {"dia": "Sábado", "temp": 88},
            {"dia": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 75},
            {"dia": "Martes", "temp": 79},
            {"dia": "Miércoles", "temp": 84},
            {"dia": "Jueves", "temp": 83},
            {"dia": "Viernes", "temp": 87},
            {"dia": "Sábado", "temp": 90},
            {"dia": "Domingo", "temp": 93}
        ]
    ],
    [   # Ciudad Guayaquil
        [   # Semana 1
            {"dia": "Lunes", "temp": 71},
            {"dia": "Martes", "temp": 72},
            {"dia": "Miércoles", "temp": 74},
            {"dia": "Jueves", "temp": 70},
            {"dia": "Viernes", "temp": 76},
            {"dia": "Sábado", "temp": 78},
            {"dia": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 69},
            {"dia": "Martes", "temp": 71},
            {"dia": "Miércoles", "temp": 70},
            {"dia": "Jueves", "temp": 73},
            {"dia": "Viernes", "temp": 75},
            {"dia": "Sábado", "temp": 77},
            {"dia": "Domingo", "temp": 88}
        ]
    ],
    [   # Ciudad Loja
        [   # Semana 1
            {"dia": "Lunes", "temp": 77},
            {"dia": "Martes", "temp": 79},
            {"dia": "Miércoles", "temp": 80},
            {"dia": "Jueves", "temp": 78},
            {"dia": "Viernes", "temp": 84},
            {"dia": "Sábado", "temp": 87},
            {"dia": "Domingo", "temp": 93}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 76},
            {"dia": "Martes", "temp": 80},
            {"dia": "Miércoles", "temp": 82},
            {"dia": "Jueves", "temp": 83},
            {"dia": "Viernes", "temp": 88},
            {"dia": "Sábado", "temp": 90},
            {"dia": "Domingo", "temp": 92}
        ]
    ]
]

# Lista de nombres de ciudades
ciudades = ["Cuenca", "Guayaquil", "Loja"]

# Calcular y mostrar el promedio de temperaturas semanales por ciudad
for i, ciudad in enumerate(ciudades):
    for semana_idx, semana in enumerate(temperaturas[i]):
        total_temp = sum(dia["temp"] for dia in semana)
        promedio = total_temp / len(semana)
        print(f"Semana {semana_idx + 1}, {ciudad}: {promedio:.2f}°F")