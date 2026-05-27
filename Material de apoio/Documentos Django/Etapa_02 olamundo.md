# Quebrando a maldição

## Aqui começaremos a usar o mvt - Configura a view

## Criando o ola mundo!
### Passo 01:

Abrir o arquivo views.py do app que foi criado
Em nosso exemplo foi o lista

Adicionar o seguinte comando dentro deste arquivo:
1. Faça o import da biblioteca HttpResponse
2. Crie uma função chamada home que receba o paramentro request

```bash

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Ola Mundo!</h1>")
```

### Passo 02:
Configurar nosso APP

Agora abra o arquivo settings.py dentro da pasta setup
1. Procuara pela opção: INSTALLED_APPS
2. Adcionar nosso app como na imagem abaixo:


```Bash

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lista.apps.ListaConfig'
]
```
### Passo 03: 
Indicar a rota de acesso, ou seja, informar qual caminho será acessado no navegador para abrir nossa página 
1. Abra o arquivo urls.py no setup
2. Fazer o import da nossa função criada no arquivo views: from fotografia.views import home
3. Identificar a linha: urlpatterns
4. Adicionar a nossa rota:  path('', home)

Ficará assim
```bash
from fotografia.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]
```

## Testando 
Abra o endereço:  http://127.0.0.1:8000/ no seu navegador.
Se tudo deu certo você verá seu ola mundo!

### Criando nosso primeiro template

## O que é um Template no Django?
Um Template no Django é um arquivo que define a estrutura e o layout de uma página web usando HTML e tags específicas do Django para exibir dados dinâmicos.
## Passo 01:

1. Criar uma pasta chamada templates dentro da pasta lista
### Obs: esta pasta deverá se chamar templates no plural e com letras minusculas
2. Criar dentro de templates criar uma pasta chamada lista
3. Criar dentro da pasta lista o arquivo home.html
4. Escreva dentro do arquivo home.html a seguinte tag:
```bash
<h1> Ola Mundo! </h1>
```

### Passo 02: 
1. Voltar no arquivo views.py dentro da pasta lista:
2. Alterar a função home para:

```bash
def home(request):
    return render(request, "lista/home.html")

```