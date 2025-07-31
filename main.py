from conn import client
# from containers import list_containers

# list_containers()

container = '3766b3d37.........'

stdin, stdout, stderr = client.exec_command(f'sudo docker exec {container} ls -1 /app/app/views/devise/mailer')
files = [f.strip() for f in stdout.read().decode().splitlines()]
error = stderr.read().decode().strip()
if error:
  print("❌ Error:", error)

for filename in files:
  path = f"/app/app/views/devise/mailer/{filename}"
  print(f"\n-> Processing {filename}")
  
  cin, cout, cerr = client.exec_command(f"sudo docker exec {container} cat {path}")
  original = cout.read().decode()
  error = cerr.read().decode().strip()
  if error:
    print(f"  ❌ Falha ao ler {filename}:", error)
    continue
  print(original)

client.close()
