# Known issues & frequently asked questions

## All ABBA related questions on forum.image.sc

You can browse through all the questions asked about ABBA in the [image.sc forum with the tag #abba](https://forum.image.sc/tag/abba). Maybe you'll find an answer to your question ?

If you want to post a question on this forum, the recommended way (if you managed to install ABBA), is to create an account on forum.image.sc and then to click {menuselection}`Help --> Ask For Help In The Forum (Web)` in the ABBA window: there will be some details about your installation in your forum question automatically added.

## Sections are gigantic when opened in ABBA

Most probably, your images are either not calibrated, or bio-formats cannot read the calibration. If you are using QuPath, you can [override the pixel size in QuPath **BEFORE** opening the project in ABBA](guide/prepare_qupath_project.md), or, if your files are not pyramidal, you can convert your files to pyramidal OME-Tiff by using [Kheops](https://github.com/BIOP/ijp-kheops) and set the correct voxel size in the conversion process.

## I only have hemi-brain sections. Can I use ABBA ?

Yes. You can turn hemi-sections into virtual full sections with {menuselection}`Slices --> Mirror Slices`, register these virtual sections, and remove the mirroring at the end with {menuselection}`Slices --> Un-Mirror Slices` (see [Hemi-sections](#hemi-sections)). You can also restrict the registrations to a rectangular [region of interest](#region-of-interest).

## I can't start any elastix or DeepSlice registration
Since ABBA 0.24, elastix and DeepSlice are installed automatically by ABBA the first time they are used, in a dedicated environment on your computer. This first installation requires an internet connection and can take a few minutes. If it fails, check the error message and the Fiji console (`Window > Console`), then report the problem and the error logs in the forum with {menuselection}`Help --> Ask For Help In The Forum (Web)`.

## I cannot see any image after I import my QuPath project

Since ABBA 0.24, slices are displayed with all their channels when imported. If you still see nothing, the slices or their channels may have been hidden, or their display range may not fit your images: select all the slices in the table of the `Slices Display` card, use the header row to make them and their channels visible, and adjust the display range (see [Display slices](guide/select_display_slices.md#display-slices)). Check also that your images are calibrated: uncalibrated images may be displayed far from the atlas (see above).

## I want to use another atlas than the ones available

The atlases currently available are:
* the [adult Allen Mouse Brain atlas CCFv3](https://zenodo.org/record/4486659/#.YngkMlRBziE), built into ABBA;
* the [Waxholm Space atlas of the Sprague Dawley Rat Brain](https://zenodo.org/record/5644162#.YngkTVRBziE), built into ABBA;
* all [BrainGlobe](https://brainglobe.info/documentation/brainglobe-atlasapi/index.html) atlases, downloaded on demand (see [Choose an atlas](guide/start_and_import.md#choose-an-atlas)).

There are other atlases, of course, but adding them in ABBA still requires some work because there is no unified way of accessing labels, properties and hierarchical structure (unless it is implemented within BrainGlobe). This is an effort I can make, but there needs to be:
1. several users needing it - and you can do your request through {menuselection}`Help --> Give Your Feedback (Web)` in the ABBA window
2. If not implemented in BrainGlobe, the atlas data need to be publicly accessible and shareable. I need to be allowed to repackage it in a different file format and make it accessible through Zenodo like the other ones.
3. ABBA can't swallow all atlases, there are a number of atlases which consist of well annotated 2d sections, but which are not fully 3D. Such atlases can't be used within ABBA.
4. I need time.

There's also [a script](https://forum.image.sc/t/custom-atlas-in-abba/77206) that allows to create a fake atlas from an image, but no ontology is imported.

Check also [this forum post](https://forum.image.sc/t/customizing-atlas-labels-of-ccf2017-for-use-in-abba/78523/5) if you want to do modifications to the original Allen Brain CCFv3 atlas.

## I can't open my state file anymore

This issue occurred many times. In most cases, the state can be recovered by editing the ABBA state file(s). Here are the various causes of the issue:
* files being moved around (or drive letter being changed) ([post](https://forum.image.sc/t/issue-loading-saved-states/75223/7))
* entries being deleted from QuPath project after an ABBA state was created ([post](https://forum.image.sc/t/help-for-abba-in-fiji-could-not-load-saved-state/71477/7))
* Bio-Formats memoization [storing the absolute file path of an old location](https://github.com/BIOP/ijp-imagetoatlas/issues/154#issuecomment-1419904570)
* before ABBA v0.5, the abba state was stored in three different files. Any of them missing was a problem

Any project created after ABBA v0.5+ will be less susceptible to these issues:
* an ABBA state is not split in three files anymore, but stored [in a zipped file with an `.abba` extension](reference/state_files.md). This also allows to remove some absolute path.
* when required, the absolute path is written as few times as possible, and there's a mechanism that asks users to update their files if their location is not valid anymore.
* if an entry is removed in QuPath, the state file can nonetheless be opened in ABBA.

You should still fix first your file location in QuPath before fixing the QuPath project path in ABBA

Side note: the new state mechanism allows to share much more easily a registration between collaborators, or even with a publication. A few changes in file path, and you're done.
