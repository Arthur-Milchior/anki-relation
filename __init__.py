# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation

from anki.notes import Note
from aqt.utils import getOnlyText
from config import *
from anki.sched import Scheduler

def getRelationsFromNote(self):
    tags = set()
    for tag in self.tags:
        for prefix in tag_prefixes:
            if tag.startswith(prefix):
                tags.add(tag)#[len(prefix):])
                break
    return tags

def removeRelationsFromNote(self):
    for tag in self.tags:
        for prefix in tag_prefixes:
            if tag.startswith(prefix):
                self.delTag(tag)
                break
    

Note.getRelations=getRelationsFromNote
Note.removeRelations=removeRelationsFromNote

def getRelationsFromNotes(notes):
    tags = set()
    for note in notes:
        tags |= note.getRelations
    return tags
        
def createTag():
    """A tag, from current prefix and an id.

    Id is either a time stamp or asked to user"""
    timeId=str(intTime(1000))
    suffix=getOnlyText(_("Name of the relation:"), default=timeId) if query_relation_name else timeId
    return current_tag_prefix+suffix

def queryRelated(tags):
    return " or ".join([f"tag:{tag}" for tag in tags])

def createRelation(notes,tag=None):
    """Create a new relation over those notes. """
    tag=createTag() if tag is None else tag
    for note in notes:
        note.addTag(tag)

        
def addNotesToRelations(notes):
    """If a single relation exists, add all notes to it. Return whether it works."""
    tags = getRelationsFromNotes(notes)
    if len(tags)==1:
        tag=tags.pop()
        createRelation(notes,tag=tag)
        return True
    else:
        return False

def mergeRelations(notes):
    """All of those notes belong to a single relation

    if at most one relation was present, then it is used.
    Otherwise, they are removed from all past relations and a new one is created."""
    if addNotesToRelations(notes):
        return
    for note in notes:
        note.removeRelations()
    createRelation(notes)


def getCardFromRelation(relation):
    todo
    
#from anki/sched.py
def _burySiblings(self, card):
    """Also bury related cards"""
        toBury = []
        nconf = self._newConf(card)
        buryNew = nconf.get("bury", True)
        rconf = self._revConf(card)
        buryRev = rconf.get("bury", True)
        #######
        note = card.note()
        relations=note.getRelations()
        nids = {card.nid}
        for relation in relations:
            nids|= getCardFromRelation(relation)
        ###########
        # loop through and remove from queues
        for cid,queue in self.col.db.execute("""
select id, queue from cards where nid in ? and id!=?
and (queue=0 or (queue=2 and due<=?))""",
                list(nids), card.id, self.today):#nids instead of nid
            if queue == 2:
                if buryRev:
                    toBury.append(cid)
                # if bury disabled, we still discard to give same-day spacing
                try:
                    self._revQueue.remove(cid)
                except ValueError:
                    pass
            else:
                # if bury disabled, we still discard to give same-day spacing
                if buryNew:
                    toBury.append(cid)
                try:
                    self._newQueue.remove(cid)
                except ValueError:
                    pass
        # then bury
        if toBury:
            self.col.db.execute(
                "update cards set queue=-2,mod=?,usn=? where id in "+ids2str(toBury),
                intTime(), self.col.usn())
            self.col.log(toBury)

Scheduler._burySiblings=_burySiblings
