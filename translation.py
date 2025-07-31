from googletrans import Translator
import asyncio

async def translate(text: str):
  google = Translator()
  result = await google.translate(text, dest='pt')
  print(result.text)

# TODO: Handle variables name to don't translate
# TODO: Transform into a exportable function
# TODO: Format the response
if __name__ == "__main__":
  asyncio.run(translate(
    '''<p>Hi {{user.available_name}},</p>

<p>
  Conversation #{{conversation.display_id}} in {{ inbox.name }} 
  has missed the SLA for resolution time under policy {{ sla_policy.name }}.
</p>

<p>
<a href="{{action_url}}">Please address immediately.</a>
</p'''))
