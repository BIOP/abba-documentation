# Fiji - Slices selection and display

Once your dataset is opened in ABBA, you’ll be able to position slices along the slicing axis ("Z") and adjust each slice in 2D (including tilt and roll corrections, 2D affine, and spline in-plane registrations).

When ABBA starts, you’ll begin in `Positioning mode`, where the Allen brain atlas is displayed with regularly spaced slices overlaid on your dataset.

:::{warning}
Using a mouse is strongly recommended for a smoother experience
:::

----

## Selecting slices

ABBA allows you to select and perform actions on specific slices. Each slice is represented by a round handle, which indicates whether it’s selected (green) or not (yellow).

![Highlighted green handle of selected slices](/assets/img/fiji_selected_slice.png)

There are two ways to select slices:

### Rectangle Selection with the Mouse

You can select slices by drawing rectangles around them. There are also modifier keys for adding or removing slices from the current selection:

* `Hold and left-click`: Draw a rectangle to select slices.
* `Ctrl + hold and left-click`: Remove slices from the current selection.
* `Shift + hold and left-click`: Add slices to the current selection.

:::{warning}
Make sure to press the modifier keys before drawing the rectangle, or they won’t take effect.
:::

Here’s a demonstration of adding slices using `shift + rectangle`, removing slices with `ctrl + rectangle`, and selecting all slices with `ctrl + a`.

![Selecting slices in bdv](/assets/gif/fiji_select_slices.gif)

### Slice display table

You can also select slices in the Slices Display card table:

![Selecting slices in bdv](/assets/gif/fiji_select_slices_table.gif)

The selection behaves as a standard table (in windows: `shift` to select a range, `ctrl` to toggle the selection of a single slice). And there are additional shortcuts:

* `Ctrl + a`: Select all slices.
* `Ctrl + shift + a`: Deselect all slices.

For Mac users, use `cmd` instead of `ctrl`.

## Slices display options

To facilitate registration, it’s essential to ensure your slices are displayed properly. Depending on your use case, you may want to show only a subset of channels and adjust the minimum and maximum display values for optimal contrast.

### Removing Unwanted Slices

In some cases, especially with multi-series files like VSI files, you might encounter unwanted images, such as labels or macro images. These unwanted slices, typically RGB images, will often appear black in the slice display table, making them easy to identify.

To remove unwanted slices:

* Select the slices that appear black in the table.
* Right-click in the ABBA viewer window and select `Remove Selected Slices` (or go to `Edit > ABBA - Remove Selected Slices` in the menu bar).

![Removing slices](/assets/gif/fiji_remove_slices.gif)

### Displaying Specific Channels

Often, slices have multiple channels, but not all of them are useful for registration or analysis. To focus on the relevant channels, you can control their display by toggling selected channels through the header of the slice display table.

Additionally, you can adjust the color, and the minimum and maximum display values for better contrast (pay attention to where you need to click in the column headers).

![Slices display options](/assets/gif/fiji_slices_display_options.gif)

If necessary, the display for each slice can be further customized by modifying its corresponding row in the table.

# Fiji - Registration workflow

The registration process starts with a manual step, which serves two purposes:

* Estimate the position of each slice along the "Z" axis of the atlas.
* Adjust the slicing angles of the atlas.

:::{hint} 
If your slices have sufficient quality, consider using ABBA's DeepSlice integration to skip these initial manual registration steps. Note than DeepSlice is available only in coronal orientation for adult mouse and rat altases only.
:::

To help position each slice along the slicing axis, ABBA offers an interface designed for easy manipulation of a series of slices.

## Flip and/or rotate slices

In some cases, the acquired slices might be flipped or rotated relative to the atlas. You can correct this by using the `Edit Selected Slices` tab, which provides four options:

![Edit selected slices](/assets/img/fiji_edit_slices_tab.png)

The first two buttons rotate the selected slices 90° clockwise (CW) or counterclockwise (CCW). The next two buttons flip the slices either vertically or horizontally.

