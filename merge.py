# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation

from .utils import *
from aqt.utils import tooltip

def createRelationBrowser(browser,relation=None):
    notes = getSelectedNotes(browser)
    createRelation(notes,relation)
    
def createRelation(notes,relation=None):
    """Create a new relation over those notes. """
    debug(f"Calling createRelations on {notes}")
    l=len(notes)
    # if l==0:
    #     return
    # if l==1:
    #     tooltip(f"You selected a single note, no relation created")
    #     return
    relation=createRelationName() if relation is None else relation
    for note in notes:
        debug(f"Adding relation {relation} to note {note.id}")
        note.addTag(relation)
        note.flush()
    tooltip(f"Relation {relation} created with {l} notes.")
    

        
def addNotesToRelations(notes):
    """If a single relation exists, add all notes to it. Return whether it works."""
    relations = getRelationsFromNotes(notes)
    l=len(relations)
    if l==1:
        relation=relations.pop()
        createRelation(notes,relation=relation)
        debug(f"A single relation is present in {notes}. All of their cards will be added to it.")
        return True
    elif l==0:
        debug(f"No relations are present in {notes}, thus new relations can't be added")
    else:
        debug(f"Multiple relations are present in {notes}, thus new relations can't be added")
    return False

def mergeRelations(browser):
    """All of those notes belong to a single relation.

    If at most one relation was present, then it is used.
    Otherwise, they are removed from all past relations and a new one is created."""
    selectedNotes = getSelectedNotes(browser)
    debug(f"Calling mergeRelations on {selectedNotes}")
    relations=getRelationsFromNotes(selectedNotes)
    relatedNotes = selectedNotes|getNotesFromRelations(relations)
    if len(relations)==1:
        debug(f"A single relation was found while merging {selectedNotes}, thus we add notes to it.")
        createRelation(selectedNotes,relation=relations.pop() )
        return
    debug(f"0 or many relation(s) was(were) found while merging {selectedNotes}, thus we delete those relations and create a new one..")
    for note in relatedNotes:
        for relation in relations:
            note.delTag(relation)
    createRelation(relatedNotes)

