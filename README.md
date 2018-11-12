Copyright: Arthur Milchior <arthur@milchior.fr>
Based on anki code by Damien Elmes <anki@ichi2.net>
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in https://github.com/Arthur-Milchior/anki-relation
Initially requested on https://www.reddit.com/r/Anki/comments/9vjnpv/addon_idea_manually_marking_notes_as_related/

Allow to create a new of relations between notes. Burying sibling cards will now also bury cards of related note. This only work on computer, not on ios, android or ankiweb.

To «relate» notes, in the browser, select each note you want in your new relation, and then press Ctrl+m (or notes>create a relation). A new relation will be created.

To delete a relation r, just delete the tag relation_r.

To see all cards related to some note, select this note in the browser, and do (note>see related notes), or Ctrl+r.

##Notes in multiple relations
A note may belong to multiple relation. If a card of this note is seen, all cards of all of its relations will be buried. If you select a card belonging to three relations and then click on merge, the three relations will be merged.




###Configuration
Two notes are related if they have a tag of the form relation_xxxxxxxx, with the same value for xxxxx. You can change "relation_" to any other prefix in the add-ons configuration. By default, xxxxx is a random value. You can choose a meaningful value. In athe add-ons configuration switch "query relation name" to true, then when you create a relation, anki will prompt you to enter the relation's name.

###TODO

When synchronising on the computer, look at card seen today, and bury their related cards. (I don't think I'll ever do it).

Add a button to remove notes from relation.

Add an option to add a single card to a relation, instead of an entire note.

If you want to merge multiple relations into a single one, select at least one note from each relation and click on (note >merge the selected relations). If a note has no relation, it will just be added to this new relation.