:::{warning}
Unlike most other actions in ABBA, these flipping and rotating actions cannot be undone using `Ctrl+Z` (or redone with `Ctrl+Shift+Z`). However, they can easily be reversed by applying the opposite rotation or flip.
:::

## Manual interactive transformation of slices (Scale, Translate, Rotate)

To apply manual transformations (such as rotation, translation, and scaling) to the selected slices, go to the top menu bar and select `Edit > ABBA - Interactive Transform`. This tool allows you to rotate, translate, and scale the slices anisotropically (for example, compensating for the common 20% shrinkage in the Y direction due to slicing).

![Interactive slice transformation](/assets/gif/fiji_interactivetransform.gif)

This feature provides fast visual feedback as you apply transformations. Once you're satisfied with the adjustments, simply close the `Interactive Transform` window. This tool can also be used in review mode or with different overlap modes for more precise adjustments.

:::{warning}
Similar to flipping and rotating, the interactive transformation cannot be undone using `Ctrl+Z`. However, you can revert to the original transformation by clicking the `Restore initial settings` button.
:::

## Slices registration | Z Axis (manual)

Before beginning the registration process, you must position slices along the Z axis and correct the slicing angles of the atlas to match your dataset. Since the slicing angle applies to all slices, it’s best to register one animal at a time.

### Drag selected slices

If your slices are not sorted correctly along the atlas axis, you can manually rearrange them. Select the slices that are out of place and drag them along the axis. If needed, you can create gaps between slices to accommodate others.

By selecting one or more slices, you can shift them along the slicing axis by dragging the rectangles below the atlas:

![Drag slices along axis](/assets/gif/fiji_slices_drag.gif)

### Distribute spacing between selected slices

To evenly space selected slices, click the distribute spacing button in the `Edit Selected Slices` card or press the `d` shortcut. This action can be undone with `Ctrl+Z` and redone with `Ctrl+Shift+Z`:

![Distribute slices](/assets/gif/fiji_slices_distribute.gif)

When no slice is marked as a key slice (explained below), the `distribute spacing` function preserves the positions of the first and last selected slices.

### Manual positioning along the Atlas axis + Locking Key Slices

ABBA allows you to switch between a zoomed-out overview and a zoomed-in view for precise alignment of individual slices with the atlas.

A recommended workflow for manually aligning slices along the atlas includes:

* Sorting slices correctly along the axis.
* Rotating or flipping slices to match the atlas orientation.
* Displaying the atlas sliced with the largest slices thickness (every 500 microns - see gif just below):
* Shifting slices along the atlas at their approximately correct position
* Matching precisely a slice of your choice (usually one with easily recognizable features) with the atlas by zooming in
* Setting this slice as `key slice` (select this slice only, right click and select `Set as key slice` in the popup menu). As long as you don't drag this slice, each key slice has its z position locked in the atlas: `Distribute Spacing` won't affect the position of key slices.
* Setting a few others slices precisely and setting them as key slices
* Adjusting atlas slicing angles and checking all slices.
* Using `distribute spacing` to evenly space slices between key slices.

![Coarsening atlas slicing](/assets/gif/fiji_atlas_coarse_slicing.gif)

This coarse display allows, by dragging slices, to adjust approximately all slices along the atlas.

:::{note}
The displayed slicing of the atlas does not affect the registration. Internally, slices are positioned with a precision of 10 microns, which corresponds to the highest resolution of the atlas.
:::

After all slices are approximately positioned, you can zoom in into the atlas, reduce the displayed spacing, fine tune  the position of a few slices along the atlas and set these fine tuned slices as `key slices`.

![Finding correspondance and key slice](/assets/gif/fiji_atlas_drag_then_key.gif)

Once key slices are set, their positions along the axis remain locked when other slices are moved. You can still drag key slices manually if needed.

When key slices are selected, they will keep their position along the axis when other slices are dragged (you can still directly drag the key slice if you need to move it). The other slices are stretched along the axis while maintaining their spacing ratio.

You can set multiple key slices in specific positions along your sections, usually the ones with the most recognizable features.

