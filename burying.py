# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation
# Addon number 413416269  https://ankiweb.net/shared/info/413416269

#from  anki/sched.py  and anki/schedv2.py 
from anki.utils import ids2str, intTime
from anki.sched import Scheduler
from anki.schedv2 import Scheduler as Scheduler2
from .utils import getNidsFromRelation, debug

def _burySiblingsAux(self, card,V1):
        """Also bury related cards"""
        debug(f"calling _burySiblings({card},{V1})\n")
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
            nids|= getNidsFromRelation(relation)
        # loop through and remove from queues
        query=f"""
        select id, queue from cards where (nid in {ids2str(nids)}) and id!={card.id}
        and (queue=0 or (queue=2 and due<={self.today}))"""#nids instead of nid
        print(f"query is {query}")
        for cid,queue in self.col.db.execute(query):
        ###########
            debug(f"The query retuned {cid}, {queue}")
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
            print(f"Burying {toBury}")
            if V1:
                    self.col.db.execute(
                            "update cards set queue=-2,mod=?,usn=? where id in "+ids2str(toBury),
                            intTime(), self.col.usn())
                    self.col.log(toBury)
            else:#V2
                    self.buryCards(toBury, manual=False)
                    
        else:
            print("nothing to bury")
Scheduler._burySiblings=(lambda self,card: _burySiblingsAux(self, card,True))
Scheduler2._burySiblings=(lambda self,card: _burySiblingsAux(self, card,False))
