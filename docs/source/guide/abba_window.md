# The ABBA window

The ABBA window is a [BigDataViewer](https://imagej.github.io/plugins/bdv/index) window, which displays big multiresolution images in a highly responsive way. It contains:

* a **menu bar**, with all ABBA commands (listed in the [Menu reference](../reference/menu_reference.md));
* the **viewer**, where the atlas and your slices are displayed;
* a **side panel** made of cards, with the display settings and the most frequent editing tools.

![The ABBA window: the menu bar, the viewer with the atlas sections and the registered demo slices, the cards on the right](/assets/abba/guide/abba_window/window.png)

## Navigate in the viewer

The BigDataViewer interface is quite different from the standard ImageJ display, so take some time to get familiar with the basic navigation controls:

* `hold and drag right-click`: pan across the image;
* `mouse wheel`: zoom in / out;
* `up / down keys`: zoom in / out;
* `shift + up / down key`: fast zoom in / out.

{menuselection}`View --> Navigate --> Center On Atlas` brings the atlas back in the middle of the window if you get lost. All shortcuts are listed in [Keyboard & mouse shortcuts](../reference/shortcuts.md).

## Atlas display

When ABBA starts, you see the atlas, sliced regularly along the slicing axis. The atlas is a multichannel image: depending on the atlas, its channels contain anatomical images (Nissl staining, autofluorescence...), the borders between regions, and the region labels. For the Allen Brain atlas CCFv3, the anatomical channels are a Nissl staining (channel 0) and an autofluorescence image (channel 1).

In the `Atlas Display` card, you can toggle each atlas channel on or off and adjust its visibility, to emphasize or de-emphasize each one. The settings are kept when you switch between the two display modes.

![The Atlas Display card, with the Nissl channel hidden](/assets/abba/guide/abba_window/atlas_display_card.png)

## Display modes

ABBA has two display modes, which you switch with the buttons of the `Display & Navigation` card, the {menuselection}`View --> Display Mode` menu or the right-click menu:

* The **positioning mode**, active when ABBA starts, displays all slices side by side along the atlas. It is used to sort the slices and position them along the slicing axis. In this mode, `Change Overlap Mode` (shortcut `O`) cycles through the ways slices are drawn relative to the atlas, and two sliders set how much they overlap.
* The **review mode** (shortcut `R`) displays one slice at a time, overlaid on the atlas. It is used to check and refine registrations.

![Review mode: the current slice over the atlas section at its position, the slice handles in a row above](/assets/abba/guide/abba_window/review_mode.png)

### Current slice

One slice is the **current slice**: it has a white circle around its handle, and it is the slice displayed in review mode. Use the left and right arrow keys, or the `Previous` and `Next` buttons of the `Display & Navigation` card, to change the current slice; `C` centers the view on it. The viewer shows its name, its position along the slicing axis and its registrations, top left, and the `Slices Display` card its name.

![The current slice in positioning mode: a white circle around its handle, and arrows above it; here no slice is selected, so all handles are yellow](/assets/abba/guide/abba_window/current_slice.png)

In the `Display & Navigation` card, `Display One Slice Only (fast)` hides all slices but the current one, which keeps the display responsive with many big slices, and `Display All Slices` shows them all again.

## The side panel cards

The side panel can be opened and closed with the small arrow at the right edge of the viewer, or with {menuselection}`View --> Cards`. Click the title of a card to expand or collapse it. It contains the following cards:

![The cards of the side panel, all collapsed](/assets/abba/guide/abba_window/cards.png)

| Card | Content |
|---|---|
| `Sources` | The list of the sources displayed by BigDataViewer (atlas channels and slices), collapsed at start. |
| `Atlas Information` | Name and details of the atlas used in the session. |
| `Atlas Display` | Visibility and display settings of the atlas channels. |
| `Slices Display` | The name of the current slice, and the table of all slices: selection, visibility, channels, colors and display ranges (see [Select & display slices](select_display_slices.md)). |
| `Display & Navigation` | Display modes, overlap settings in positioning mode, navigation between slices, and browsing of the registration steps of a slice. |
| `Edit Selected Slices` | Rotations and flips of the selected slices, and even spacing of the slices (see [Orient slices](orient_slices.md)). |
| `Atlas Slicing` | Slicing angles of the atlas (see [Position slices along the atlas](position_along_atlas.md)). |
| `Define Region Of Interest` | The rectangle of the atlas where registrations and exports are computed (see [Region of interest](#region-of-interest)). |

{menuselection}`View --> Cards --> Add Resources Monitor` adds a card that monitors memory and CPU usage, useful when many registrations run in parallel.

## The right-click menu

Right-click in the viewer to get a menu acting on the selected slices: set or remove key slices, hide or show slices, remove slices, edit or remove the last registration, undo and redo, and switch between the display modes.

## Undo and redo

Most actions can be undone with `Ctrl+Z` and redone with `Ctrl+Shift+Z` (or {menuselection}`Edit --> Undo` and {menuselection}`Edit --> Redo`): moving slices, registrations, key slices, rotations and flips, and edits of a registration. Loading a state cannot be undone.

## Mouse options

{menuselection}`Edit --> Configuration --> Mouse Options` displays, next to the mouse pointer, the atlas coordinates of the point under it, or information about the slice under it.

## Log

{menuselection}`View --> Log` opens a window that logs the slice events of the session (creation, deletion, actions), useful to report a problem.
