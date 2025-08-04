from translate import Translator
from loguru import logger

def translate(text: str) -> str:
  if not text.strip():
    logger.warning("⚠️ Texto recebido está vazio ou em branco. Ignorando tradução.")
    return text

  try:
    translator = Translator(to_lang="pt-br")
    result = translator.translate(text)
    logger.success("🌍 Tradução concluída com sucesso.")

    return result

  except Exception as e:
    logger.error(f"❌ Erro durante tradução: {e}")
    logger.debug(f"Texto com falha na tradução: {text}")
    return text
