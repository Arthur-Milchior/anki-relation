Allow to create a new kind of relations between notes.
Burying sibling cards will now also bury cards of related note.
This only work on computer, not on ios, android or ankiweb.

To «relate» notes, in the browser, select each note you want in your new relation, and then press Ctrl+Alt+E (or edit>create a relation).
A new relation will be created.

To delete a relation r, just delete the tag relation_r.

To see all cards related to some note, select this note in the browser, and do (edit>see related notes), or Ctrl+Alt+Shift+E.

## Notes in multiple relations
A note may belong to multiple relation. If a card of this note is seen, all cards of all of its relations will be buried.
If you select a card belonging to three relations and then click on merge, the three relations will be merged.

## Interaction with "Copy note"
You can use add-on
[1566928056](https://ankiweb.net/shared/info/1566928056) to copy
cards. You can configure the add-on in order that a note and its copy
get related.

### Configuration
Two notes are related if they have a tag of the form relation_xxxxxxxx, with the same value for xxxxx.
You can change "relation_" to any other prefix in the add-ons configuration. By default, xxxxx is a random value.
You can choose a meaningful value.
In athe add-ons configuration switch "query relation name" to true, then when you create a relation, anki will prompt you to enter the relation's name.

### TODO

When synchronising on the computer, look at card seen today, and bury their related cards. (I don't think I'll ever do it).

Add a button to remove notes from relation.

Add an option to add a single card to a relation, instead of an entire note.

If you want to merge multiple relations into a single one, select at least one note from each relation and click on (note >merge the selected relations).
If a note has no relation, it will just be added to this new relation.

Key         |Value
------------|-------------------------------------------------------------------
Copyright   |Arthur Milchior <arthur@milchior.fr>
Based on    |Anki code by Damien Elmes <anki@ichi2.net>
License     |GNU AGPL, version 3 or later; http|//www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-relation
Addon number| [413416269](https://ankiweb.net/shared/info/413416269)
Initially requested|h ttps://www.reddit.com/r/Anki/comments/9vjnpv/addon_idea_manually_marking_notes_as_related/
Debugged by |cjdduarte
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](https://Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
