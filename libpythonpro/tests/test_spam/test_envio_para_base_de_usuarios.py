from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


# Mock - troca um objeto por outro
class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Vinicius', email='viniciusfrantz@hotmail.com'),
            Usuario(nome='Luli', email='viniciusfrantz@hotmail.com')
        ],
        [
            Usuario(nome='Vinicius', email='viniciusfrantz@hotmail.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'viniciusfrantz@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Vinicius', email='viniciusfrantz@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'lulifrantz@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    enviador.enviar.assert_called_once_with(
        'lulifrantz@hotmail.com',
        'viniciusfrantz@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
