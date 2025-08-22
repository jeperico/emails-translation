from pathlib import Path
from loguru import logger

def process(folder, recursive=False):
  folder = '.' + folder
  p = Path(folder)
  
  if not p.exists():
    logger.error(f"Folder {folder} does not exist.")
    return
  if not p.is_dir():
    logger.error(f"Path {folder} is not a directory.")
    return
  
  files = p.rglob('*') if recursive else p.iterdir()
  
  for entry in files:
    if not entry.is_file():
      continue
    try:
      with entry.open('r', encoding='utf-8', errors='replace') as f:
        content = f.read()
        logger.info(f"Processed {entry}")
    except Exception as e:
      logger.error(f"Error processing {entry}: {e}")


folders = [
  '/views/devise/mailer',
  '/views/mailers/administrator_notifications/account_compliance_mailer',
  '/views/mailers/administrator_notifications/account_notification_mailer',
  '/views/mailers/administrator_notifications/channel_notifications_mailer',
  '/views/mailers/administrator_notifications/integrations_notification_mailer',
  '/views/mailers/agent_notifications/conversation_notifications_mailer',
  '/views/mailers/conversation_reply_mailer',
  '/views/mailers/team_notifications/automation_notification_mailer',
]

for folder in folders:
  process(folder)
