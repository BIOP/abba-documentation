# Your first registration

This tutorial registers demo mouse brain sections to the Allen Brain atlas, from start to finish, in about half an hour. Each step links to the page of the user guide that explains it in detail.

You need Fiji with ABBA installed (see [Installation](../installation/installation.md)), an internet connection, a mouse, and about 2 GB of free disk space.

## 1. Start ABBA

In Fiji, type `ABBA Start` in the search bar and press `Enter`.

* In the `Open Atlas` dialog, choose `allen_mouse_10um_java`, the adult mouse Allen Brain atlas built into ABBA. It is downloaded the first time.
* In the `ABBA Start` dialog, click `Coronal`, check that the axes read `RL`, `SI` and `AP`, then click `OK`.

The ABBA window opens with the atlas. Take a minute to [navigate in the viewer](../guide/abba_window.md#navigate-in-the-viewer): drag with the right mouse button to pan, use the mouse wheel to zoom.

![The ABBA window after start: atlas sections in a row in the viewer, the cards on the right](/assets/abba/getting_started/first_registration/01_abba_started.png)

## 2. Open the demo slices

Click {menuselection}`Import --> Open Demo Slices From ZENODO`, keep `Number of slides` to `1`, and click `OK`. The slide is downloaded from Zenodo (about 1 GB) the first time, then cached on your computer.

The sections of the slide appear below the atlas, selected. The slide label and overview images are imported too: their name does not contain `10x`. Select them in the table of the `Slices Display` card, then right-click in the viewer and choose `Remove Selected Slices` (see [Remove unwanted slices](../guide/select_display_slices.md#remove-unwanted-slices)).

![Demo slices just imported: the label and overview images of the slide, large and grey, are imported with the sections](/assets/abba/getting_started/first_registration/02_demo_slices_imported.png)

## 3. Adjust the display

In the `Slices Display` card, select all slices (`ctrl + A`), then use the header row of the table to show the nuclear (DAPI) channel and adjust its minimum and maximum displayed values: the tissue should be clearly visible, but not saturated (see [Display slices](../guide/select_display_slices.md#display-slices)). This matters for DeepSlice, which receives the channels with their display settings: color, minimum and maximum.

![The 12 sections, all selected, with only their DAPI channel displayed](/assets/abba/getting_started/first_registration/03_display_adjusted.png)

## 4. Check the orientation

Switch to review mode with `R`, and browse the slices with the left and right arrow keys. All slices must be oriented like the atlas, and flipped the same way. If some are not, select them and use the rotation and flip buttons of the `Edit Selected Slices` card (see [Orient slices](../guide/orient_slices.md)). Switch back to the positioning mode with `R`.

![Review mode on a section before positioning: it lies over the atlas section at its initial position, which does not match yet](/assets/abba/getting_started/first_registration/04_review_before_deepslice.png)

## 5. Position the slices with DeepSlice

Select all slices (`ctrl + A`) and click {menuselection}`Register --> DeepSlice --> DeepSlice Registration`:

* keep the `mouse` model, for this mouse atlas;
* set `Slice channels` to `0,1`: the DAPI channel, and channel 1, mostly autofluorescence, which outlines the sections well;
* keep `Adjust atlas slicing angle` checked;
* choose `Keep order + ensure regular spacing` as `Position post-processing`: the sections of the slide were cut at a regular interval, a prior knowledge DeepSlice can use;
* click `OK`.

The first time, ABBA installs DeepSlice, which takes a few minutes. DeepSlice then positions each slice along the atlas, adjusts the atlas slicing angles, and adds a first affine registration (see [Automated positioning with DeepSlice](#deepslice)).

Run DeepSlice a second time, with the same settings: the second run refines the result a bit more.

![After the two DeepSlice runs, positioning mode: the sections are evenly spaced along the atlas, a marker under each handle for each run](/assets/abba/getting_started/first_registration/05_after_deepslice.png)

Check the result in review mode. If a slice is badly positioned, drag it in positioning mode, or correct the atlas slicing angles in the `Atlas Slicing` card (see [Manual positioning](../guide/position_along_atlas.md#manual-positioning)).

![After the two DeepSlice runs, review mode: the same section over the atlas section at its new position](/assets/abba/getting_started/first_registration/05_review_after_deepslice.png)

## 6. Register the slices in plane

With all slices selected:

1. Click {menuselection}`Register --> Affine --> Elastix Registration (Affine)`. Set `Atlas channels` to `0,1` and `Slice channels` to `0,1`: the channels are paired in order. Channel 0 pairs the Nissl staining of the atlas with DAPI, which look alike; channel 1 pairs their autofluorescence. Using both pairs improves the registration. Keep the registration pixel size to 40 micrometers, fast and enough for an affine registration, and click `OK`.
2. Click {menuselection}`Register --> Spline --> Elastix Registration (Spline)`, with the same channels, 10 control points along X and a 20 micrometers pixel size, finer, for the local deformations. The number of control points along Y follows the aspect ratio of the region of interest: about 100 control points in all.

The indicators below the slice handles turn green when the registrations are done (see [Refine the in-plane registration](../guide/inplane_registration.md)). The first registration takes a moment longer, while ABBA installs elastix.

![The slice handles, in review mode: under each one, four green markers for its four registrations, the two DeepSlice runs, Elastix affine and Elastix spline, all done](/assets/abba/getting_started/first_registration/06_registration_markers.png){.dialog}

Check the result in review mode: press `P` and `N` to step back and forth through the registrations of the slices. A registration that went wrong can be removed with {menuselection}`Register --> Remove Last Registration`, or edited by hand with {menuselection}`Register --> Edit Last Registration`.

![Review mode after the Elastix registrations: the list of the registrations of the section, top left, all done](/assets/abba/getting_started/first_registration/06_review_after_elastix.png)

## 7. Save your work

Click {menuselection}`File --> Save State (+View)` and choose a file name: your session is saved in an `.abba` file, which you can reopen later (see [Save, load and share your work](../guide/save_load_share.md)).

## 8. Export the results to QuPath

Select all slices and click {menuselection}`Export --> QuPath --> Export Slices To New QuPath Project`, then choose an empty folder. ABBA creates a QuPath project with the demo images, their atlas regions and their registration.

Open this project in QuPath, with the ABBA extension installed, and import the atlas regions on each image: see [Analyse in QuPath](../guide/qupath_analysis.md).

Congratulations, you registered your first brain sections! Read the [user guide](../guide/prepare_qupath_project.md) to apply the same workflow to your own data.
