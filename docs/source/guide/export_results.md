# Export results

The most useful way to use the results of ABBA is usually to continue the analysis in QuPath: the atlas regions are transformed into the coordinates of the original slices, which are not deformed. This page explains all the export options; the analysis in QuPath is explained in [Analyse in QuPath](qupath_analysis.md).

All export commands act on the selected slices.

## Principle

For each slice, ABBA stores a registration: a function that maps a point of the atlas to a pixel of the slice (the forward transform). Unless the registration is very unusual, this function can be inverted, which maps a pixel of the slice to its atlas coordinates (the backward transform).

With this invertible transform, many exports are possible:

1. warp the atlas regions onto the slice: this is what the QuPath export does;
2. warp the slices onto the atlas;
3. export an image of the atlas coordinates of each pixel of the slice.

The first option is the fastest, since only the outlines of the regions are deformed, and the best one for the analysis, since your original data is not deformed.

## Export to QuPath

### Slices imported from a QuPath project

Click {menuselection}`Export --> QuPath --> Export Registrations To QuPath Project`. For each selected slice, ABBA saves its atlas regions and its registration in the folder of the corresponding image of the QuPath project. They are then imported in QuPath with the ABBA extension: see [Analyse in QuPath](qupath_analysis.md).

![Export Registrations To QuPath Project dialog](/assets/dialogs/export-registration-to-qupath.png){.dialog}

Check `Overwrite previous export` to replace a previous export of the same images, after editing a registration for instance.

### Slices imported from files

For slices imported from files with Bio-Formats, click {menuselection}`Export --> QuPath --> Export Slices To New QuPath Project` and choose an empty folder: ABBA creates a QuPath project (QuPath 0.7) containing the images of the selected slices, with their atlas regions and their registration, ready to be imported in QuPath with the ABBA extension. Only slices made of a single series of a 2D file can be exported this way, one slice per image.

## Warp slices onto the atlas

### Why it is not so obvious

As you add registration steps, the slices displayed in the ABBA window look better and better registered to the atlas. But these warped slices cannot be used directly for an analysis: only the part needed for the display is warped, on the fly, at the resolution of the screen.

To export warped slices, a full warped image must be computed at a resolution you choose. If you choose a small pixel size, the computation can take a long time: try a large pixel size first (40 micrometers, for instance). Halving the pixel size multiplies the computation time by 4.

### Export warped slices

Select the slices to export and click {menuselection}`Export --> ImageJ --> Export Registered Slices To ImageJ`. You get an ImageJ stack, one plane per slice, that can be saved and handled as any other ImageJ image.

* `Pixel size`: 20 micrometers gives a fast and broad overview. Exporting gigantic images this way is not advised: process the original images in QuPath instead.
* `Slice channels`: the channels to export, separated by commas, or `*` for all channels.
* `Add atlas regions overlay`: adds the atlas regions of each slice as an overlay of ROIs, named after the ontology property of your choice (acronym, name, id...).
* `Interpolate`: gives a smoother image, at the cost of computation speed.

:::{warning}
If you choose a pixel size that is far too small, you may reach the ImageJ limit of 2 billion pixels per plane.
:::

