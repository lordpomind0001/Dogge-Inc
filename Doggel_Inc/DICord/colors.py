class Color:
    def __init__(self):
        self.colors = {
            'default': 0x000000,
            'aqua': 0x1ABC9C,
            'dark_aqua': 0x11806A,
            'green': 0x57F287,
            'dark_green': 0x1F8B4C,
            'blue': 0x3498DB,
            'dark_blue': 0x206694,
            'purple': 0x9B59B6,
            'dark_purple': 0x71368A,
            'luminous_vivid_pink': 0xE91E63,
            'dark_vivid_pink': 0xAD1457,
            'gold': 0xF1C40F,
            'dark_gold': 0xC27C0E,
            'orange': 0xE67E22,
            'dark_orange': 0xA84300,
            'red': 0xED4245,
            'dark_red': 0x992D22,
            'grey': 0x95A5A6,
            'dark_grey': 0x979C9F,
            'darker_grey': 0x7F8C8D,
            'light_grey': 0xBCC0C0,
            'navy': 0x34495E,
            'dark_navy': 0x2C3E50,
            'yellow': 0xFFFF00,
            'white': 0xFFFFFF,
            'blurple': 0x5865F2,
            'greyple': 0x99AAb5,
            'dark_but_not_black': 0x2C2F33,
            'not_quite_black': 0x23272A,
            'fuchsia': 0xEB459E
        }

    def get(self, color_name):
        """
        Get the hexadecimal color code for a given color name as supported by Discord.

        Parameters:
        color_name (str): The name of the color.

        Returns:
        int: The hexadecimal color code.
        """
        return self.colors.get(color_name.lower(), self.colors['default'])
