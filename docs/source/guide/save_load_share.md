# Save, load and share your work

## Save the state of a session

At each step of the workflow, you can save the state of your work, as long as no registration is running.

Click {menuselection}`File --> Save State (+View)`. An `.abba` extension is added to the file name. An `.abba` file is a set of text files zipped together: the slices, their positions, display settings and registrations, the atlas slicing and the current view (see [State & transform files](../reference/state_files.md)).

These files are small and fast to save, so do not hesitate to save successive files all along your workflow. Consider your work done when you have the regions in QuPath, though: a state file offers fewer guarantees on the long term.

## Reopen a session

To reopen a session where you left it, start a new ABBA session with the same atlas, then click {menuselection}`File --> Load State (+View)` and select your `.abba` file. You can also drag and drop an `.abba` file onto the viewer of the ABBA window.

:::{note}
A state can only be loaded in a session without slices: restart ABBA before loading another state. Loading a state cannot be undone.
:::

:::{warning}
State files reference your images and your QuPath project by their location on disk. If you move your image files or your QuPath project, ABBA asks you for their new location when the state is opened. If the images come from a QuPath project, fix the image paths in QuPath first, before reopening the state in ABBA.
:::

(standardized-export)=
## Share a registered dataset: the standardized zip

To share a registered dataset with collaborators, or with a publication, click {menuselection}`Export --> Export Standardized ABBA Project (Zip)`. It creates a self-contained zip file with:

* all the slices of the session, downscaled to the pixel size of your choice (the images must have been properly calibrated when imported);
* the ABBA state, to reopen the session in ABBA;
* the deformation field of the final registration of each slice: the atlas coordinates of its pixels;
* metadata: the atlas, its slicing orientation, and a free text describing the experiment.

![Export Standardized ABBA Project (Zip) dialog](/assets/dialogs/export-std-zip-state.png){.dialog}

The zip is named `abba_export_<identifier>.zip`. The session itself is not modified.

To open such a zip, click {menuselection}`Import --> Import Standardized ABBA Project (Zip) in new ABBA instance`: a new ABBA session opens with the content of the zip.
