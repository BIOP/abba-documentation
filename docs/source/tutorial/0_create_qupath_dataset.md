# Creating a compatible QuPath project
:::{warning}
Do not modify the images in the project once they have been opened and used in ABBA. Changing the images in the QuPath project may cause ABBA to function improperly.
:::

:::{hint}
Using a QuPath project is the preferred method for working with ABBA, as it greatly simplifies downstream processing.
:::

## Dataset requirements

ABBA is designed to work on a set of brain slices from a single animal. If you need to align slices from multiple animals, each animal should be processed in a separate QuPath project. While it's possible to combine slices from different animals in one dataset, this reduces flexibility in the registration process, particularly in terms of setting different cutting angles for different animals.

### Supported Image Formats

ABBA can handle a variety of image types, including:

* Any format supported by [Bio-Formats](https://bio-formats.readthedocs.io/en/latest/supported-formats.html)
* Data streamed from an [OMERO](https://www.openmicroscopy.org/omero/) server
* XML-defined [BigDataViewer datasets](https://imagej.net/plugins/bdv/playground/bdv-playground-open-dataset)
* A [QuPath](https://qupath.github.io/) project (which internally uses Bio-Formats and OMERO)

Please also review the information on [pyramidal file format requirements](../explanation/file_formats_supported.md) to ensure your files meet the necessary criteria.

## Setting up a dataset of brain sections in QuPath

As recommended, you should begin by creating a QuPath project that contains all the brain slices you wish to register, typically from one animal.

For detailed instructions, refer to the QuPath documentation: [Creating a Project in QuPath](https://qupath.readthedocs.io/en/latest/docs/tutorials/projects.html).

Below is a brief overview of the steps to set up a project:
* (You can download a [demo dataset](demo_dataset.md) if needed.)
* Create a new project by dragging and dropping an empty folder into QuPath's graphical user interface.
* Drag and drop your images into the QuPath project.
* Select `Bio-Formats builder` and click Import.

:::{note}
You can also work with OMERO images, provided they are accessed through the [OMERO-RAW QuPath extension](https://github.com/BIOP/qupath-extension-biop-omero). After installing the extension, you can add images directly by browsing your OMERO server: `Extensions > OMERO-RAW > Browse server...` and importing images or entire datasets.
:::

![creating a project with slices in QuPath](/assets/gif/qupath_create_project.gif)

:::{warning}
Ensure that all images are correctly calibrated (in units such as microns or millimeters, not **pixels**). In QuPath, verify this by checking the `Image` tab, where the physical unit should be specified. If the units are set to pixels, adjust the pixel size before importing the project into Fiji's ABBA plugin, or the images will be scaled incorrectly.
:::

![image calibration in QuPath](/assets/img/qupath_image_calibration.png)

---

At this point, your work in QuPath is complete. You can leave QuPath open as you proceed with the rest of the workflow.
