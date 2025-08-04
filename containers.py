from conn import client
from loguru import logger

def list_containers():
  logger.info("📦 Buscando UUIDs dos containers Docker...")

  stdin, stdout, stderr = client.exec_command('sudo ls -l /var/lib/docker/containers')

  output = stdout.read().decode().strip()
  error = stderr.read().decode().strip()

  if error:
    logger.error("❌ Não foi possível obter os UUIDs dos containers.")
    logger.debug(f"Detalhes do erro: {error}")
  else:
    logger.success("✅ UUIDs dos containers obtidos com sucesso.")
    logger.debug(f"Resultado:\n{output}")
    print(output)

list_containers()
