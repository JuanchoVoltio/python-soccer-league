class Pago_nomina:
    def __init__(self, salario):
        self.salario = salario
        self.acumulado = 0

    def dt(self, bono_pole):
        if(bono_pole):
            self.salario = round(self.salario * 1.10, 2)

    def piloto(self, puesto_clasi, bono_pista):
        if(puesto_clasi == 1 or puesto_clasi == 2):
            self.salario = round(self.salario * 1.10, 2)
        if(bono_pista):
            self.salario = round(self.salario * 1.20, 2)

    def mecanico(self, tiempo_pits):
        if(tiempo_pits <= 2.2):
            self.salario = round(self.salario * 1.05, 2)

    def __str__(self):
        return "El costo de la nomina es: " + str(self.salario) + " USD"


salario_final = Pago_nomina(10000)
salario_final.dt(True)
salario_final.piloto(2,False)
salario_final.mecanico(2)

print(salario_final)