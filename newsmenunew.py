import sys

from consolemenu import *
from consolemenu.items import *


def main():

    menu = ConsoleMenu("My News Reader", "Happy Reading !")

    # item1 = MenuItem("Management", menu)
    # item1 = MenuItem("Sports", menu)
    # item1 = MenuItem("Startups", menu)

    # Commands for Editorials
    submenu_editorials = ConsoleMenu(
        "Editorials", "Read editorials from Top news sites")
    command_item_eds_hindu = CommandItem("The Hindu", "node index eds hindu")
    command_item_eds_et = CommandItem("Economic Times", "node index eds et")
    command_item_eds_ie = CommandItem("Indian Express", "node index eds ie")
    command_item_eds_hbl = CommandItem(
        "Hindu Business Line", "node index eds hbl")
    command_item_eds_guardian = CommandItem(
        "Guardian", "node index eds guardian")
    submenu_editorials.append_item(command_item_eds_hindu)
    submenu_editorials.append_item(command_item_eds_et)
    submenu_editorials.append_item(command_item_eds_ie)
    submenu_editorials.append_item(command_item_eds_hbl)
    submenu_editorials.append_item(command_item_eds_guardian)
    menu_submenu_editorials = SubmenuItem(
        "Editorials", submenu=submenu_editorials)
    menu_submenu_editorials.set_menu(menu)
    menu.append_item(menu_submenu_editorials)

    # Commands for Sports
    submenu_sports = ConsoleMenu("Sports", "Read Sports Updates")
    command_item_sports_f1 = CommandItem("ESPN F1", "node index sports f1")
    command_item_sports_epl = CommandItem(
        "English Premier League", "node index sports epl")
    submenu_sports.append_item(command_item_sports_f1)
    submenu_sports.append_item(command_item_sports_epl)
    menu_submenu_sports = SubmenuItem("Sports", submenu=submenu_sports)
    menu_submenu_sports.set_menu(menu)
    menu.append_item(menu_submenu_sports)

    # Commands for Magazines
    submenu_magz = ConsoleMenu(
        "Magazines", "Good Reads from top magazine websites")
    command_item_magz_hbr = CommandItem(
        "Harvard Business Review", "node index magz hbr")
    command_item_magz_projsyn = CommandItem(
        "Project Syndicate", "node index magz projsyn")
    command_item_magz_economist = CommandItem(
        "The Economist", "node index magz economist")
    command_item_magz_atlantic = CommandItem(
        "The Atlantic", "node index magz atlantic")
    command_item_magz_newyorker = CommandItem(
        "The NewYorker", "node index magz newyorker")
    command_item_magz_frontline = CommandItem(
        "Frontline by Hindu", "node index magz frontline")
    submenu_magz.append_item(command_item_magz_hbr)
    submenu_magz.append_item(command_item_magz_projsyn)
    submenu_magz.append_item(command_item_magz_economist)
    submenu_magz.append_item(command_item_magz_atlantic)
    submenu_magz.append_item(command_item_magz_newyorker)
    submenu_magz.append_item(command_item_magz_frontline)
    menu_submenu_magz = SubmenuItem(
        "Magazines", submenu=submenu_magz)
    menu_submenu_magz.set_menu(menu)
    menu.append_item(menu_submenu_magz)

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
