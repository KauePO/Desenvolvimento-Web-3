from core.models import FeriadoModel
from django.test import TestCase
from datetime import datetime

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'natal')

    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'natal.html')

class FeriadoModelTest(TestCase):
    def setUp(self):
        self.cadastro = FeriadoModel.objects.create(nome="Natal", dia=25, mes=12)

    def test_created (self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_name (self):
        feriado_no_banco = FeriadoModel.objects.first()
        self.assertEqual(feriado_no_banco.nome, 'Natal')