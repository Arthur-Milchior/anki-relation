# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation
# Addon number 413416269  https://ankiweb.net/shared/info/413416269
from aqt import mw

userOption = mw.addonManager.getConfig(__name__)
if userOption["current tag prefix"] not in userOption["tag prefixes"]:
    userOption["tag prefixes"].append(userOption["current tag prefix"])
    userOption["tag prefixes"]= userOption["tag prefixes"]
    mw.addonManager.writeConfig(__name__,userOption)