The export is restricted to the [region of interest](#region-of-interest): to export a small part of the atlas faster, define a small region of interest first, either in review mode or in positioning mode, and restore the full size afterwards.

![One plane of the stack exported by Export Registered Slices To ImageJ: a demo slice, registered, at 20 micrometers per pixel, its DAPI channel](/assets/abba/guide/export_results/registered_slice_export.png)

Do not forget to adjust the brightness and contrast of the exported image.

<!-- TODO: dialog screenshot of 'Export Registered Slices To ImageJ' (needs a live session: the ROI naming choices come from the atlas). -->

### Export the atlas at the same positions

To export the atlas in the same conditions (pixel size and region), click {menuselection}`Export --> ImageJ --> Export Atlas To ImageJ` with the same pixel size. Depending on the atlas, its channels include anatomical images, region borders, atlas coordinates, a left/right indicator and region labels: the channels are listed, in order, in the `Atlas Display` card.

![Export Atlas To ImageJ dialog](/assets/dialogs/export-atlas-to-imagej.png){.dialog}

Keep `Interpolate` unchecked when you export label channels. The exported atlas stack can be combined with the exported slices into a multichannel stack, since both have the same geometry.

![The same plane exported by Export Atlas To ImageJ, Nissl channel: the atlas section at the position of the slice, with the same geometry](/assets/abba/guide/export_results/atlas_export.png)

## Export the atlas coordinates of the original slices

Using the backward transform, {menuselection}`Export --> ImageJ --> Export Atlas Coordinates Of Original Slices To ImageJ` exports, for each selected slice, a 3-channel 32-bit image with the same pixels as the original, unregistered slice: each pixel holds its atlas coordinates (X, Y, Z), in millimeters.

![Export Atlas Coordinates Of Original Slices To ImageJ dialog](/assets/dialogs/export-deformation-field-to-imagej.png){.dialog}

* `Resolution level`: original slice images are often multiresolution; 0 is the full resolution, 1 the first downscaled level, etc.
* `Additional downsampling factor`: downsamples the exported image further, to speed up the computation.
* `Max iterations for transform inversion` can be left to its default value; increase it if the inversion of a spline registration does not converge.

With this image, you can, for instance, detect cells in ImageJ on the original slice and find their atlas coordinates. {menuselection}`Export --> ImageJ --> Export Original Slices To ImageJ` opens the original slice images in ImageJ, at the resolution level of your choice.

After adjusting the brightness and contrast of the exported image, you may get an image like this one:

![Atlas coordinates image](/assets/img/fiji_atlas_coordinates_image.png)

A periodic LUT is applied to each channel, which makes the warping easy to see. What really matters is the value of each pixel in each channel: its atlas coordinates, in millimeters.

## Export atlas regions as ImageJ ROIs

{menuselection}`Export --> ImageJ --> Export Regions To Roi Manager` adds the atlas regions of each selected slice to the ImageJ ROI Manager, in the pixel coordinates of the original, full resolution slice image. Since slice images are usually big, this is not the most recommended workflow: prefer QuPath.

{menuselection}`Export --> ImageJ --> Export Regions To File` saves the same regions as one ImageJ ROI set zip file per slice, in a folder of your choice.

![Exporting regions to the ROI Manager](/assets/gif/fiji_export_ij1_roi_manager.gif)

<!-- TODO GIF phase: re-record with ABBA 0.24.1 (the ROI Manager is an AWT window, which abba-doc-assets does not paint). -->

<!-- TODO: dialog screenshots of the two region exports (need a live session). -->

## Export to BigDataViewer

The `Export --> BigDataViewer` menu shows the registered slices in a new BigDataViewer window, saves them as a BigDataViewer-Playground dataset, or resamples them into a 3D volume in atlas coordinates. These exports are experimental: see the [Menu reference](#menu-export) for their parameters.

The thickness of the slices along the slicing axis, used by the 3D exports, is set with {menuselection}`Export --> Set Slices Thickness`, or {menuselection}`Export --> Set Slices Thickness (fill gaps)` to extend each slice halfway to its neighbors. It does not affect the registrations.

## Export as a QuickNII dataset

{menuselection}`Export --> QuickNII --> Export Registered Slices As Quick NII Dataset` packages the selected slices into a dataset that QuickNII can open: the registered slices are resampled at the pixel size of your choice, within the region of interest, and a series JSON file gives the position of each image in the atlas.

![Export Registered Slices As Quick NII Dataset dialog](/assets/dialogs/export-slices-to-quicknii-dataset.png){.dialog}

:::{warning}
This export has limitations. By default, the images are saved as JPEG, a lossy compression that supports only 3 channels and 8 bits of dynamic range. Keep the `.abba` state file if you want to modify the registration later.
:::

## Export a standardized, self-contained zip

{menuselection}`Export --> Export Standardized ABBA Project (Zip)` creates a self-contained zip of the whole session, with the slices, their registrations and deformation fields, to share a registered dataset: see [Save, load and share your work](#standardized-export).
