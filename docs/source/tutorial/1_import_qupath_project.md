# Data import & navigation

:::{note}
You will  need a mouse, since navigating with a trackpad can be frustrating!
:::

Start Fiji, or launch the ABBA application if you used the installer, then start the ABBA plugin (type `ABBA` in Fiji’s search bar or go to `Plugins › BIOP › Atlas › ABBA - ABBA Start`). You will then need to choose an atlas (this documentation uses the Allen adult mouse brain atlas) and select between three slicing orientations: coronal, sagittal, or horizontal. The examples provided use the coronal orientation, as it is the most common, but ABBA functions similarly in all orientations.

## Navigating ABBA's BigDataViewer

ABBA utilizes [Fiji's BigDataViewer](https://imagej.github.io/plugins/bdv/index) to display multiresolution images in a highly responsive way. However, the BigDataViewer interface is quite different from the standard ImageJ display, so it's essential to get familiar with the basic navigation controls:
* `hold and drag right-click` pan across the image
* `mouse wheel`  zoom in / out
* `up / down keys` zoom in / out
* `shift + up / down key` fast zoom in / out

Take some time to practice these commands so you can efficiently navigate across the atlas.

## Atlas display options

When ABBA starts, you will see the atlas dataset, sliced regularly along the Z-axis. The dataset consists of a 3-channel image, which in the case of the Allen Brain Atlas CCFv3, includes:

* `Nissl (Ch. 0)`
* `Ara (Ch. 1)`
* `Label Borders (Ch. 2)`

You can toggle these channels on or off using checkboxes and adjust their visibility using sliders to emphasize or de-emphasize each one.

![Atlas display options](/assets/gif/fiji_abba_atlas_display.gif)

## Importing a QuPath Project into ABBA

Once you’re comfortable with the navigation, you can proceed to import a QuPath project. In the ABBA window menu, click `Import > ABBA - Import QuPath Project`:

![Importing a QuPath Project in ABBA](/assets/img/fiji_import_qupath.png)

:::{info}
To import a QuPath project, you can also drag and drop a `.qpproj` file into ABBA's graphical interface (in the viewer area).
:::

Next, select your project file, specify the initial position of the first slice, and enter the approximate slice spacing in millimeters (the demo dataset uses 80-micron spacing). These values are just starting estimates and will be fine-tuned later.

![Set initial positions of the slices in the atlas](/assets/img/fiji_set_ini_position.png)

After this, a second window will appear with advanced import options. The default settings (as shown below) should work for most cases.

![Advanced import options](/assets/img/fiji_advanced_import_options.png)

The plane origin convention doesn’t matter for most users.

:::{warning}
If your dataset contains 16-bit RGB channels (as is the case for some CZI files), be sure to check the `Split RGB channels` option.
:::

The initial import process may take up to a minute. Once the project is loaded, you should see an image similar to this:

![Project newly opened in ABBA](/assets/img/fiji_just_opened_project.png)

## Other import methods

### Importing a [QuickNII] project

You have an option to open a QuickNII project within `Import>Import QuickNII project` and selecting the `.json` file for this project. 

:::{warning}
Be aware that the import will not necessarily be exact! Indeed QuickNII allows for each slice of a similar dataset to be positioned in any orientation. In ABBA, within a single project, the slicing angle correction will be applied identically to all sections. As a result, during the import of the QuickNII project, ABBA will compute the median slicing angles for all slices and apply it identically to all slices.
:::

It is also possible to export an ABBA project into a QuickNII project, but this will suffer from limitations. Check the [export section](3_export_registrations.md#5-export-as-a-new-quicknii-dataset) for more details.

### Importing the Current ImageJ Window
You can also import the current ImageJ window into ABBA, provided the window is in focus. Make sure that the pixel size is set correctly, ideally in millimeters.

:::{warning}
There is currently a bug that prevents reopening ABBA state files created using this method.
:::

### Direct file import of a file

While importing a file that isn’t part of a QuPath project can make downstream processes more difficult, it is possible. However, proceed with this option only if you are sure it won’t affect your workflow.

### Importing from BigDataViewer Playground

You can also drag and drop sources directly from the [BigDataViewer Playground](https://imagej.net/plugins/bdv/playground/bdv-playground)'s [tree view](https://imagej.net/plugins/bdv/playground/bdv-playground-visualize) into the BigDataViewer window in ABBA.
