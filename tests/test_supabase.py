from src.gerador import PasswordGenerator

def test_salvar_senha_sucesso(mock_user_id, mock_supabase):
    """Testa salvamento de senha no BD"""
    mock_supa = mock_supabase.return_value.table.return_value.insert
    mock_supa.return_value.execute.return_value.data = [
        {'id': '123', 'password_text': 'test123!'}
    ]

    generator = PasswordGenerator(mock_user_id)
    resultado = generator.salvar_senha('test123!', 'random', 8)

    assert resultado is not None
    assert resultado['password_text'] == 'test123!'


def test_listar_senhas(mock_user_id, mock_supabase):
    """Testa listagem de senhas"""
    mock_supa = mock_supabase.return_value.table.return_value.select
    mock_supa.return_value.eq.return_value.order.return_value.limit\
        .return_value.execute.return_value.data = [
            {'id': '1', 'password_text': 'senha1'},
            {'id': '2', 'password_text': 'senha2'}
        ]

    generator = PasswordGenerator(mock_user_id)
    resultado = generator.listar_senhas()

    assert len(resultado) == 2
