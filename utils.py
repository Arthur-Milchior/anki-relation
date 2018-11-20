# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation
# Addon number 413416269  https://ankiweb.net/shared/info/413416269

from .config import userOption
from aqt.utils import getOnlyText, askUser
from anki.utils import intTime
from anki.find import Finder
from anki.notes import Note
from aqt import mw

def debug(s):
    print(s)
    pass

def getRelationsFromNote(self):
    relations = set()
    for relation in self.tags:
        for prefix in userOption["tag prefixes"]:
            if relation.startswith(prefix):
                relations.add(relation)#[len(prefix):])
                break
    debug(f"The relations from note {self.id} are {relations}")
    return relations

def removeRelationsFromNote(self):
    for tag in self.tags:
        for prefix in userOption["tag prefixes"]:
            if tag.startswith(prefix):
                self.delTag(tag)
                debug(f"Removing tag {tag} from note {self.id}")
                break
    

Note.getRelations=getRelationsFromNote
Note.removeRelations=removeRelationsFromNote

def getRelationsFromNids(nids):
    notes=[Note(mw.col,id=nid) for nid in nids]
    return getRelationsFromNotes(notes)
def getRelationsFromNotes(notes):
    relations = set()
    for note in notes:
        relations |= note.getRelations()
    debug(f"The relations from notes {notes} are {relations}")
    return relations
        
def createRelationName(browser):
    """A tag, from current prefix and an id. Or None

    Id is either a time stamp or asked to user.
    None if the user cancel.
    """
    timeId=str(intTime(1000))
    while True:
        if userOption["query relation name"]:
            suffix=getOnlyText(_("Name of the relation:"), default=timeId)
            if suffix=="":
                return None
        else:
            suffix=timeId
        relation = userOption["current tag prefix"]+suffix
        if len(getNidsFromRelation(relation))>0:
            confirm= askUser(f"A relation called {relation} already exists. Do you want to add the selected notes to this relation ?", defaultno=True, parent=browser)
            if confirm is True:
                break
        else:
            break
    debug(f"The new relation name is {relation}")
    return relation

def queryRelated(relations):
    query =" or ".join([f"tag:{relation}" for relation in relations])
    debug(f"Query from relations {relations} is {query}")
    return query 

def getNidsFromRelation(relation):
    nids=getNidsFromRelations([relation])
    debug(f"from relation {relation} we get nids {nids}")
    return  nids

def getNotesFromRelation(relation):
    notes={Note(mw.col, id=nid) for nid in getNidsFromRelation(relation)}
    debug(f"from relation {relation} we get notes {notes}")
    return nids

def getNidsFromRelations(relations):
    finder = Finder(mw.col)
    nids= set(finder.findNotes(queryRelated(relations)))
    debug(f"from relations {relations} we get nids {nids}")
    return nids
def getNotesFromRelations(relations):
    notes={Note(mw.col, id=nid) for nid in getNidsFromRelations(relations)}
    debug(f"from relations {relations} we get notes {notes}")
    return notes

def getSelectedNotes(browser):
        nids=browser.selectedNotes()
        debug(f"Selected nids are {nids}")
        notes={Note(mw.col,id=nid) for nid in nids}
        debug(f"Selected notes are {notes}")
        return notes
