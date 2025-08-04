pysetup:
	@echo "🐍 Configurando ambiente Python..."
	python3 -m venv venv
	. venv/Script/activate && pip install --upgrade pip
	. venv/Script/activate && pip install -r requirements.txt

runcontainer:
	@echo "📦 Listando containers Docker..."
	. venv/Script/activate && python .\containers.py

runmain:
	@echo "🚀 Executando script principal..."
	. venv/Script/activate && python .\main.py

clean:
	@echo "🧹 Limpando ambiente virtual..."
	rm -rf venv
