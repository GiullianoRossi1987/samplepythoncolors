# coding = utf-8
# using namespace std


class ColorSystem(object):
    """
    That class contains the main data information to change ANSI codification of a string
    :cvar _foreground: A dict that contain the ANSI configuration of the letter on the text.
    :cvar _foreground_modes: Another dict to the letter ANSI configuration, but that contains options, not colors, 
                             options such as bold letter or inverse colors
    :cvar _backgrounds: That dict contain the color information for the background of the text.
    All the dicts and cvars have the 'default' option to return the text part with the standard codification.
    """

    _foreground = {
        "red": "\033[1;31m",
        "black": "\033[1;30m",
        "green": "\033[1;32m",
        "yellow": "\033[1;33m",
        "blue": "\033[1;34m",
        "default": "\033[0;0m",
        "purple": "\033[1;35m",
        "cyan": "\033[1;36m",
        "gray": "\033[1;37m",
        "dark-gray": "\033[1;90m",
        "white-red": "\033[1;91m",
        "white-green": "\033[1;92m",
        "white-yellow": "\033[1;93m",
        "white-blue": "\033[1;94m",
        "white-purple": "\033[1;95m",
        "white-cyan": "\033[1;96m",
        "white": "\033[1;97m"
    }

    _foreground_modes = {
        "bold": "\033[;1m",
        "reverse": "\033[;7m",
        "default": "\033[0;0m"
    }

    _backgrounds = {
        "black": "\033[1;40m",
        "red": "\033[1;41m",
        "green": "\033[1;42m",
        "yellow": "\033[1;43m",
        "blue": "\033[1;44m",
        "purple": "\033[1;45m",
        "cyan": "\033[1;46m",
        "gray": "\033[1;47m",
        "dark-gray": "\033[1;100m",
        "white-red": "\033[1;101m",
        "white-green": "\033[1;102m",
        "white-yellow": "\033[1;103m",
        "white-blue": "\033[1;104m",
        "white-purple": "\033[1;105m",
        "white-cyan": "\033[1;106m",
        "white": "\033[1;107m",
        "default": "\033[0;0m"
    }


    class ColorNotFound(KeyError):
        """
        if the color can't be found as a key from the dict option.
        """
        args: str = "That color '$color' don't exist in the system!"

        def __init__(self, *args):
            """
            Starts the error message that contain the error!
            """
            print(args)
            exit(1)
           

    class InvalidColorType(Exception):
        """
        At the verification, it  is used for the programming debug, if the option of the method 'check_valid_colors' have the
        invalid *type_color
        """
        args: object = "That type of color '$color_type' don't exists!"

        def __init__(self, *args):
            """
            Starts the error message that contain the error!
            """
            print(args)
            exit(1)

    @classmethod
    def check_valid_colors(cls, colors: str, type_color="foreground"):
        """
        Verify if a color is valid, if not raise the Exception cls.ColorNotFound
        """
        if type_color == "foreground":
            if colors not in cls._foreground.keys(): raise cls.ColorNotFound(colors+" is not a valid color!")
        elif type_color == "background":
            if colors not in cls._backgrounds.keys(): raise cls.ColorNotFound(colors + " is not a valid color!")
        elif type_color == "foreground-modes":
            if colors not in cls._foreground_modes.keys(): raise cls.ColorNotFound(colors + "is not a valid color!")
        else: raise cls.InvalidColorType(type_color)


    def set_color_to(self, txt: str, foreground="default", background="none", foreground_mode="none"):
        """
        :return: The colored text!
        """
        self.check_valid_colors(foreground)
        colored = self._foreground[foreground] + txt + self._foreground["default"]
        if background != "none": 
            self.check_valid_colors(background, "background")
            colored = self._backgrounds[background] + colored
            colored += self._backgrounds["default"]
        if foreground_mode != "none": 
            self.check_valid_colors(foreground_mode, "foreground-modes")
            colored = self._foreground_modes[foreground_mode] + colored
            colored += self._foreground_modes["default"]
        return colored



