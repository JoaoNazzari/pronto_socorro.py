import unittest
from pronto_socorro import ProntoSocorro

class TestProntoSocorro(unittest.TestCase):
    def test_chegada_paciente(self):
        pronto_socorro = ProntoSocorro()
        pronto_socorro.chegada_paciente("Alice", 25, 7)
        self.assertEqual(len(pronto_socorro.fila_prioridades), 1)

    def test_proximo_paciente(self):
        pronto_socorro = ProntoSocorro()
        pronto_socorro.chegada_paciente("Bob", 30, 8)
        pronto_socorro.chegada_paciente("Charlie", 35, 6)
        pronto_socorro.proximo_paciente()
        self.assertEqual(len(pronto_socorro.fila_prioridades), 2)

    def test_atendimento_paciente(self):
        pronto_socorro = ProntoSocorro()
        pronto_socorro.chegada_paciente("Dave", 40, 9)
        pronto_socorro.chegada_paciente("Eve", 45, 6)
        pronto_socorro.atendimento_paciente()
        self.assertEqual(len(pronto_socorro.fila_prioridades), 1)

if __name__ == '__main__':
    unittest.main()