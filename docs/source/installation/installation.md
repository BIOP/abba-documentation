# Installation

ABBA is an application offering both a graphic user interface (_GUI_) and a command line interface (_CLI_) that works as _plugin_ of [Fiji](https://fiji.sc/), a common image-processing software used in health sciences.

In addition, we also offer a [QuPath](https://qupath.github.io/) extension that helps importing the region annotations that were registered with ABBA.

:::{hint}
The QuPath extension, while optional, is highly recommended. It simplifies dataset definition and post-registration analysis.
:::

## ABBA plugin for Fiji

:::{tip} For Windows users, [a standalone installer is available](https://github.com/BIOP/ijp-imagetoatlas/releases/), which simplifies the installation process. 
:::

ABBA can be directly installed from Fiji's interface as a plugin, but depending from your needs you might want to follow a different installation method to unlock additional functionalities, namely:

<!-- * [elastix/transformix](https://github.com/SuperElastix/elastix): Software used for automating 2D in-plane registration. -->
* [BrainGlobe](https://brainglobe.info/about.html): a Python library that [extends the atlases](https://brainglobe.info/documentation/brainglobe-atlasapi/index.html#atlases-available) available in ABBA.
* [DeepSlice](https://www.deepslice.com.au/): a deep-learning-based method for automatic registration of coronal sections to mouse and rat brain atlases. Its integration with ABBA can work both _online_ (i.e. it uploads your downscaled images to DeepSlice's servers, requiring an internet connection) and _offline_ (i.e. it runs the model locally, on your computer).

There are three methods to control ABBA installation within Fiji:
1. using a standalone installer for Windows;
2. using a [Fiji](https://fiji.sc/) installation;
3. using a Python virtual environment to manage the correct versions of [`abba-python`](https://pypi.org/project/abba-python/), [`brainglobe-atlasapi`](https://pypi.org/project/brainglobe-atlasapi/) and [`deepslice`](https://pypi.org/project/DeepSlice/).

The tables below summarize the functionality available for each installation method across different operating systems:

| Windows                                             | Method 1 | Method 2   | Method 3   |
|-----------------------------------------------------|----------|------------|------------|
| CLI                                                 | ✅       | ✅         | ✅         |
| GUI                                                 | ✅       | ✅         | ✅         |
| Default atlases<br/>(Allen's Mouse & Waxholm's Rat) | ✅       | ✅         | ✅         |
| BrainGlobe atlases                                  | ✅       | ❌         | ✅         |
| DeepSlice (online)                                  | ✅       | ✅         | ✅         |
| DeepSlice (local)                                   | ✅       | _Optional_ | _Optional_ |
 
| Linux                                               | Method 1 | Method 2   | Method 3   |
|-----------------------------------------------------|----------|------------|------------|
| CLI                                                 | ❌       | ✅         | ✅         |
| GUI                                                 | ❌       | ✅         | ✅         |
| Default atlases<br/>(Allen's Mouse & Waxholm's Rat) | ❌       | ✅         | ✅         |
| BrainGlobe atlases                                  | ❌       | ❌         | ✅         |
| DeepSlice (online)                                  | ❌       | ✅         | ✅         |
| DeepSlice (local)                                   | ❌       | _Optional_ | _Optional_ |

| MacOS                                               | Method 1 | Method 2   | Method 3   |
|-----------------------------------------------------|----------|------------|------------|
| CLI                                                 | ❌       | ✅         | ✅         |
| GUI                                                 | ❌       | ✅         | ❌         |
| Default atlases<br/>(Allen's Mouse & Waxholm's Rat) | ❌       | ✅         | ✅         |
| BrainGlobe atlases                                  | ❌       | ❌         | ✅         |
| DeepSlice (online)                                  | ❌       | ✅         | ✅         |
| DeepSlice (local)                                   | ❌       | _Optional_ | _Optional_ |

_NOTE_: an internet connection is required during the installation.

### Method 1 - Windows installer

Windows users can use an [automatic installer](https://github.com/BIOP/ijp-imagetoatlas/releases/latest) that sets everything up into an installation with all optional features enabled. This is the simplest solution, albeit the one receiving updates the least frequently.

### Method 2 - Fiji plugin manager

This method gets updates the fastest, and they can be installed directly using Fiji's Updater (i.e., `Help > Update...`).

#### Step 1. Download and install Fiji
If Fiji is not already installed, download it from [fiji.sc](https://fiji.sc/) and install it.

#### Step 2. Add necessary update site
* click `Help > Update... > Manage update sites`;
* tick the checkbox `PTBIOP`;
* _optional_: tick the checkbox `OMERO 5.5-5.6`\
This step is necessary only if you want to use ABBA on images saved on an [OMERO server](https://www.openmicroscopy.org/omero/);
* click `Apply and close` then `Apply changes`;
* restart Fiji.

#### Step 3. Install elastix/transformix

[elastix](https://elastix.dev/), a toolbox for 2D in-plane registration, is an indipendent program that is executed by ABBA under the hood in order to apply affine and spline transformations to the images.

* download [elastix version 5.2.0](https://github.com/SuperElastix/elastix/releases/tag/5.2.0) for your operating system;
* extract it to a convenient location (e.g., `C:\` on Windows, `/opt/` on Linux, `Applications` on MacOS).

##### Windows
Download [Visual C++ redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) (`vc_redist.x64.exe` for 64-bit systems) and install it. 

:::{warning}
If you are updating Fiji and switch from elastix 5.0.1 to elastix 5.2.0, make sure you have the latest version installed. Otherwise elastix will not work.
:::

##### Linux
No special steps are required.

##### MacOS
Since macOS treats elastix and transformix as software from "unknown developers," you need to [create security exceptions](https://support.apple.com/en-hk/guide/mac-help/mh40616/mac) for both executables to bypass repeated warnings.

#### Step 5. Set elastix paths in Fiji

Now you have to tell Fiji where to find your installation of `elastix` and `transformix` by clicking on `Plugins › BIOP › Elastix > Test elastix`. When asked, specify the paths of `elastix` and `transformix` executables. For instance:

![Setting elastix and transformix path in Fiji](../assets/img/fiji_elastix_transformix_path.png)

In Fiji's console (`Window > Console`, if closed), you should see a confirmation messages like:
```
[INFO] Elastix	->	set :-) 
Transformix	->	set :-) 
```

Lastly, you will be asked to start a registration test. Run it and check its result.
<!-- To verify `elastix` is working, you can run [this test script](https://gist.githubusercontent.com/NicoKiaru/b91f9f3f0069b765a49b5d4629a8b1c7/raw/a64f92467bc354eb45af579b5eb3c5a8a0c466b4/TestRegister.groovy) in Fiji. Save the file with a .groovy extension, open it in Fiji, and run it. -->

#### Step 6. Install DeepSlice locally _[optional]_

While you can use the default web-based DeepSlice interface, installing it locally can streamline the registration process.

To install DeepSlice locally, please follow the instructions specified in the [BIOP wrappers repository](https://github.com/BIOP/ijl-utilities-wrappers#deepslice). In brief, the installation consists of:
* installing miniforge;
* adding conda to the PATH environment variable (Windows only);
* creating a conda environment for `deepslice`;
* specifying the conda environment location in Fiji.

### Method 3 - Installing ABBA plugin in python

ABBA can also be installed within a python environment thanks to [`abba-python`](https://pypi.org/project/abba-python/). This method adds support to [BrainGlobe](https://brainglobe.info/documentation/brainglobe-atlasapi/index.html#atlases-available)'s additional atlases.

For the installation instructions refer to the [project's page](https://github.com/BIOP/abba_python).

## ABBA extension for QuPath

### QuPath 0.6

1. if QuPath is not already installed, [download it](https://qupath.github.io/) and install it;

The ABBA extension is distributed into QuPath via a the QuPath-BIOP catalog.
This catalog is NOT enabled by default in QuPath. In order to add it to the list of available catalogs:

2. Open QuPath
3. Go to **Extensions → Manage extensions**
4. Click **Manage extension catalogs**
5. Enter the catalog URL: `https://github.com/BIOP/qupath-biop-catalog`
6. Browse and install the latest abba extension by clicking its (+) button
7. Make sure to restart QuPath

:::{note}
Note that the BraiAn extension is available via the catalog `https://github.com/carlocastoldi/qupath-extension-braian-catalog`
:::

:::{note}
If you're using OMERO for your data, you'll need to install the QuPath OMERO extension with optional dependencies. 
You need to import your images in OMERO by using the [Ice API](https://github.com/qupath/qupath-extension-omero).
:::

### QuPath 0.5 (legacy - no bug fix)

1. if QuPath is not already installed, [download it](https://qupath.github.io/) and install it;
2. download the version 0.3.3 [ABBA extension](https://github.com/BIOP/qupath-extension-abba/releases/tag/0.3.3) zip file (named `qupath-extension-abba-0.3.3.zip`);
3. unzip it;
4. drag-and-drop the `.jar` files into QuPath's main window;

:::{note}
If you're using OMERO for your data, you'll need the [QuPath OMERO RAW extension](https://github.com/BIOP/qupath-extension-biop-omero). Follow the [installation guide](https://github.com/BIOP/qupath-extension-biop-omero/blob/omero-raw/README.md).
:::

5. Restart QuPath.

You should now see the following extensions under `Extensions > Manage extensions`:
* ABBA
* Image Combiner Warpy
* Warpy
* OMERO BIOP _[optional]_