def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el monto del descuento en función del porcentaje dado.

    :parametros monto_total: Monto total de la compra.
    :parametros porcentaje_descuento: Porcentaje de descuento a aplicar (15%)
    :return: Monto del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Llamadas a la función
monto1 = 300
monto2 = 900

# Primera llamada
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# Segunda llamada
descuento2 = calcular_descuento(monto2, 15)
monto_final2 = monto2 - descuento2


print(f"Monto total: ${monto1:.2f}, Descuento: ${descuento1:.2f}, Monto final: ${monto_final1:.2f}")
print(f"Monto total: ${monto2:.2f}, Descuento: ${descuento2:.2f}, Monto final: ${monto_final2:.2f}")