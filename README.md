# 📘 Guia: Traduzindo todos os templates de emails do chatwoot
## 📝 Pré-requisitos
- Python 3.13.x instalado
- Git instalado (recomendado)
- Docker ou Docker Desktop instalado
- Acesso ao container desejado (via Portainer ou CLI)
- ```make``` instalado (opcional)

## 🛠️ Passo a passo

### I. Instalação do repositório:
Caso possua o ``git`` instalado em seu computador, apenas clone o repositório:
```bash
git clone https://github.com/jeperico/emails-translation
```
Caso contrário, vá em 'Código' > 'Baixar ZIP' e extraia o zip no local desejado

### II. Configuração de ambiente
Copie o arquivo de exemplo .env.example para .env e adicione suas credenciais do servidor:
```bash
cp .env.example .env
```


### III. Instalação de dependências
Use o make para configurar o ambiente Python (criação do venv e instalação do requirements.txt):
```bash
make pysetup
```
Ou configure manualmente:
```bash
python3 -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```

### IV. Ative o ambiente virtual
Dentro do terminal, ative o venv criado (Windows). Nota: É necessário estar com o venv ativado para rodar comandos ``python``:
```bash
.\venv\Scripts\activate
```

### V. Liste os containers disponíveis
Para identificar o container Docker onde a aplicação será executada:
```bash
make runcontainer
```
Ou
```bash
python .\containers.py
```
Ou acesse o Portainer e copie o UUID do container desejado.

### VI. Configure o container no .env
No arquivo .env, defina a variável CONTAINER com o UUID obtido:

### VII. Execute o processo principal (main.py)
Com tudo pronto, execute:
```bash
make runmain
```
Ou
```bash
python .\main.py
```
