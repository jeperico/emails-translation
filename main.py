from dotenv import load_dotenv
import os
from conn import client
from translation import translate

load_dotenv()

container = os.getenv('CONTAINER')

def process(folder):
  stdin, stdout, stderr = client.exec_command(f'sudo docker exec {container} ls -1 {folder}')
  files = [f.strip() for f in stdout.read().decode().splitlines()]
  error = stderr.read().decode().strip()
  if error:
    print("\n❌ Error: ", error)

  for filename in files:
    path = f"{folder}/{filename}"
    print(f"\n⏳ Processando {filename}")
    
    check_cmd = f"sudo docker exec {container} stat -c %s {path}"
    stdin, stdout, stderr = client.exec_command(check_cmd)
    size_output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    if error:
      print(f"\n❌ Falha ao verificar tamanho de {filename}:", error)
      continue

    if size_output == '0':
      print(f"\n📄 {filename} está vazio. Ignorando.")
      continue

    stdin, stdout, stderr = client.exec_command(f"sudo docker exec {container} cat {path}")
    original = stdout.read().decode()
    error = stderr.read().decode().strip()

    if error:
      print(f"\n❌ Falha ao ler {filename}:", error)
      continue
    print(f"\n📜 Conteúdo do arquivo: \n{original}")

    if translate == '':
      print('\n📄 Arquivo vazio')
      continue
    translated = translate(original)
    stdin, stdout, stderr = client.exec_command(f"sudo docker exec -i {container} sh -c 'cat > {path}'")
    stdin.write(translated)
    stdin.channel.shutdown_write()
    error = stderr.read().decode().strip()
    if error:
      print(f"\n❌ Falha ao sobrescrever {filename}:", error)
      continue
    print('\n🌍 Arquivo traduzido com sucesso')


process('/app/app/views/devise/mailer')
process('/app/app/views/mailers/administrator_notifications/account_compliance_mailer')
process('/app/app/views/mailers/administrator_notifications/account_notification_mailer')
process('/app/app/views/mailers/administrator_notifications/channel_notifications_mailer')
process('/app/app/views/mailers/administrator_notifications/integrations_notification_mailer')
process('/app/app/views/mailers/agent_notifications/conversation_notifications_mailer')
process('/app/app/views/mailers/conversation_reply_mailer')
process('/app/app/views/mailers/team_notifications/automation_notification_mailer')

client.close()
