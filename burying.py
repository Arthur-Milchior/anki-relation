# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation


#from anki/sched.py
from anki.utils import ids2str, intTime
from anki.sched import Scheduler
from .utils import *

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
            self.col.db.execute(
                "update cards set queue=-2,mod=?,usn=? where id in "+ids2str(toBury),
                intTime(), self.col.usn())
            self.col.log(toBury)
        else:
            print("nothing to bury")

Scheduler._burySiblings=_burySiblings
