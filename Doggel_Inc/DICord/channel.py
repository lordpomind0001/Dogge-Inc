class Channel:
  def __init__(self, channel_id, client):
    self.id = channel_id
    self.client = client
    self.session = client.session

  async def send(self, content, embed=None, reference=None):     
    url = f'https://discord.com/api/v6/channels/{self.id}/messages'
    headers = {
      'Authorization': f'Bot {self.client.token}',
      'Content-Type': 'application/json',
    }
    payload = {
      'content': content,
      'message_reference': {'message_id': reference} if reference else None
    }
    if embed is not None:
      payload['embed'] = embed
    async with self.session.post(url, headers=headers, json=payload) as response:
      return await response.json()
