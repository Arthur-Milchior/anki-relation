# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation
# Addon number 413416269  https://ankiweb.net/shared/info/413416269
from aqt import mw

options = None
def readIfRequired():
    global options
    if options is None:
        options = mw.addonManager.getConfig(__name__) or dict()

def newConf(config):
    global options
    options = None

def getConfig(s = None, default = None):
    """Get the dictionnary of objects. If a name is given, return the
    object with this name if it exists.

    reads if required."""

    readIfRequired()
    if s is None:
        return options
    else:
        return options.get(s, default)

mw.addonManager.setConfigUpdatedAction(__name__,newConf)

if getConfig("current tag prefix") not in getConfig("tag prefixes"):
    getConfig("tag prefixes").append(getConfig("current tag prefix"))
    options["tag prefixes"] = getConfig("tag prefixes")
    mw.addonManager.writeConfig(__name__,options)