You typically need only 2 or 3 key slices for accurate positioning along the atlas. The distribute function ensures even spacing between selected slices, while preserving key slice positions and the placement of the first and last slices.

### Using the review mode to investigate the position of slices along the atlas

Positioning mode allows easy movement of slices but is not optimal for overlaying sections onto the atlas. You can switch to review mode to display a single slice at a time, overlaying it with the atlas for inspection.

To switch to review mode:

* Press the shortcut key r. 
* Or click `Review` in the `Display & Navigation > Modes` card.
* Or Select `Display > Review Mode` from the menu bar.

![Review mode](/assets/img/fiji_review_mode.png)

In review mode, the current slice (indicated by a white circle around the handle) is displayed. Navigate between slices with the left and right arrow keys, or use the `Previous` and `Next` buttons in the `Display & Navigation` card.

If adjustments are needed, you can return to positioning mode at any time.

--- 

`Right` and `Left` key to change the current slice also works in the positioning mode.

![Current slice](/assets/img/fiji_current_slice.png)

--- 

## Correcting atlas slicing orientation

The `Atlas Slicing` card contains two sliders to adjust the slicing angles of the atlas:

![Atlas slicing adjustement](/assets/gif/fiji_adjust_atlas_angle.gif)

Use slices with easily identifiable features to set the slicing orientation. 

:::{note}
The atlas slicing angles will be consistent across all sections: while you can tilt the atlas, you cannot "bend" it.
:::

## Slices registration | Z Axis (automated with DeepSlice)

