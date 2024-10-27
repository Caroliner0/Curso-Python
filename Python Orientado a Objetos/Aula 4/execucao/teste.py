from modelo.medico import Medico
from modelo.paciente import Paciente

if __name__ == '__main__':

    med1 = Medico("Rui", "Cardiologista")
    med2 = Medico ("Ana", "Pediatra")
    med3 = Medico ('Bob', 'Ortopedista')

    pac1 = Paciente ('Nath', "F", 34)
    pac2 = Paciente ('Leo', 'M', 23)
    pac3 = Paciente('Cadu', 'M', 16)
    pac4 = Paciente ('Maria', 'F', 24)

    #Relacionamentos

    med1.pacientes = [pac1, pac4]
    med2.pacientes = [pac3]
    med3.pacientes = [pac1, pac2, pac3, pac4]

    pac1.medicos = [med1, med3]
    pac2.medicos = [med3]
    pac3.medicos = [med2, med3]
    pac4.medicos = [med1, med3]

    #lISTA DE MEDICOS
    medicos = [med1, med2, med3]

    for medico in medicos:
        print("Medico: " + str(medico))
        print('_______________')
        for paciente in medico.pacientes:
          print("Paciente: " + str(paciente))
          print ('***************')
        print ('-------------------------')


    pass