# Select & display slices

## Select slices

Most ABBA commands act on the **selected slices**. Each slice is represented by a round handle below the atlas, which is green when the slice is selected and yellow when it is not.

![Slices 3 to 7 selected: their handles are green and joined by a line, the handles of the other slices are yellow](/assets/abba/guide/select_display_slices/selected_slices.png)

There are two ways to select slices.

### Rectangle selection with the mouse

Draw rectangles around slice handles to select them. Modifier keys add or remove slices from the current selection:

* `hold and left-click`: draw a rectangle to select slices;
* `shift + hold and left-click`: add slices to the current selection;
* `ctrl + hold and left-click`: remove slices from the current selection.

:::{warning}
Press the modifier keys before drawing the rectangle, or they won't take effect.
:::

Here is a demonstration on the demo slices: a rectangle selects three slices, `shift + rectangle` adds three others, `ctrl + rectangle` removes one, and `ctrl + A` selects all slices.

![Selecting slices with rectangles in positioning mode: selected slices are green, the others yellow](/assets/abba/guide/select_display_slices/select_slices.gif)

### The slice table

You can also select slices in the table of the `Slices Display` card:

![The table of the Slices Display card, filtered by name with `10x_0`: the selected slices are the highlighted rows](/assets/abba/guide/select_display_slices/slices_table_filtered.png)

The selection behaves as in a standard table (`shift` to select a range, `ctrl` to toggle the selection of a single slice). Type a part of a slice name in `Filter by name`, above the table, to show only the matching slices: with many slices, this is the quickest way to find and select some of them.

Additional shortcuts:

* `ctrl + A`: select all slices;
* `ctrl + shift + A`: deselect all slices.

On macOS, use `cmd` instead of `ctrl`.

{menuselection}`Slices --> Select Slices` and {menuselection}`Slices --> Deselect Slices` select or deselect slices by their index.

## Display slices

To register slices, you need to see them well: show the channels that matter for the registration and adjust their contrast.

Slices are displayed with all their channels when they are imported. In the table of the `Slices Display` card, the header row acts on all the selected slices at once: toggle the visibility of each channel, and set its color and its minimum and maximum displayed values (pay attention to where you click in the column headers). Each row customizes the display of a single slice.

![All slices selected, with only their channel 0 (DAPI) shown and its display range set to 0 - 1185: crossed eyes for the hidden channels, the range in the colored cells](/assets/abba/guide/select_display_slices/slices_table_display.png)

{menuselection}`Slices --> Set Slices Display Range` sets the minimum and maximum displayed values of channels of all the selected slices at once.

:::{warning}
The display settings matter beyond the display: the images sent to DeepSlice are made with them. Avoid saturated images (see [DeepSlice](#deepslice)).
:::

(remove-unwanted-slices)=
## Remove unwanted slices

Multi-series files, like VSI files, may contain unwanted images: slide labels, macro or overview images. They are usually RGB images, easy to spot in the slice table.

To remove them, select them, then right-click in the viewer and choose `Remove Selected Slices`, or click {menuselection}`Slices --> Remove Slices`. Removing slices can be undone.

![The Slices menu, Remove Slices](/assets/abba/guide/select_display_slices/remove_slices_menu.png)

## Reorder channels

If your slices do not all have their channels in the same order, or if you want to drop some channels, {menuselection}`Slices --> Re-Index Slices channels` replaces each selected slice by a new one with the channels in the order you give (for instance `1,0` swaps the first two channels, `0,2` keeps the first and the third). The new slices keep the position and the registrations of the original ones.

(white-background)=
## Slices with a white background

By default ABBA works with fluorescent images: the background is mostly black, and when a slice needs to be extended outside of its bounds, it is filled with black. Brightfield images have a white background instead, and black out-of-bounds pixels cause dark edges in registrations and exports.

Click {menuselection}`Slices --> Set White Background` to fill the area outside the selected slices with another value: 255 for 8-bit or RGB images, 65535 for 16-bit images, or a slightly lower value matching your actual background, so that the bounds of the images are as little visible as possible.

![Setting a white background to slices](/assets/img/fiji_white_background_slice.png)

Left: default; middle: background too dim; right: correct background value. (Data taken from the DeepSlice example dataset.)

It is also recommended to increase the maximum displayed value of white-background slices, to 512 for instance, to dim them and get a transparency-like behavior over the atlas.
