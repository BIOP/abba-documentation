# Position slices along the atlas

Once the slices are [oriented](orient_slices.md), two things must be estimated before registering them in plane:

* the position of each slice along the slicing axis ("Z") of the atlas;
* the slicing angles of the atlas, to match the cutting angle of your sections.

This can be done manually, or automatically with DeepSlice for coronal sections of mouse and rat brains.

Since the slicing angle applies to all slices, register one animal at a time.

## Manual positioning

All manual positioning is done in positioning mode, where the slices are displayed side by side below the atlas.

### Drag selected slices

If your slices are not sorted correctly along the atlas, select the slices that are out of place and drag their handles along the axis. You can create gaps between slices to make room for others.

![Drag slices along axis](/assets/gif/fiji_slices_drag.gif)

### Distribute spacing between selected slices

To space the selected slices evenly, click `Distribute Spacing` in the `Edit Selected Slices` card, press `D`, or click {menuselection}`Slices --> Distribute Slices`. This can be undone with `ctrl + Z`:

![The atlas row and, below it, a small square for the position of each slice: top, as positioned by DeepSlice; bottom, after Distribute Spacing on all slices](/assets/abba/guide/position_along_atlas/distribute_spacing.png)

When no slice is a key slice (explained below), the first and last selected slices keep their position.

### Key slices

A recommended workflow to position slices along the atlas is:

* sort the slices along the axis;
* display the atlas with a coarse spacing (every 500 micrometers, the default, see the picture below) and drag the slices to their approximate position;
* zoom in, and match precisely a slice with easily recognizable features to the atlas;
* set this slice as a **key slice**: select it alone, right-click and choose `Set as Key Slice(s)`;
* position a few other slices precisely and set them as key slices;
* adjust the atlas slicing angles and check all slices;
* use `Distribute Spacing` to space the other slices evenly between the key slices.

![The atlas row with `Displayed slicing` at 10 atlas steps (a section every 100 micrometers, top) and at 50, the default (every 500 micrometers, bottom): set it in the `Atlas Display` card](/assets/abba/guide/position_along_atlas/displayed_slicing.png)

:::{note}
The displayed slicing of the atlas does not affect the registration. Internally, slices are positioned with a precision of 10 micrometers, the highest resolution of the atlas.
:::

![Finding correspondence and key slice](/assets/gif/fiji_atlas_drag_then_key.gif)

Key slices keep their position along the axis when other slices are dragged or distributed: the slices between two key slices are stretched along the axis while keeping their spacing ratio. You can still drag a key slice itself if you need to move it. Two or three key slices, usually the ones with the most recognizable features, are typically enough.

![A key slice: its handle is larger than the others, and a magenta square marks its position on the slicing axis](/assets/abba/guide/position_along_atlas/key_slice.png)

### Check positions in review mode

The positioning mode makes moving slices easy, but is not ideal to compare a section with the atlas. Switch to review mode (`R`) to display one slice at a time overlaid on the atlas, and browse the slices with the left and right arrow keys. You can switch back to the positioning mode at any time to correct a position.

![Review mode: a slice over the atlas section at its position, here after DeepSlice](/assets/abba/getting_started/first_registration/05_review_after_deepslice.png)

## Correct the atlas slicing angles

The `Atlas Slicing` card contains two sliders to adjust the slicing angles of the atlas:

![The Atlas Slicing card, with the angles found by DeepSlice for the demo slices](/assets/abba/guide/position_along_atlas/atlas_slicing_card.png)

Use slices with easily identifiable features to set the slicing angles.

:::{note}
The atlas slicing angles are the same for all sections: you can tilt the atlas, but you cannot "bend" it.
:::

<!-- TODO GIF phase: re-record dragging slices and setting a key slice with ABBA 0.24.1 and the demo slices. -->

(deepslice)=
## Automated positioning with DeepSlice

[DeepSlice](https://www.deepslice.com.au) ([publication](https://doi.org/10.1038/s41467-023-41645-4)) is a deep-learning tool that aligns whole mouse or rat brain histological sections to an atlas. In ABBA, it automates:

* the estimation of the atlas slicing angles;
* the initial positioning of slices along the slicing axis;
* a first in-plane affine registration (no deformation beyond an affine transformation).

The alignment is then refined with the [in-plane registrations](inplane_registration.md).

:::{note}
DeepSlice only works with the adult mouse Allen Brain atlas and the Waxholm rat atlas, in coronal orientation. With other atlases or orientations, the DeepSlice menu entry is not shown.
:::

:::{warning}
* DeepSlice needs **correctly oriented slices, all flipped the same way**: see [Orient slices](orient_slices.md).
* For best results, use DeepSlice on slices of a single animal: the same slicing angle correction applies to all slices.
* **Avoid saturated pixels!** DeepSlice works on 8-bit RGB images, made from your slices with their current display settings (color, minimum and maximum). Images that are too dark or too bright are badly registered: adjust the display settings first (see [Display slices](select_display_slices.md#display-slices)).
:::

To run DeepSlice, select the slices to register and click {menuselection}`Register --> DeepSlice --> DeepSlice Registration`.

![DeepSlice Registration dialog](/assets/dialogs/register-slices-deepslice-appose.png){.dialog}

* `DeepSlice model`: `mouse` or `rat`, matching the atlas.
* `Slice channels`: the channels sent to DeepSlice, for instance `0` for a nuclear staining only, `0,2` for the first and third channels, or `*` for all channels. The selected channels are merged into an RGB image with their display settings.
* `Adjust atlas slicing angle`: if checked, the atlas slicing angles are set to the median angle found by DeepSlice. Uncheck it to keep the current angles.
* `Pixel size sent to DeepSlice`: the slices are downsampled to this pixel size before being sent.
* `Ensemble`: averages the predictions of several models; results may be better or not depending on the dataset: try both.
* `Position post-processing`: how the positions predicted by DeepSlice are corrected:
  * `Keep order`: the current order of the slices is preserved;
  * `Keep order + ensure regular spacing`: the order is preserved and the slices are evenly spaced, with a spacing estimated by DeepSlice;
  * `Keep order + set spacing (parameter below)`: the order is preserved and the slices are evenly spaced, with the `Slice spacing` you give;
  * `No post-processing`: the raw DeepSlice positions, slices may be reordered;
  * `Keep current slice positions (in-plane registration only)`: the slices are not moved, only registered in plane, for instance after you positioned them manually.

DeepSlice runs on your computer. The first time it is used, ABBA installs it, with the Python environment it needs: this takes a few minutes and requires an internet connection. The following runs start much faster.

**Before**

![Before DeepSlice: the demo slices as imported, regularly spaced at the anterior end of the atlas](/assets/abba/getting_started/first_registration/03_display_adjusted.png)

**After**

![After DeepSlice: the slices positioned along the atlas, an R marker under each handle for the DeepSlice registration](/assets/abba/getting_started/first_registration/05_after_deepslice.png)

The result can then be refined with the [in-plane registrations](inplane_registration.md). The DeepSlice affine registration can also be edited by hand with {menuselection}`Register --> Edit Last Registration`.
