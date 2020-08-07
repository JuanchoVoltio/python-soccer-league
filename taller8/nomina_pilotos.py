print("=====Programa para calcular la nomina=====\n")
class Pago_nomina:
    def __init__(self, salario):
        self.salario = salario
    

    def bonodirector(self, bono_pole):
        if(bono_pole):
            self.salario = eval(self.salario) * 1.10
            print()
            print("la nomina del director es", self.salario, "ya que se obtuvo bono por pole" )
            

    def bonopiloto(self, puesto_clasi, bono_pista):
        if(puesto_clasi <=2):
            self.salario = eval(self.salario)* 1.10
            print()
            print("la nomina de los 2 pilotos es", self.salario *2,"ya que se obtuvo bono por clasificacion"  )
        else:
          pass
        if(bono_pista):
            self.salario = eval(self.salario) * 1.20
            print()
            print("la nomina de los 2 pilotos es", self.salario *2 )
        

    def bonomecanico(self, tiempo_pits):
        if(tiempo_pits <= 2.2):
            self.salario = eval(self.salario) * 1.05
            print()
            print("la nomina de los 4 mecanicos es", self.salario*4,"ya que se obtuvo bono por tiempo en pits" )

    
sueldo_base_piloto=input("Ingrese el salario del piloto \n" )
sueldo_base_mecanico=input("Ingrese el salario del mecanico \n" )
sueldo_base_director=input("Ingrese el salario base del director \n" )
salario_piloto = Pago_nomina(sueldo_base_piloto)
salario_mecanico = Pago_nomina(sueldo_base_mecanico)
salario_director = Pago_nomina(sueldo_base_director)
salario_director.bonodirector(True)
salario_piloto.bonopiloto(2,False)
salario_mecanico.bonomecanico(True)
