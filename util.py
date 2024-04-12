import os

def clear_display():
    """
    Clear the display
    """

    os.system("cls" if os.name == "nt" else "clear")
