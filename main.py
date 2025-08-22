from dotenv import load_dotenv
import os
from conn import client
from translation import translate
from loguru import logger

load_dotenv()

container = os.getenv('CONTAINER')

def process(folder):
  logger.info(f"📂 Acessando pasta: {folder}")
  stdin, stdout, stderr = client.exec_command(f'sudo docker exec {container} ls -1 {folder}')
  files = [f.strip() for f in stdout.read().decode().splitlines()]
  error = stderr.read().decode().strip()

  if error:
    logger.critical(f"❌ Falha ao acessar arquivos na pasta {folder}: {error}")
    return

  for filename in files:
    path = f"{folder}/{filename}"
    logger.info(f"🔄 Processando arquivo: {filename}")

    check_cmd = f"sudo docker exec {container} stat -c %s {path}"
    stdin, stdout, stderr = client.exec_command(check_cmd)
    size_output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    if error:
      logger.error(f"❌ Erro ao verificar tamanho do arquivo {filename}: {error}")
      continue

    if size_output == '0':
      logger.warning(f"⚠️  Arquivo {filename} está vazio. Ignorando.")
      continue

    stdin, stdout, stderr = client.exec_command(f"sudo docker exec {container} cat {path}")
    original = stdout.read().decode()
    error = stderr.read().decode().strip()

    if error:
      logger.error(f"❌ Erro ao ler o arquivo {filename}: {error}")
      continue

    if not original.strip():
      logger.warning(f"⚠️  {filename} aparentemente vazio após leitura. Ignorando.")
      continue

    if original:
      logger.info(f"📄 Conteúdo original de {filename}:\n{original}")

    translated = translate(original)
    stdin, stdout, stderr = client.exec_command(f"sudo docker exec -i {container} sh -c 'cat > {path}'")
    stdin.write(translated)
    stdin.channel.shutdown_write()
    error = stderr.read().decode().strip()

    if error:
      logger.error(f"❌ Erro ao sobrescrever {filename}: {error}")
      continue

    logger.success(f"📄 Arquivo {filename} traduzido e sobrescrito com sucesso.")


folders = [
  '/app/app/views/devise/mailer',
  '/app/app/views/mailers/administrator_notifications/account_compliance_mailer',
  '/app/app/views/mailers/administrator_notifications/account_notification_mailer',
  '/app/app/views/mailers/administrator_notifications/channel_notifications_mailer',
  '/app/app/views/mailers/administrator_notifications/integrations_notification_mailer',
  '/app/app/views/mailers/agent_notifications/conversation_notifications_mailer',
  '/app/app/views/mailers/conversation_reply_mailer',
  '/app/app/views/mailers/team_notifications/automation_notification_mailer',
]

# Grandes ciclos de preço ocorrem a cada 3 anos
# Bezerro caro (carne vai ficar cara)
# Bezerro dando dinheiro > Não mata as vacas, procria elas (segurar matriz)
# Frigorífico compra vaca e boi > menos vaca, aumento no preço da @ boi
# Boi sendo mais caro, usa mais os bezerros, cai de preço
# Bezerro barato (carne vai ficar barata)
# Cria das vacas nn compensam, ent descarta vaca, diminui os bezzeros, aumenta o preço

for folder in folders:
  process(folder)

client.close()
