from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Vinicius', email='viniciusfrantz@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(conexao, sessao):
    usuarios = [
        Usuario(nome='Vinicius', email='viniciusfrantz@hotmail.com'),
        Usuario(nome='Luli', email='viniciusfrantz@hotmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
