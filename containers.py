from conn import client
from loguru import logger

def list_containers():
  _, stdout, stderr = client.exec_command('sudo ls -l /var/lib/docker/containers')

  output = stdout.read().decode().strip()
  error = stderr.read().decode().strip()

  if error:
    logger.error("Can't get container's uuids:")
    print(error)
  else:
    logger.success("Here is yours container's uuids")
    print(output)

list_containers()
