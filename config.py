# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation

from main import mw

userOption = mw.addonManager.getConfig(__name__)
current_tag_prefix = userOption["current tag prefix"]
tag_prefixes = userOption["tag prefixes"]
query_relation_name = userOption["query relation name"]
if current_tag_prefix not in tag_prefixes:
    tag_prefixes.append(current_tag_prefix)
    userOption["tag prefixes"]= tag_prefixes
    mw.addonManager.writeConfig(__name__,userOption)
    
