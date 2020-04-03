Allow the user to create a new kind of relation between notes.
Burying sibling cards will now also bury cards of any related notes.
This add-on only works on Anki desktop, not on iOS, Android or AnkiWeb.

### Using this add-on
**Create a relation:** in the browser, select each note you want in your new relation.
Then either press `Ctrl+Alt+E` or select `Edit>create a relation`.
A new relation will be created and can be seen in the Tags of each Card.

**Delete a relation:** to delete relation `r`, just delete the tag `relation_r` (or `customPrefix_r` if you've changed the default settings.)
This can be done with the `Backspace` key in the Tags field.

**See relations:** select a note in the browser. Then either press `Ctrl+Alt+Shift+E` or select `Edit>see related notes` to see only the notes it is related to.

### Configuration
Two notes are related if they have a tag of the form `relation_xxxxxxxx`, with the same value for `xxxxx`.
You can change `relation_` to any other prefix in the add-ons configuration. By default, `xxxxx` is a generated value.
If you'd like, you can choose a meaningful value.
In the add-on's configuration switch `query relation name` to true, then when you create a relation, anki will prompt you to enter the relation's name.

### Notes on multiple relations
A note may belong to multiple relations. If a card of this note is seen, all the cards of all of its relations will be buried.
If you select a card belonging to three relations and then click on merge, the three relations will be merged.

### Interaction with "Copy note"
The [Copy notes (1566928056)](https://ankiweb.net/shared/info/1566928056) add-on is used to, well, copy notes.
It can be configured so that when a note is copied, a relation between the two is created automatically.

### TODO

When synchronising on the computer, look at cards seen today, and bury their related cards. (I don't think I'll ever do it).

Add a button to remove notes from relation.

Add an option to add a single card to a relation, instead of an entire note.

If you want to merge multiple relations into a single one, select at least one note from each relation and click on (note >merge the selected relations).
If a note has no relation, it will just be added to this new relation.

Key         |Value
------------|-------------------------------------------------------------------
Copyright   |Arthur Milchior <arthur@milchior.fr>
Based on    |Anki code by Damien Elmes <anki@ichi2.net>
License     |GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-relation
Addon number| [413416269](https://ankiweb.net/shared/info/413416269)
Initially requested|https://www.reddit.com/r/Anki/comments/9vjnpv/addon_idea_manually_marking_notes_as_related/
Debugged by |cjdduarte
