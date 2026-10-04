# Start ABBA and import slices

:::{note}
You will need a mouse: navigating with a trackpad can be frustrating!
:::

## Start ABBA

Start Fiji, or launch the ABBA application if you used the Windows installer, then start ABBA: type `ABBA Start` in Fiji's search bar, or click {menuselection}`Plugins --> BIOP --> Atlas --> ABBA - ABBA Start`.

### Choose an atlas

The first dialog asks for the atlas to register your slices to.

![Open Atlas dialog](/assets/dialogs/atlas-chooser.png){.dialog}

* Names ending in `_java` are the atlases built into ABBA: `allen_mouse_10um_java` is the adult mouse Allen Brain atlas CCFv3.1, `whs_sd_rat_39um_java` is the Waxholm Space atlas of the Sprague Dawley rat brain v4.2. They are downloaded once, the first time they are used, then cached on your computer.
* Names with `@` and a version, like `allen_mouse_25um@3.0`, are [BrainGlobe atlases](https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html). They are downloaded the first time they are opened, which can take minutes and a few GB. The first time BrainGlobe is used on a computer, ABBA also sets up the Python environment BrainGlobe needs, which takes a few more minutes.
* `Additional atlases` is optional: atlas names, separated by commas, whose images are added as extra channels to the main atlas. Leave it empty for a plain atlas.

:::{tip}
To see all the BrainGlobe atlases that can be used, and the ones already downloaded, run {menuselection}`Plugins --> BIOP --> Atlas --> List BrainGlobe Atlases` in Fiji. Afterwards, the atlas dialog offers the whole list.
:::

This documentation uses the Allen mouse brain atlas in coronal orientation, the most common case, but ABBA works the same way with any atlas and orientation.

### Choose the slicing orientation

The second dialog sets how the atlas is cut, to match the orientation of your sections.

![ABBA Start dialog](/assets/dialogs/abba-start.png){.dialog}

Click `Coronal`, `Sagittal` or `Horizontal` to set the three axes at once. If your sections are displayed in another way, set the anatomical direction of each axis yourself:

* `X axis`: the direction of your sections from left to right on screen;
* `Y axis`: the direction of your sections from top to bottom on screen;
* `Z axis`: the slicing axis, along which the sections follow each other.

:::{warning}
Check the three axes before clicking `OK`: the dialog remembers the values of your last session, and the three axes must be different.
:::

The ABBA window opens, with the atlas displayed. The next page, [The ABBA window](abba_window.md), explains how to navigate in it.

## Import slices

ABBA offers several ways to import slices, all in the `Import` menu of the ABBA window. Importing a QuPath project is the recommended one.

(import-qupath-project)=
### Import a QuPath project

Click {menuselection}`Import --> Import QuPath Project`, or drag and drop a `.qpproj` file onto the viewer of the ABBA window.

![Import QuPath Project dialog](/assets/dialogs/import-slices-from-qupath.png){.dialog}

Select your project file, then give an initial position along the slicing axis for the first slice and the approximate spacing between slices, in millimeters (the demo dataset uses an 80 micrometers spacing: 0.08). These values are only starting estimates, refined later. Use a negative spacing to reverse the order of the slices.

A second dialog then offers a few dataset options. The defaults work in most cases:

* `Dataset Name`: name of the dataset in the BigDataViewer-Playground tree; leave it empty to use the project folder name.
* `Plane Origin Convention`: where the origin of each image is located. This does not matter for most users.
* `Split RGB Channels`: splits RGB images into three channels.

:::{warning}
If your dataset contains 16-bit RGB channels (as is the case for some CZI files), check `Split RGB Channels`.
:::

The first import may take up to a minute. Once the project is loaded, the slices appear along the atlas. They are displayed with all their channels, and the imported slices are selected.

![ABBA window right after importing slices: the atlas sections in a row, the imported slices below them, all selected](/assets/abba/guide/start_and_import/slices_imported.png)

(import-files)=
### Import files with Bio-Formats

Click {menuselection}`Import --> Import With Bio-Formats` to import image files directly, without a QuPath project. Each image series of each file becomes a slice.

![Import With Bio-Formats dialog](/assets/dialogs/import-slices-from-files.png){.dialog}

This is convenient, but a QuPath project makes the analysis of the results easier. You can create one at the end, with the registration results, with {menuselection}`Export --> QuPath --> Export Slices To New QuPath Project` (see [Export results](export_results.md)).

(import-demo-slices)=
### Open demo slices

To try ABBA without your own data, click {menuselection}`Import --> Open Demo Slices From ZENODO`. Demo mouse brain sections are downloaded from [Zenodo](https://zenodo.org/records/14918378) and cached on your computer (about 1 GB per slide; each slide holds several sections).

![Open Demo Slices From ZENODO dialog](/assets/dialogs/import-demo-slices-zenodo.png){.dialog}

The label and overview images of each slide are imported as extra slices: remove them before registering (see [Remove unwanted slices](#remove-unwanted-slices)).

Another demo dataset, a whole mouse brain (25 or 97 sections), can be streamed from a public OMERO server with {menuselection}`Import --> Open Demo Slices From OMERO`. It comes as a QuPath project, so registrations can be exported to it. This requires an internet connection and the OMERO dependencies of Fiji.

### Import a QuickNII project

Click {menuselection}`Import --> Import QuickNII Project` and select the `.json` file of a [QuickNII](https://quicknii.readthedocs.io/) series (DeepSlice produces this format too). The images it references must be in the same folder. The slice positions, their in-plane affine transformations and the atlas slicing angle are imported.

![Import QuickNII Project dialog](/assets/dialogs/import-slices-from-quicknii.png){.dialog}

:::{warning}
The import is not necessarily exact! QuickNII allows each slice of a dataset to be positioned in any orientation. In ABBA, within a single session, the slicing angle is the same for all slices. During the import, ABBA computes the median slicing angle of all slices and applies it to all of them.
:::

An ABBA session can also be exported as a QuickNII dataset, with some limitations: see [Export results](export_results.md).

### Import the current ImageJ image

Click {menuselection}`Import --> Import Current ImageJ Window` to import the image of the active ImageJ window as a single slice. Make sure its pixel size is set correctly.

:::{warning}
A state file containing slices imported this way may not be reopened. Prefer saving the image to a file and importing it with Bio-Formats.
:::

### Import sources from BigDataViewer-Playground

Click {menuselection}`Import --> Import Sources From BDV-Playground`, or drag and drop sources from the [BigDataViewer-Playground](https://imagej.net/plugins/bdv/playground/bdv-playground) [tree view](https://imagej.net/plugins/bdv/playground/bdv-playground-visualize) onto the viewer of the ABBA window.

### Open a standardized ABBA project

A standardized ABBA project is a zip file created with {menuselection}`Export --> Export Standardized ABBA Project (Zip)`, to share a registered dataset. Open it with {menuselection}`Import --> Import Standardized ABBA Project (Zip) in new ABBA instance`: see [Save, load and share your work](save_load_share.md).
