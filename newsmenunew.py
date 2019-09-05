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
        "Editorials/Articles", "Read editorials and articles")
    command_item_eds_hindu = CommandItem("The Hindu", "node index eds hindu")
    command_item_eds_et = CommandItem("Economic Times", "node index eds et")
    command_item_eds_ie = CommandItem("Indian Express", "node index eds ie")
    command_item_eds_hbl = CommandItem(
        "Hindu Business Line", "node index eds hbl")
    command_item_eds_economist = CommandItem(
        "Economist", "node index eds economist")
    command_item_eds_guardian = CommandItem(
        "Guardian", "node index eds guardian")
    command_item_eds_projsyn = CommandItem(
        "Project Syndicate", "node index projsyn all")
    submenu_editorials.append_item(command_item_eds_hindu)
    submenu_editorials.append_item(command_item_eds_et)
    submenu_editorials.append_item(command_item_eds_ie)
    submenu_editorials.append_item(command_item_eds_hbl)
    submenu_editorials.append_item(command_item_eds_economist)
    submenu_editorials.append_item(command_item_eds_guardian)
    submenu_editorials.append_item(command_item_eds_projsyn)
    menu_submenu_editorials = SubmenuItem(
        "Editorials/Articles", submenu=submenu_editorials)
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

    # Commands for Management/Startups
    submenu_mgmt = ConsoleMenu(
        "Management/Startups", "Leadership in a gist...")
    command_item_mgmt_hbr = CommandItem(
        "Harvard Business Review", "node index hbr latest")
    # command_item_mgmt_ys = CommandItem("YourStory-Social", "node index yourstory social")
    submenu_mgmt.append_item(command_item_mgmt_hbr)
    # submenu_mgmt.append_item(command_item_mgmt_ys)
    menu_submenu_mgmt = SubmenuItem(
        "Management/Startups", submenu=submenu_mgmt)
    menu_submenu_sports.set_menu(menu)
    menu.append_item(menu_submenu_mgmt)

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
