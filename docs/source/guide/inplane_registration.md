# Refine the in-plane registration

Once the slices are positioned along the slicing axis and the atlas slicing angles are corrected, each slice is registered to the atlas in 2D, in its own plane. This is done automatically, manually, or with a mix of both.

:::{note}
For automatic registrations, ABBA uses [elastix](https://elastix.dev/), a toolbox for medical image registration. ABBA sets the elastix parameters from the known pixel sizes of the slices and of the atlas, so that there is little to tune. The key metric of the registration is the [Mattes mutual information](https://doi.org/10.1109/TMI.2003.809072), robust when registering images of different modalities, such as DAPI versus Nissl, or autofluorescence images.

elastix runs on your computer. The first time it is used, ABBA installs it automatically: this takes a moment and requires an internet connection.
:::

:::{note}
For manual registrations, ABBA uses the [manual affine editor](orient_slices.md#manual-affine-registration) and Fiji's [BigWarp](https://imagej.github.io/plugins/bigwarp), where you place landmarks on the slice and the atlas.
:::

:::{warning}
If your image file format does not contain multiple resolution levels (pyramids), ABBA may struggle to downsample the images properly, which can lead to poor registrations. Check `Show registration images` in the registration dialog to see the images that are actually registered. See [Supported file formats](../reference/file_formats.md).
:::

## Registration workflow and status indicators

When a registration starts on a slice, an indicator appears below its handle. It is round for automatic registrations and rectangular for manual ones, and its color shows the status of the job:

- light red: registration waiting (not started, or waiting for the user, like a manual registration whose editor is open);
- yellow: registration in progress;
- green: registration done.

![The slice handles in review mode, each with its markers: all the slices have their DeepSlice and Elastix affine registrations done (green), except 10x_06, whose manual registration is open in the editor, and whose Elastix affine registration waits behind it (light red)](/assets/abba/guide/inplane_registration/registration_status.png)

ABBA runs several registrations in parallel, from 4 to 128 at once depending on your computer. You can monitor the memory and CPU usage with {menuselection}`View --> Cards --> Add Resources Monitor`.

The following sequence shows the twelve demo slices, positioned by DeepSlice (the first marker, done), when an Elastix affine registration and then an Elastix spline registration are started on all of them: the markers of both registrations appear at once, waiting, then each one runs and is done in turn.

![The slice handles in review mode, with the markers of the registrations of each slice, from waiting to running to done](/assets/abba/guide/inplane_registration/registration_progress.gif)

(sped up 5 times: about 30 seconds of real time)

Registrations add up: you usually start with an affine registration, followed by one or two spline registrations. Here is the top right quarter of a demo slice, with the borders of the atlas regions only, after DeepSlice, after an Elastix affine registration, and after an Elastix spline registration:

![A quarter of a slice with the atlas region borders, after each registration step: DeepSlice, Elastix affine, Elastix spline](/assets/abba/guide/inplane_registration/registration_steps.png)

For difficult slices where the automated registrations fail, start with a manual registration to help the automated ones, or edit the result of a spline registration by hand, adding landmarks in the regions you care about most.

:::{warning}
If a slice contains broken or missing regions, a perfect registration can be hard or even impossible to reach: ABBA does not handle discontinuous deformations well.
:::

(registration-channels)=
## Choosing the channels

Each registration asks for the channels to use, as 0-based indices separated by commas, for the atlas and for the slices. Atlas and slice channels are **paired in order**, and there must be as many of each. For instance:

* atlas `0`, slices `0`: atlas channel 0 (Nissl, for the Allen Brain atlas) is registered with slice channel 0 (DAPI, for instance);
* atlas `0,1`, slices `0,1`: atlas Nissl with slice channel 0, and atlas autofluorescence (channel 1) with slice channel 1;
* atlas `0,0`, slices `1,3`: if slice channels 1 and 3 both contain nuclei, both are registered with the atlas Nissl.

The atlas channels are listed, in order, in the `Atlas Display` card. When several channel pairs are used, each pair contributes equally to the registration: this makes the registration more robust when your slices contain distinct features, like autofluorescence, matching a specific atlas channel.

![Multi Channels](/assets/img/fiji_registration_multichannel_images.png)

(region-of-interest)=
## Region of interest

Registrations, and exports, are computed within a rectangular **region of interest** of the atlas: by default, the full atlas section. To restrict it, for instance to hemi-sections or to a region you care about, open the `Define Region Of Interest` card, click `Define Interactively` and draw the rectangle in the viewer, or type its coordinates. `Full Size` restores the full atlas section.

![The Define Region Of Interest card, with a region restricted to the left half of the atlas](/assets/abba/guide/inplane_registration/define_roi_card.png)

![The same region of interest in review mode: outside of it, the atlas is dimmed](/assets/abba/guide/inplane_registration/region_of_interest.png)

:::{warning}
Remember to restore the full size when you are done: the region of interest applies to all the following registrations and exports.
:::

## Affine registration (automated)

The affine registration scales, rotates, translates and shears the slices to match the atlas, without deforming them locally. Select the slices to register and click {menuselection}`Register --> Affine --> Elastix Registration (Affine)`.

![Elastix Registration (Affine) dialog](/assets/dialogs/register-slices-elastix-affine.png){.dialog}

A common start is the DAPI channel of the slices with the Nissl channel of the atlas (channel 0). `Registration pixel size` is the pixel size of the images sent to elastix: 40 micrometers is a good start for a mouse brain. Check `Show registration images` to see these images.

## Spline registration (automated)

The spline registration deforms the slices locally. Select the slices to register and click {menuselection}`Register --> Spline --> Elastix Registration (Spline)`. It is usually run after an affine registration.

![Elastix Registration (Spline) dialog](/assets/dialogs/register-slices-elastix-spline.png){.dialog}

The slice is deformed by a grid of control points: `Number of control points along X` sets its size along X, and the number along Y follows the aspect ratio of the region of interest. More control points allow more local deformations, at the risk of overfitting when the structures of the slice and of the atlas differ. Values between 5 and 20 are recommended.

## BigWarp registration (manual)

For full control over the registration, click {menuselection}`Register --> Spline --> BigWarp Registration`: each selected slice opens in [BigWarp](https://imagej.github.io/plugins/bigwarp), one after the other, where you place landmarks on the slice and on the atlas. The channels you select are only used for the display.

![BigWarp Registration dialog](/assets/dialogs/register-slices-bigwarp.png){.dialog}

## Edit a registration

The last registration of a slice can be edited by hand, if it is editable: select the slices to edit and click {menuselection}`Register --> Edit Last Registration` (or right-click and choose `Edit Last Registration`).

![Edit Last Registration dialog](/assets/dialogs/register-slices-edit-last.png){.dialog}

* Spline registrations (Elastix spline, BigWarp) open in BigWarp, with the landmarks of the registration already in place. Move or add landmarks with the [BigWarp commands](../reference/shortcuts.md#bigwarp), then close the BigWarp window: the result appears in the ABBA window.
* Affine registrations (Elastix affine, manual affine, DeepSlice) open in the affine editor.

Edits can be undone with `ctrl + Z`.

:::{warning}
If many slices are selected, the registration of each slice opens for editing, one after the other. Make sure this is what you intend!
:::

![Edit Last Registration on an Elastix spline registration: the two BigWarp windows, the moving slice (left) and the atlas (right), with the landmarks of the registration in magenta](/assets/abba/guide/inplane_registration/bigwarp_edit.png)

You can check the [BigWarp documentation](https://imagej.net/plugins/bigwarp), or the [relevant part of the video tutorial](https://youtu.be/sERGONVw4zE?t=2534s), for more information about its interface. After editing a registration, export it again (to QuPath for instance) to update the results.

## Remove a registration

To remove the last registration of the selected slices, click {menuselection}`Register --> Remove Last Registration`, or right-click and choose `Remove Last Registration`. This can be undone.

## Copy registrations from one slice to others

{menuselection}`Register --> Copy Registrations From Model And Apply To Selected Slices` copies all the registrations of a model slice and appends them, as they are, to the selected slices: nothing is recomputed. See [the use case in this issue](https://github.com/BIOP/ijp-imagetoatlas/issues/174).

![Copy registrations dialog](/assets/dialogs/register-slices-copy-and-apply.png){.dialog}

## Browse registration steps

To review the registration steps of the slices, use the `Browse Registrations` buttons of the `Display & Navigation` card:

* `View Previous [P]`: go back to the previous registration step;
* `View Next [N]`: move to the next registration step.

The registration indicators turn from green to gray as you step back through the registrations.

## Registration workflow example

A typical registration is obtained with these successive steps, on all slices:

* affine registration: atlas channels `0,1` with slice channels DAPI and autofluorescence;
* spline registration, 15 control points: atlas channels `0,1` with slice channels DAPI and autofluorescence.

This takes about 10 minutes for 50 slices on a laptop.

## Adding your own registration method

The registration methods (BigWarp, Elastix spline, affine...) are plugins discovered automatically by ABBA. While the documentation is lacking for the moment, you can write a registration plugin of your own and use it in ABBA: it appears in the `Register` menu.
