from translate import Translator

def translate(text: str):
  translatorPt = Translator(to_lang="pt-br")
  result = translatorPt.translate(text)
  
  return result
