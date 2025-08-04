# 📘 Guia: Traduzindo todos os emails do chatwoot
## Pré-requisitos
- Python 3.13.x instalado
- ```make``` instalado
- Docker e acesso ao container desejado (via Portainer ou CLI)

## 🛠️ Passo a passo
1. Configure o ambiente
Copie o arquivo de exemplo .env.example para .env e adicione suas credenciais do servidor:
```bash
cp .env.example .env
```

2. Instale as dependências
Use o make para configurar o ambiente Python (criação do venv e instalação do requirements.txt):
```bash
make pysetup
```
Ou
```bash
python3 -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```

3. Liste os containers disponíveis
Para identificar o container Docker onde a aplicação será executada:
```bash
make runcontainer
```
Ou
```bash
python .\containers.py
```
Ou acesse o Portainer e copie o UUID do container desejado.

4. Configure o container no .env
No arquivo .env, defina a variável CONTAINER com o UUID obtido:

5. Execute o processo principal (main.py)
Com tudo pronto, execute:
```bash
make runmain
```
Ou
```bash
python .\main.py
```
