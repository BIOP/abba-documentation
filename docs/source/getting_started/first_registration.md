# Your first registration

This tutorial registers demo mouse brain sections to the Allen Brain atlas, from start to finish, in about half an hour. Each step links to the page of the user guide that explains it in detail.

You need Fiji with ABBA installed (see [Installation](../installation/installation.md)), an internet connection, a mouse, and about 2 GB of free disk space.

<!-- TODO GIF phase: illustrate each step with screenshots of the ABBA window on the demo slices. -->

## 1. Start ABBA

In Fiji, type `ABBA Start` in the search bar and press `Enter`.

* In the `Open Atlas` dialog, choose `allen_mouse_10um_java`, the adult mouse Allen Brain atlas built into ABBA. It is downloaded the first time.
* In the `ABBA Start` dialog, click `Coronal`, check that the axes read `RL`, `SI` and `AP`, then click `OK`.

The ABBA window opens with the atlas. Take a minute to [navigate in the viewer](../guide/abba_window.md#navigate-in-the-viewer): drag with the right mouse button to pan, use the mouse wheel to zoom.

## 2. Open the demo slices

Click {menuselection}`Import --> Open Demo Slices From ZENODO`, keep `Number of slides` to `1`, and click `OK`. The slide is downloaded from Zenodo (about 1 GB) the first time, then cached on your computer.

The sections of the slide appear below the atlas, selected. The slide label and overview images are imported too: their name does not contain `10x`. Select them in the table of the `Slices Display` card, then right-click in the viewer and choose `Remove Selected Slices` (see [Remove unwanted slices](../guide/select_display_slices.md#remove-unwanted-slices)).

## 3. Adjust the display

In the `Slices Display` card, select all slices (`ctrl + A`), then use the header row of the table to show the nuclear (DAPI) channel and adjust its minimum and maximum displayed values: the tissue should be clearly visible, but not saturated (see [Display slices](../guide/select_display_slices.md#display-slices)). This matters for DeepSlice, which works on the displayed images.

## 4. Check the orientation

Switch to review mode with `R`, and browse the slices with the left and right arrow keys. All slices must be oriented like the atlas, and flipped the same way. If some are not, select them and use the rotation and flip buttons of the `Edit Selected Slices` card (see [Orient slices](../guide/orient_slices.md)). Switch back to the positioning mode with `R`.

## 5. Position the slices with DeepSlice

Select all slices (`ctrl + A`) and click {menuselection}`Register --> DeepSlice --> DeepSlice Registration`. Choose the `mouse` model, the DAPI channel as `Slice channels`, keep `Adjust atlas slicing angle` checked and `Keep order` as post-processing, then click `OK`.

The first time, ABBA installs DeepSlice, which takes a few minutes. DeepSlice then positions each slice along the atlas, adjusts the atlas slicing angles, and adds a first affine registration (see [Automated positioning with DeepSlice](#deepslice)).

Check the result in review mode. If a slice is badly positioned, drag it in positioning mode, or correct the atlas slicing angles in the `Atlas Slicing` card (see [Manual positioning](../guide/position_along_atlas.md#manual-positioning)).

## 6. Register the slices in plane

With all slices selected:

1. Click {menuselection}`Register --> Affine --> Elastix Registration (Affine)`. Set `Atlas channels` to `0` (the atlas Nissl staining) and `Slice channels` to the DAPI channel, keep the registration pixel size to 40 micrometers, and click `OK`.
2. Click {menuselection}`Register --> Spline --> Elastix Registration (Spline)`, with the same channels, 10 control points and a 20 micrometers pixel size.

The indicators below the slice handles turn green when the registrations are done (see [Refine the in-plane registration](../guide/inplane_registration.md)). The first registration takes a moment longer, while ABBA installs elastix.

Check the result in review mode: press `P` and `N` to step back and forth through the registrations of the slices. A registration that went wrong can be removed with {menuselection}`Register --> Remove Last Registration`, or edited by hand with {menuselection}`Register --> Edit Last Registration`.

## 7. Save your work

Click {menuselection}`File --> Save State (+View)` and choose a file name: your session is saved in an `.abba` file, which you can reopen later (see [Save, load and share your work](../guide/save_load_share.md)).

## 8. Export the results to QuPath

Select all slices and click {menuselection}`Export --> QuPath --> Export Slices To New QuPath Project`, then choose an empty folder. ABBA creates a QuPath project with the demo images, their atlas regions and their registration.

Open this project in QuPath, with the ABBA extension installed, and import the atlas regions on each image: see [Analyse in QuPath](../guide/qupath_analysis.md).

Congratulations, you registered your first brain sections! Read the [user guide](../guide/prepare_qupath_project.md) to apply the same workflow to your own data.
