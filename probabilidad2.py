
import random

# --- 1. Crear la caja con las 60 bolas ---
ball_box = {}

for i in range(60):
    if i < 10:
        ball_box[i] = "White"
    elif (i > 9) and (i < 30):
        ball_box[i] = "Red"
    else:
        ball_box[i] = "Green"

# --- 2. Parámetros del experimento ---
num_experiments = 1000
num_tomas = 5

# --- 3. Contadores ---
count_3blancas_2rojas = 0
count_todas_mismo_color = 0

# --- 4. Simulación ---
for i in range(num_experiments):
    # Seleccionamos 5 bolas con reemplazo (por índice)
    tomas = [ball_box[random.randint(0, 60)] for i in range(num_tomas)]
    
    blanco = tomas.count("White")
    rojo = tomas.count("Red")
    verde = tomas.count("Green")

    # (1) Caso: 3 blancas y 2 rojas
    if blanco == 3 and rojo == 2:
        count_3blancas_2rojas += 1

    # (2) Caso: todas del mismo color
    if blanco == 5 or rojo == 5 or verde == 5:
        count_todas_mismo_color += 1

# --- 5. Calcular probabilidades ---
prob_3blanco_2rojo = count_3blancas_2rojas / num_experiments
prob_todas_mismo_color = count_todas_mismo_color / num_experiments

# --- 6. Mostrar resultados ---
print("=== RESULTADOS DE LA SIMULACIÓN ===")
print(f"Experimentos totales: {num_experiments}")
print(f"Probabilidad de obtener 3 blancas y 2 rojas: {prob_3blanco_2rojo:.4f} ({prob_3blanco_2rojo*100:.2f}%)")
print(f"Probabilidad de que todas sean del mismo color: {prob_todas_mismo_color:.4f} ({prob_todas_mismo_color*100:.2f}%)")
