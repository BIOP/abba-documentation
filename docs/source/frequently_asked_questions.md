
# Known issues & frequently asked questions

## All ABBA related questions on forum.image.sc

You can browse through all the questions asked about ABBA in the [image.sc forum with the tag #abba](https://forum.image.sc/tag/abba). Maybe you'll find an answer to your question ?

If you want to post a question on this forum, the recommended way (if you managed to install ABBA), is to create an account on forum.image.sc and then to run the command `ABBA - Ask for help in the forum` from within Fiji: there will be some details about your installation in your forum question automoatically added.

## Sections are gigantic when opened in ABBA

Most probably, your images are either not calibrated, or bio-formats cannot read the calibration. If you are using QuPath, you can [override the pixel size in QuPath **BEFORE** opening the project in Fiji's ABBA plugin](/tutorial/0_create_qupath_dataset.md), or, if your files are not pyramidal, you can convert your files to pyramidal OME-Tiff by using [Kheops](https://github.com/BIOP/ijp-kheops) and set the correct voxel size in the conversion process.

## I only have hemi-brain sections. Can I use ABBA ?

Yes, you can restrict the registration to a certain rectangular region of interest. Please have a look at [this question](https://forum.image.sc/t/abba-experimental-a-fiji-qupath-workflow-for-mouse-brain-slice-registration-to-the-allen-brain-atlas-ccfv3/54345/15) and the [answer just below](https://forum.image.sc/t/abba-experimental-a-fiji-qupath-workflow-for-mouse-brain-slice-registration-to-the-allen-brain-atlas-ccfv3/54345/16). Also, there is the possibility to [virtually mirror the hemi-section (check point 3)](https://forum.image.sc/t/abba-aligning-big-brains-and-atlases-v0-5-3-released/80732). You can then register the whole 'virtual section', and remove the virtual extra half at the end.

## I can't start any elastix registrations
Either the elastix executable file location is not set, or you are missing a library, or you are missing some access rights. The installation of external dependencies on multiple OS is pain. To narrow down the issue, you can try to look for the command `Test elastix` located in ` Plugins › BIOP › Elastix › Test Elastix `. [It should look like this](https://forum.image.sc/t/abba-experimental-a-fiji-qupath-workflow-for-mouse-brain-slice-registration-to-the-allen-brain-atlas-ccfv3/54345/28). If this did not help you solve the issue, please report the problem and error logs in the forum by using `Help > ABBA - Ask for help in the forum`.

## I cannot see any image after I import my Qupath project

It could be because the slices are invisible by default (for faster loading). Select all the slices in the table and click on the header line to make them visible, as well as the channels you want to see, and increase the contrast if necessary. There is a [step by step documentation accessible here](https://docs.google.com/presentation/d/1c5yG-5Rhz5WlR4Hf9TNVkjqb6yD6oukza8P6vHGVZMw/edit#slide=id.p1), check from slice 53 for the display options.

## I want to use another atlas than the ones available

The atlases currently available are:
* the [adult Allen Mouse Brain atlas CCFv3](https://zenodo.org/record/4486659/#.YngkMlRBziE)
* the [Waxholm Space atlas of the Sprague Dawley Rat Brain V4](https://zenodo.org/record/5644162#.YngkTVRBziE)
* depending on your installation, all [BrainGlobe](https://brainglobe.info/documentation/bg-atlasapi/index.html) atlases

There are other atlases, of course, but adding them in ABBA still requires some work because there is no unified way of accessing labels, properties and hierarchical structure (unless it is implemented within BrainGlobe). This is an effort I can make, but there needs to be:
1. several users needing it - and you can do your request through ABBA `Help > ABBA - Give your feedback`
2. If not implemented in BrainGlobe, the atlas data need to be publicly accessible and shareable. I need to be allowed to repackage it in a different file format and make it accessible through Zenodo like the other ones.
3. ABBA can't swallow all atlases, there are a number of atlases which consists of well annotated 2d sections, but which are not fully 3D. Such atlases can't be used within ABBA.
3. I need time.

There's also [a script](https://forum.image.sc/t/custom-atlas-in-abba/77206) that allows to create a fake atlas from an image, but no ontology is imported.

Check also [this forum post](https://forum.image.sc/t/customizing-atlas-labels-of-ccf2017-for-use-in-abba/78523/5) if you want to do modifications to the original Allen Brain CCFv3 atlas.

## I can't open my state file anymore

This issue occurred many times. In most cases, the state can be recovered by editing the ABBA state file(s). Here are the various causes of the issue:
* files being moved around (or drive letter being changed) ([post](https://forum.image.sc/t/issue-loading-saved-states/75223/7))
* entries being deleted from QuPath project after an ABBA state was created ([post](https://forum.image.sc/t/help-for-abba-in-fiji-could-not-load-saved-state/71477/7))
* Bio-Formats memoization [storing the absolute file path of an old location](https://github.com/BIOP/ijp-imagetoatlas/issues/154#issuecomment-1419904570)
* before ABBA v0.5, the abba state was stored in three different files. Any of them missing was a problem

Any project created after ABBA v0.5+ will be less susceptible to these issues:
* an ABBA state is not split in three files anymore, but stored [in a zipped file with an `.abba` extension](/explanation/registration_storage.md). This also allows to remove some absolute path.
* when required, the absolute path is written as few times as possible, and there's a mechanism that ask users to update their files if their location is not valid anymore.
* if an entry is removed in QuPath, the state file can nonetheless be opened in ABBA.

You should still fix first your file location in QuPath before fixing the QuPath project path in ABBA

Side note: the new state mechanism allow to share much more easily a registration between collaborators, or even with a publication. A few changes in file path, and you're done.
