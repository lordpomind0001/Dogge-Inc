
class Embed:
    def create_embed(self, title, description, color, fields=None, footer=None, image_url=None):
        """
        Create an embed structure for Discord.

        Parameters:
        title (str): The title of the embed.
        description (str): The description of the embed.
        color (int): The color code of the embed.
        fields (list of dict): A list of fields to include in the embed.
        footer (dict): The footer information.
        image_url (str): The URL of the image to include in the embed.

        Returns:
        dict: The embed structure.
        """
        embed = {
            'title': title,
            'description': description,
            'color': color,
            'fields': fields if fields else [],
            'footer': footer if footer else {},
            'image': {'url': image_url} if image_url else {}
        }
        return embed
  
