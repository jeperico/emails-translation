from dotenv import load_dotenv
import os
from paramiko import SSHClient, AutoAddPolicy
from loguru import logger

load_dotenv()

try:
  client = SSHClient()
  client.set_missing_host_key_policy(AutoAddPolicy())

  client.connect(
    os.getenv('HOST_IP'),
    username=os.getenv('HOST_USER'),
    password=os.getenv('HOST_PASS')
  )

  logger.success("🔐 Conexão SSH estabelecida com sucesso.")

except Exception as e:
  logger.critical(f"❌ Falha ao conectar via SSH: {e}")
  raise SystemExit(1)
