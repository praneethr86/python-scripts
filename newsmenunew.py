import sys

from consolemenu import *
from consolemenu.items import *


def main():

    menu = ConsoleMenu("My News Reader", "Happy Reading !")

    # Commands for Editorials
    submenu_editorials = ConsoleMenu(
        "Editorials/Columns", "Read editorials/columns from Top news sites")
    command_item_eds_hindu = CommandItem("The Hindu", "node index eds hindu")
    command_item_eds_hindulead = CommandItem(
        "The Hindu Lead Opinion", "node index eds hindulead")
    command_item_eds_et = CommandItem("Economic Times", "node index eds et")
    command_item_eds_ie = CommandItem("Indian Express", "node index eds ie")
    command_item_eds_ie_columns = CommandItem(
        "IndianExpress Columns", "node index eds iecolumns")
    command_item_eds_hbl = CommandItem(
        "Hindu Business Line", "node index eds hbl")
    command_item_eds_guardian = CommandItem(
        "Guardian", "node index eds guardian")
    command_item_eds_livemint = CommandItem(
        "LiveMint", "node index eds livemint")
    submenu_editorials.append_item(command_item_eds_hindu)
    submenu_editorials.append_item(command_item_eds_hindulead)
    submenu_editorials.append_item(command_item_eds_et)
    submenu_editorials.append_item(command_item_eds_ie)
    submenu_editorials.append_item(command_item_eds_ie_columns)
    submenu_editorials.append_item(command_item_eds_hbl)
    submenu_editorials.append_item(command_item_eds_guardian)
    submenu_editorials.append_item(command_item_eds_livemint)
    menu_submenu_editorials = SubmenuItem(
        "Editorials/Columns", submenu=submenu_editorials)
    menu_submenu_editorials.set_menu(menu)
    menu.append_item(menu_submenu_editorials)

    # Commands for Sports
    submenu_sports = ConsoleMenu("Sports", "Read Sports Updates")
    command_item_sports_f1_espn = CommandItem(
        "ESPN F1", "node index sports espnf1")
    command_item_sports_f1_autosport = CommandItem(
        "Autosport F1", "node index sports autof1")
    command_item_sports_epl = CommandItem(
        "English Premier League", "node index sports epl")
    submenu_sports.append_item(command_item_sports_f1_espn)
    submenu_sports.append_item(command_item_sports_f1_autosport)
    submenu_sports.append_item(command_item_sports_epl)
    menu_submenu_sports = SubmenuItem("Sports", submenu=submenu_sports)
    menu_submenu_sports.set_menu(menu)
    menu.append_item(menu_submenu_sports)

    # Commands for Tech News
    submenu_tech = ConsoleMenu("Tech", "Read Tech News")
    command_item_tech_techcrunch = CommandItem(
        "TechCrunch", "node index tech techcrunch")
    command_item_tech_tnw = CommandItem("TheNextWeb", "node index tech tnw")
    command_item_tech_readwrite = CommandItem(
        "ReadWrite", "node index tech readwrite")
    submenu_tech.append_item(command_item_tech_techcrunch)
    submenu_tech.append_item(command_item_tech_tnw)
    submenu_tech.append_item(command_item_tech_readwrite)
    menu_submenu_tech = SubmenuItem("Tech", submenu=submenu_tech)
    menu_submenu_tech.set_menu(menu)
    menu.append_item(menu_submenu_tech)

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
    command_item_magz_sciam = CommandItem(
        "Scientific American", "node index science sciam")
    command_item_magz_popsci = CommandItem(
        "Popular Science", "node index science popsci")
    submenu_magz.append_item(command_item_magz_hbr)
    submenu_magz.append_item(command_item_magz_projsyn)
    submenu_magz.append_item(command_item_magz_economist)
    submenu_magz.append_item(command_item_magz_atlantic)
    submenu_magz.append_item(command_item_magz_newyorker)
    submenu_magz.append_item(command_item_magz_frontline)
    submenu_magz.append_item(command_item_magz_sciam)
    submenu_magz.append_item(command_item_magz_popsci)
    menu_submenu_magz = SubmenuItem(
        "Magazines", submenu=submenu_magz)
    menu_submenu_magz.set_menu(menu)
    menu.append_item(menu_submenu_magz)

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
