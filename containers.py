from conn import client

def list_containers():
  _, stdout, stderr = client.exec_command('sudo ls -l /var/lib/docker/containers')

  output = stdout.read().decode().strip()
  error = stderr.read().decode().strip()

  if error:
    print("❌ Error:", error)
  else:
    print("✅ Output:", output)

list_containers()
