import unittest

from database import database

def buscar_datos(*args, **kwargs):
    for persona, atributos in database.items():
        igual = True
        for arg in args:
            if arg not in atributos.values():
                igual = False
                break
        if igual:
            return persona
    return 'No se encuentra en la base de datos'

            

class TestInDatabase(unittest.TestCase):

    def test_persona1(self):
        resultado = buscar_datos("Pablo", "Diego", "Picasso", "Ruiz", **database)
        self.assertEqual(resultado, "persona1")
    
    def test_persona2(self):
        resultado = buscar_datos("Martinez", "Adriano", "Barbuzza", "Salvador", **database)
        self.assertEqual(resultado, "persona2")

    def test_persona3(self):
        resultado = buscar_datos("Agustin", "Miguel", "Correnti", "Reinoso", **database)
        self.assertEqual(resultado, "persona3")
    
    def test_persona4(self):
        resultado = buscar_datos("Tomas", "Zalazar", **database)
        self.assertEqual(resultado, "persona4")
    
    def test_persona5(self):
        resultado = buscar_datos("Lucca", "Goria", "Ciro", **database)
        self.assertEqual(resultado, "persona5")
    


if __name__ == "__main__":
    unittest.main()
