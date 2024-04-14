import os
import sys
import io
import logging

import yaml
import pandas as pd
import tabulate
import bs4

import zjuintl_assistant
import util


def list_due_assignments(assist: zjuintl_assistant.Assistant):
    """
    List due assignments
    """
    items = assist.get_due_assignments()

    for item in items:
        print(
            str(item.date) + "\t" +
            item.course + "\t\t" +
            item.title
        )
    

def list_grades(assist: zjuintl_assistant.Assistant):
    """
    List grades
    """
    
    items = assist.get_bb_grades(20)

    print("Showing the last 20 grades")

    for item in items:
        print(
            str(item.date) + "\t" +
            item.course + "\t\t" +
            item.title + "\t" +
            str(item.pointsPossible) + "\t" +
            item.grade
        )


def list_announcements(assist: zjuintl_assistant.Assistant):
    """
    List announcements
    """

    items = assist.get_bb_announcements(20)

    print("Showing the last 20 announcements")

    for item in items:
        print(item.date, item.course, item.title)
        if item.html_content:
            soup = bs4.BeautifulSoup(item.html_content, "html.parser")
            for element in soup.children:
                if element.name in ["p", "h1", "h2", "h3", "h4", "h5", "h6"]:
                    print(element.get_text())
                elif element.name == "table":
                    df = pd.read_html(io.StringIO(str(element)))[0]
                    print(tabulate.tabulate(df, tablefmt='simple_grid', showindex=False))
        print()
            


def quit(_: zjuintl_assistant.Assistant):
    """
    Quit
    """

    sys.exit(0)

MENU = """Input a number and press Enter
1. List Due Assignments
2. List Grades
3. List Announcements
4. Quit
"""
FUNCTIONS = [
    None,
    list_due_assignments,
    list_grades,
    list_announcements,
    quit
]


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if os.environ.get("DEBUG"):
        logging.getLogger("assistant").setLevel(logging.DEBUG)

    if not os.path.exists("config.yaml"):
        with open("config.yaml", "w") as f:
            f.write("username: \npassword: \n")
        print("Please fill in your username and password in config.yaml")
        input("Press Enter to exit ...")
        sys.exit(0)
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
        try:
            if not config["username"] or not config["password"]:
                print("Please fill in your username and password in config.yaml")
                input("Press Enter to exit ...")
                sys.exit(0)
        except KeyError:
            print("Please fill in your username and password in config.yaml")
            input("Press Enter to exit ...")
            sys.exit(0)

    assist = zjuintl_assistant.Assistant(config["username"], config["password"])

    while True:
        print()
        try:
            choice = int(input(MENU))
            if choice < 1 or choice >= len(FUNCTIONS):
                print(f"Please input a number between 1 and {len(FUNCTIONS)-1}")
                continue
        except ValueError:
            print("Please input a integer")
            continue
        util.clear_display()
        FUNCTIONS[choice](assist)
