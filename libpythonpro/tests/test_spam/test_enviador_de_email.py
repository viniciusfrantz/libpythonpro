import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['viniciusfrantz@hotmail.com', 'joao@hotmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'destinatario@hotmail.com',
        'Curso Python Pro',
        'Turma Henrique Bastos'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['aaahotmail.com', '']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'destinatario@hotmail.com',
            'Curso Python Pro',
            'Turma Henrique Bastos'
        )
