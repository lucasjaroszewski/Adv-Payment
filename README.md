# Advance Payment

## Sobre o projeto
https://adv-payment-jwt.herokuapp.com/

Desenvolvido com o __Django Rest Framework__, o projeto trata-se da construção de uma API _(Application Programming Interface)_ para facilitar as operações de uma empresa que antecipa pagamentos. No projeto, existem os usuários fornecedores e a empresa que administra os pagamentos. Para fornecer o melhor fluxo de caixa ao fornecedor e rentabilizar o caixa da empresa, a empresa concede um desconto a todos os pagamentos que forem adiantados, de acordo com a fórmula abaixo:

```
NOVO_VALOR = VALOR_ORIGINAL - (VALOR_ORIGINAL * ((3% / 30) * DIFERENCA_DE_DIAS))
```

## Tecnologias
- Django REST framework (Python)
- Autenticação por Token (JWT)
- PostgreSQL (Banco de dados)
- Bootstrap (CSS)
- Celery (E-mails automáticos)
- Logging (Qualquer modificação de pagamento na API)
- Coverage (Testes)
- Deploy (Heroku)

## Como executar o projeto

```bash
# Clone o repositório
git clone https://github.com/lucasjaroszewski/Adv-Payment

# Acesse a pasta Adv-Payment
cd Adv-Payment

# Crie e ative o ambiente virtual
virtualenv myenv
source myenv/Scripts/activate

# Instale as dependências do projeto
pip install -r requirements.txt

# Execute o makemigrations e o migrate do django
python manage.py makemigrations
python manage.py migrate

# Execute o servidor
python manage.py runserver
```

## Documentação

### Funcionamento do API

```
# Quando um cliente se cadastra no aplicativo, ele se torna um fornecedor de produtos
/api/user-register/
# Através do login, é gerado um token (JWT) com duração de 60 minutos
/api/user-token/

# O cliente pode criar e fazer solicitações de pagamentos adiantados pelo dashboard
# Acesso ao Dashboard: /dashboard/
/api/payment-create/
/api/payment-update/<str:id>/

# A empresa pode criar/deletar e aceitar/negar pedidos solicitados pelo fornecedor
# Acesso ao Admin Dashboard: /dashboard/admin/
/api/payment-create/
/api/payment-update/
/api/payment-delete/

# Em todas as atualizações feitas por ambos, é enviado um e-mail automático ao fornecedor
# Todos os pagamentos que passarem da data de validade não podem ser mais pagos
```

### API

```
# POST /api/user-register/ - Cria um novo usuário
# POST /api/user-login/ - Faz o login do usuário
# POST /api/user-logout/ - Faz o logout do usuário
# GET /api/user-token/ - Mostra o token JWT do usuário

# POST /api/payment-create/ - Cria um novo pagamento
# GET /api/payment-list/ - Lista todos os pagamentos
# POST /api/payment-update/<str:id>/ - Faz a atualização do pagamento
# DELETE /api/payment-delete/<str:id>/ - Deleta o pagamento
```

### Testes

```
# Para execução dos testes acesse /Adv-Payment/
# Execute os comaandos do Coverage

coverage run --omit 'myenv/*' --omit '*/migrations/*' -m unittest
coverage run manage.py test
```
