# Agenda

Sistema didático "Agenda".

### Como desenvolver ?

1. Clone o repositório
2. Crie um virtualenv 
3. Ative a virtualenv
4. Instale as dependências
5. Execute os testes

```console
git clone https://github.com/orlandosaraivajr/agenda.git
cd agenda/
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt 
pytest
pytest --cov=.
coverage html
ipython -i main.py 
```
