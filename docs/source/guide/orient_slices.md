# Orient slices (coarse registration)

Before positioning the slices along the atlas, whether manually or with DeepSlice, the slices must be oriented like the atlas: not rotated, not upside down, not mirrored. Sections are often mounted rotated on the slide, or flipped (the tissue seen from its back side), and the images then need the same correction.

:::{important}
**DeepSlice needs correctly oriented slices, all flipped the same way.** DeepSlice estimates the atlas slicing angle from the median of the angles found for each slice: a few slices left unflipped give opposite angles, which compete with the correct ones and degrade the result for all slices. Check the orientation of every slice before running DeepSlice.
:::

It is easier to judge the orientation in review mode (see [The ABBA window](abba_window.md#display-modes)), where each slice is overlaid on the atlas.

## Rotate and flip slices

The `Edit Selected Slices` card has four buttons acting on the selected slices:

![Edit selected slices](/assets/img/fiji_edit_slices_tab.png)

* the first two rotate the selected slices by 90 degrees clockwise or counterclockwise;
* the next two flip them: `Rotate around X axis (~ flip vertically)` turns the sections upside down, `Rotate around Y axis (~ flip horizontally)` mirrors them left-right.

A flip is a rotation of 180 degrees around an axis of the section plane: it shows the section from its other side, as if it had been mounted the other way around on the slide.

For other angles, click {menuselection}`Register --> Affine --> Rotate`: around `Z`, the slices rotate in plane by any angle (positive is clockwise on screen); around `X` or `Y`, only 180 or -180 degrees are accepted, which flips the slices.

![Rotate dialog](/assets/dialogs/rotate-slices.png){.dialog}

Slices rotate around the center of the [region of interest](#region-of-interest).

Rotations and flips are recorded as registration steps of the slices: they can be undone with `ctrl + Z`, and they are kept when the slices are saved, exported or copied to another slice.

:::{tip}
In coronal and horizontal orientations, mirroring a section left-right swaps the hemispheres. If you can tell the left and right hemispheres apart (a mark on the tissue, a unilateral injection...), make sure they match the atlas: the region names exported to QuPath distinguish left and right.
:::

<!-- TODO GIF phase: record the rotation and flip buttons on the demo slices. -->

## Manual affine registration

{menuselection}`Register --> Affine --> Manual Affine Registration` opens the selected slices in a dedicated window, one at a time, where you move, rotate, scale and shear each slice over the atlas with a gizmo. Use it for a coarse alignment, for instance to roughly center and scale the slices, or to compensate for the shrinkage of the tissue along one direction (often around 20% along Y due to slicing).

![Manual Affine Registration dialog](/assets/dialogs/register-slices-manual-affine.png){.dialog}

The channels you select are only used for the display in the editor. The result is a registration step like any other: it can be undone, removed, and edited later with {menuselection}`Register --> Edit Last Registration`.

<!-- TODO GIF phase: record the manual affine editor. -->

:::{note}
The manual affine registration replaces the `Interactive Transform` of previous ABBA versions.
:::

(hemi-sections)=
## Hemi-sections: mirror slices

DeepSlice and the automated registrations work best with full sections. If you only have hemi-sections, {menuselection}`Slices --> Mirror Slices` turns them into virtual full sections: the vertical midline of the atlas acts as a mirror, the half of each selected slice on the chosen side is kept, and its mirror image replaces the other half.

![Mirror Slices dialog](/assets/dialogs/mirror-do.png){.dialog}

Place the hemi-sections against the atlas midline first, with a rotation or a manual affine registration. Once the registration is done, {menuselection}`Slices --> Un-Mirror Slices` removes the mirroring while keeping the registrations made afterwards.

You can also restrict the registrations to the half of the atlas that contains tissue, with the [region of interest](#region-of-interest).