If you are working with atlases mapped to the mouse Allen Brain CCFv3 or the Rat Waxholm atlas in coronal sections, you can use [DeepSlice](https://www.deepslice.com.au) ([publication](https://doi.org/10.1038/s41467-023-41645-4)) to automate the initial registration steps. DeepSlice, a deep-learning-based tool, automatically aligns whole mouse or rat brain histological sections. 

:::{note} DeepSlice is compatible only with the Allen mouse brain atlas and the Rat Waxholm atlas, in coronal orientation. 
:::

Using DeepSlice accelerates alignment and automates key steps:

* Estimating atlas cutting angles.
* Initial positioning of slices along the Z axis.
* In-plane affine registration (without deforming slices beyond affine transformations).

ABBA can then refine this alignment through non-linear registration with tools like BigWarp or Elastix.

:::{warning} 
For best results, use DeepSlice when all slices belong to the same animal, as the same cutting angle correction applies to all slices. 
:::

:::{warning} Ensure your display settings prevent saturated pixels!

DeepSlice operates with 8-bit RGB images. Before sending slices to DeepSlice, ABBA rescales intensities based on your display settings. Proper display settings (not too dark or too bright) enhance registration quality. 
:::

### Using DeepSlice web interface in ABBA

To use the DeepSlice web interface:

* Adjust slice display settings to avoid saturation.
* Select the slices you want to register.
* Click `Align > ABBA - DeepSlice Registration (web)`.

You get the following window:

![ABBA DeepSlice options](/assets/img/fiji_deepslice_options_web.png)

* `Slices channels, 0-based, comma separated, '*' for all channels` - used to select the channels you want to export to DeepSlice. You can for instance export a nuclear channel only. You can export the first and third channel by writing `0,2`. Usually, a RGB image contains only one channel.
* `Allow change of atlas slicing angle` - When checked, ABBA will adapt the atlas slicing angle based on the median slicing angles given by DeepSlice. If you don't want to modify the atlas slicing angle, you can uncheck this box.
* `Average of several models (slower)` - this parameter is ignored in the web interface.
* `Post_processing` - this parameter is ignored in the web interface
* `Spacing (micrometer), used only when 'Keep order + set spacing' is selected` - this parameter is ignored in the web interface.

After clicking OK, this window appears:

![DeepSlice step 0](/assets/img/fiji_deepslice_0.png)

Next, upload your dataset on the DeepSlice webpage:

![DeepSlice web interface](/assets/img/deepslice_web.png)

You can drag and drop the content of your dataset folder into this page, and then submit the task.

:::{hint} Check `Slower but more accurate results` for better outcomes. If your slices are evenly spaced, select `Use section numbers` and `Normalise section angles.` 
:::

After registration, download the resulting JSON file, place it in the result folder, and confirm in the ABBA interface. The slices will be adjusted according to the new alignment.

**Before**

![Before deepslice](/assets/img/fiji_before_deepslice.png)

**After**

![After deepslice](/assets/img/fiji_after_deepslice.png)

You can further refine the registration using ABBA's non-linear tools.

### Using DeepSlice locally in ABBA

If you have installed DeepSlice locally using [this guide](https://github.com/BIOP/ijl-utilities-wrappers), you can run DeepSlice directly in ABBA. The Windows installer usually configures everything for you.

Check DeepSlice’s path by running `DeepSlice > DeepSlice setup...`:

![ABBA DeepSlice setup](/assets/img/fiji_deepslice_setup.png)

and select the proper folder containing the conda environment for DeepSlice (if you used the ABBA installer for windows, do not touch it, it should already be set correctly).

Then, to run DeepSlice locally, select the slices you want to register and run `Align > ABBA - DeepSlice registration (local)`. This window will pop-up:

![ABBA DeepSlice options](/assets/img/fiji_deepslice_options.png)

* `Slices channels, 0-based, comma separated, '*' for all channels` - used to select the channels you want to export to DeepSlice. You can for instance export a nuclear channel only. You can export the first and third channel by writing `0,2`. Usually, a RGB image contains only one channel.
* `Allow change of atlas slicing angle` - When checked, ABBA will adapt the atlas slicing angle based on the median slicing angles given by DeepSlice. If you don't want to modify the atlas slicing angle, you can uncheck this box.
* `Average of several models (slower)` - run DeepSlice two times with different models in order to improve the registration results.
* `Post_processing` - this parameter can be set as:
    * `Keep order`: maintain the current order of the sections
    * `Keep order + ensure regular spacing`: maintain the current order of the sections and separate them by a constant value, which is guessed by DeepSlice
    * `Keep order + set spacing (parameter below)`: maintain the current order of the sections and separate them by a constant value, which is set by you, according to the parameter below:
* `Spacing (micrometer), used only when 'Keep order + set spacing' is selected` - the output spacing between selected sections if `Keep order + set spacing (parameter below)` is selected

## Slices registration | XY-Axis

After positioning the slices along the Z-axis and correcting their orientation, the next step is to register the slices to the atlas in 2D along the XY-axis. This step can be performed either manually or automatically.

:::{note}
For automatic registration, ABBA utilizes [elastix](https://github.com/SuperElastix/elastix), a powerful tool for medical image registration, to align the slices with the atlas in 2D automatically. Elastix applies pre-configured registration parameters, leveraging the known calibration of the slices and the atlas's physical voxel size to minimize the need for manual parameter tuning.

The key metric used during the registration process is the [Mattes mutual information metric](https://doi.org/10.1109/TMI.2003.809072). This metric is robust for registering images across different modalities, such as DAPI vs. Nissl, or autofluorescence images. 
:::

:::{warning} 
If your image file format does not support multiple resolution levels (pyramids, multiresolution), ABBA may struggle to downsample the images properly, which could result in poor registration performance. You can check the option `show registration results as ImagePlus` to inspect how the slice and atlas are being downsampled during the registration. 
:::

:::{note}
For manual alignment, ABBA integrates Fiji's [BigWarp](https://imagej.github.io/plugins/bigwarp), which allows for precise manual placement of landmarks on both the slice and the atlas. BigWarp provides a flexible interface to adjust the registration and correct any errors from the automated process or to handle problematic slices.
:::

### Registration Workflow and Status Indicators

When you initiate a registration task for a slice, a status indicator appears beneath the slice handle to show the progress of the registration process. The indicator is circular for automatic registrations and rectangular for manual ones. The color changes according to the job’s status:

- Red: Registration not started
- Orange: Registration in progress
- Green: Registration complete

![Slice registration example](/assets/gif/fiji_register_affine_spline.gif)

ABBA is designed to handle multiple registrations in parallel. Depending on your computer's resources, it can run between 4 to 128 registrations at once. You can monitor system performance and CPU usage by enabling the Resources Monitor via the `Cards > Add resources monitor` menu.

The following sequence demonstrates the registration of 80 sections, with the following automated steps for each slice:

* Auto affine registration (DAPI vs. Nissl)
* Auto spline registration (16 points, DAPI vs. Nissl)
* Auto spline registration (16 points, autofluorescence vs. autofluorescence)

![Multi slice registration sequence](/assets/gif/fiji_progression_registration.gif)

(real time ~ 10 min)

It is possible (and advised) to perform several successive registration. You will usually start by an affine registration followed by one or two spline registrations. For 'difficult slices' where the automated registration result are bad, you can either start by a manual registration to facilitate a following automated registration, or, alternatively, you can directly edit the result of a spline transform, in order to improve it and even to add landmarks in regions in which you are more interested.

:::{warning}
If your slice contains broken or missing regions, it can be challenging or even impossible to achieve a perfect registration. ABBA may not handle discontinuous deformations well.
:::

### Affine registration (Automated)

Affine registration is the first step in aligning your dataset slices to the atlas. This process involves scaling, rotating, and translating your slices to match the atlas while preserving their relative proportions. To initiate an affine registration, select the slices you want to register and go to the top menu bar: `Align > ABBA - Elastix Registration (Affine)`.

In the registration dialog, you’ll be asked to select channels from both the atlas and your dataset slices. A common starting point is to use the DAPI channel from your sections and match it with the Nissl channel (channel 0) from the atlas. This pairing often provides a good basis for the first registration.

![Affine elastix registration](/assets/img/fiji_elastix_affine_registration.png)

ABBA supports multichannel registration, where each selected channel contributes equally to the cost function optimized during the alignment process. This is especially useful if your dataset contains channels with distinct features, such as autofluorescence, which may align well with specific atlas channels.

For example, you may have:

* Channel 0 (DAPI) matching the Nissl channel of the atlas.
* Channel 1 with autofluorescence matching the Ara channel of the atlas.

By combining these channels, the registration process becomes more robust.

![Multi Channels](/assets/img/fiji_registration_multichannel_images.png)

To set up a multichannel registration, you can specify multiple channels for both the sections and the atlas, as shown below:

![Affine elastix registration multi channel](/assets/img/fiji_elastix_affine_registration_multichannel.png)

If necessary, you can even repeat channels in the registration parameters. For example, if channels 1 and 3 in your dataset both contain nuclear signals, you can set the registration parameters as follows:

![Affine elastix registration multi channel other](/assets/img/fiji_elastix_affine_registration_multichannel_other.png)

A few extra options are available:
* `Registration re-sampling (micrometers)` specified in micrometer, is the pixel size of the images that will be send to Elastix for the registration task. Check  `Show registration results as ImagePlus` to see how the resampled images look like.
* `Show registration results as ImagePlus`, if checked, will display the raw data used for elastix registration
* `Background offset value` this parameter is obsolete, thus not taken into account anymore.

### Spline registration (Automated)

Spline registration is a more advanced form of alignment that allows for non-linear transformations. You can perform a spline registration by selecting the slices you want to register and going to the top menu bar: `Align > ABBA - Elastix Registration (Spline)`.

![Spline registration parameters](/assets/img/fiji_elastix_spline_registration.png)

During spline registration, the image is divided into a grid, where the number of control points along the X-axis determines the flexibility of the transformation. The grid creates spline-based transformations between your slice and the atlas, allowing for local adjustments that are not possible with affine registration.

The number of control points directly affects the registration's flexibility. It is recommended to choose a value between 5 (resulting in 25 total landmarks) and 20 (resulting in 400 total landmarks). A higher number of control points can provide more flexibility, but it may also risk overfitting if the underlying structure is not consistent across the slice and the atlas.

### BigWarp registration (Manual)

If you want full control over the registration process, you can use [BigWarp](https://imagej.github.io/plugins/bigwarp) for manual registration. This method allows you to place your own landmarks between the atlas and the slice, giving you precise control over the alignment. Since this process is manual, you will need to register slices one by one.

### Editing a registration

If the last registration performed on a slice is either a BigWarp or spline registration, it can be manually edited. To do so, select the slice you want to edit, and in the top menu bar, go to: `Align > ABBA - Edit Last Registration`.

:::{warning} If you select many slices before clicking "Edit Last Registration," each slice's registration will be opened for editing in sequence. Make sure this is what you intend before proceeding! 
:::

This process will open the BigWarp interface, where the landmarks from the previous registration will already be in place. You can modify or add landmarks using the standard BigWarp commands summarized below. Once you finish editing, close the BigWarp window, and the updated result will automatically appear in the ABBA interface. Note that changes cannot be undone, so ensure you're happy with the transformation before closing.

BigWarp commands summary:
* `space` = toggle for landmark mode
* `ctrl + left click` = pin a new landmark on both the fixed (atlas) and the moving (section) image.
* `drag + left click` = in landmark mode, drag an existing landmark
* `f` = display fused transform and fixed image (toggle)
* `t` = transform the image or not (toggle)

You can check [BigWarp documentation](https://imagej.net/plugins/bigwarp) for more information about its interface, or look at the [relevant part in the youtube tutorial](https://youtu.be/sERGONVw4zE?t=2534s).

After editing a registration, you can export it again (to QuPath for instance), and reload it.

![Bigwarp transform](/assets/gif/fiji_bigwarp_edit.gif)

#### Canceling / removing a XY registration

If you're not satisfied with a registration result, you can undo it for the selected slices by:

* Clicking in the top menu bar: `Align > ABBA - Remove Last Registration`
* Or right-clicking in the ABBA viewer: `Remove Last Registration`

This action can be reversed, restoring the previous registration.

#### Applying the registration sequence from one slice to another

See [the use case in this issue](https://github.com/BIOP/ijp-imagetoatlas/issues/174). Suppose you want to duplicate the registration sequence from one slice to another. It is possible with the command `ABBA - Copy and Apply Registration`:

![fiji_copy_apply_registration.png](/assets/img/fiji_copy_apply_registration.png)

### Browsing registration steps

To quickly review the registration steps for a slice, use the controls in the `Display & Navigation` card:

* `View Previous [P]`: Go back to the previous registration step
* `View Next [N]`: Move to the next registration step

The registration indicators will turn from green to gray as you step through and review the different stages.

## Development - adding a registration method of your own

The registration methods (BigWarp, Elastix spline, affine...) are plugins automatically discovered by ABBA. While the documentation is lacking for the moment, it is possible to make a registration plugin of your own and use it in ABBA.

## Registration workflow example

A typical registration may be obtained using the following successive steps, performed on all slices:

* affine registration on DAPI vs Atlas Nissl (Ch 0) + Autofluorescence vs Atlas Ara (Ch. 1)
* spline registration on DAPI vs Atlas Nissl (Ch 0) + Autofluorescent channel vs Atlas Autofluorescent (Ch 1) (15 control points)

This takes about 10 minutes for 50 slices on a laptop.

# Fiji - Saving / Opening registrations results

At each step of the workflow, you can save the current state of your work (as long as no job is being processed).

To save your project, you can click, in the top menu bar `File > ABBA - Save State (+View)`. An `.abba` extension will be automatically added to the filename. This abba file in fact a set of text files zipped together.

All files are text files, which are fast to save and rather small (in comparison to the images...). So do not hesitate to save multiple successive files all along your workflow. Consider your work done when you have obtained regions in QuPath, but the ABBA state file has less guarantee on the long term.

To open a project where you left it, it is compulsory to close ABBA session and restart it. Once restarted, click in the top menu bar `File > ABBA - Load State (+View)`, and select your previously saved `.abba` file.

:::{warning}
If you move your image files, your qupath project, or the other files associated to the state file, ABBA may not be able to find your images because absolute file path are used. If you opened images from a QuPath project, fix URIs in QuPath first before reopening ABBA.
:::