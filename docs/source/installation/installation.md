# Installation

ABBA comprises a Fiji plugin, an extension for QuPath, and external software for automating the registration process.

:::{hint}
The QuPath extension, while optional, is highly recommended. It simplifies dataset definition and post-registration analysis.
:::

# Fiji + ABBA plugin installation

:::{tip} For Windows users, [a standalone installer is available](https://github.com/BIOP/ijp-imagetoatlas/releases/), which simplifies the installation process. 
:::

ABBA can be installed as a Fiji plugin, but additional components are needed to unlock its full functionality. In particular, ABBA performs best with the following components:

* [DeepSlice](https://www.deepslice.com.au/): A deep-learning-based method for automatic registration of coronal sections to mouse and rat brain atlases.
* [elastix/transformix](https://github.com/SuperElastix/elastix): Software used for automating 2D in-plane registration.
* [BrainGlobe](https://brainglobe.info/about.html): A Python library that standardizes access to various brain atlases.

There are three primary ways to install ABBA, each corresponding to different setups:
* Using the Windows standalone installer
* Using [Fiji](https://fiji.sc/) (available for Windows, macOS, and Linux)
* Using Python with a pip dependency [abba_python](https://pypi.org/project/abba-python/)

The table below summarizes the functionality available for each installation method across different operating systems:

| Installation mode                                                                       | Headless | GUI | Mouse/Rat atlas | Brainglobe Atlas | DeepSlice (Local) |
|-----------------------------------------------------------------------------------------|----------|-----|-----------------|------------------|-------------------|
| Opt 1. ABBA installer <br/>(Win)                                                        | [x]      | [x] | [x]             | [x]              | [x]               |
| Opt 2. Fiji <br/>+ PTBIOP update site <br/>(Win, Mac, Linux)                            | [x]      | [x] | [x]             |                  |                   |
| Opt 2. Fiji <br/>+ PTBIOP update site <br/>+ DeepSlice conda env <br/>(Win, Mac, Linux) | [x]      | [x] | [x]             |                  | [x]               |
| Opt 3. abba_python <br/>(Win, Linux)                                                    | [x]      | [x] | [x]             | [x]              |                   |
| Opt 3. abba_python <br/>+ DeepSlice conda env <br/>(Win, Linux)                         | [x]      | [x] | [x]             | [x]              | [x]               |
| Opt 3. abba_python <br/>(Mac)                                                           | [x]      |     | [x]             | [x]              |                   |
| Opt 3. abba_python <br/>+ DeepSlice conda env <br/>(Mac)                                | [x]      |     | [x]             | [x]              | [x]               |

## Option 1 - Installing the ABBA plugin using the Windows installer

This is the simplest option, available only for Windows users.

[https://github.com/BIOP/ijp-imagetoatlas/releases/latest](https://github.com/BIOP/ijp-imagetoatlas/releases/latest)

Requirements:

* An internet connection is required during installation to download necessary dependencies from PyPI, including [deepslice](https://pypi.org/project/DeepSlice/), [abba-python](https://pypi.org/project/abba-python/), and [brainglobe-api](https://pypi.org/project/brainglobe-atlasapi/).
* The first time you run ABBA, you will need to download the atlas you intend to use.

## Option 2 - Installing the ABBA plugin in Fiji

### Step 1. Download and install Fiji
If Fiji is not already installed, download and install it from [fiji.sc](https://fiji.sc/).

### Step 2. Activate the PTBIOP update site
* Click `Help > Update... > Manage update sites`
* Check the box for `PTBIOP`
* Click `Apply and close` then `Apply changes`
* Restart Fiji

### Step 3. (Optional) Activate the OMERO 5.5-5.6 update site
* Click `Help > Update... > Manage update sites`
* Tick the checkbox `OMERO 5.5-5.6`
* Click `Apply and close` then `Apply changes`
* Restart Fiji

### Step 4. Install elastix/transformix

ABBA relies on  [elastix](https://github.com/SuperElastix/elastix) for 2D in-plane registration. Elastix is independent of Fiji and must be installed separately.
* Download [elastix version 5.2.0](https://github.com/SuperElastix/elastix/releases/tag/5.2.0) for your operating system.
* Extract it to a convenient location (`C:` on Windows, `Applications` on macOS).

#### Windows
Install [Visual C++ redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170), (choose `vc_redist.x64.exe` for a 64-bit system). 

:::{warning}
If you are updating Fiji and switch from elastix 5.0.1 to elastix 5.2.0, make sure you have the latest version installed. Otherwise elastix will not work.
:::

#### Mac
Since macOS treats elastix and transformix as software from "unknown developers," you need to [create security exceptions](https://support.apple.com/en-hk/guide/mac-help/mh40616/mac) for both executables to bypass repeated warnings.

#### Linux
No special steps are required.

### Step 5. Set `elastix` and `transformix` Paths in Fiji
* Run Fiji and execute `Plugins › BIOP › Set and Check Wrappers`.
* Specify the paths for the elastix and transformix executables. For instance:

![Setting elastix and transformix path in Fiji](../assets/img/fiji_elastix_transformix_path.png)

You should see confirmation messages like:

* [INFO] Transformix -> set :-)
* Elastix -> set :-)

To verify elastix is working, you can run [this test script](https://gist.github.com/NicoKiaru/b91f9f3f0069b765a49b5d4629a8b1c7) in Fiji. Save the file with a .groovy extension, open it in Fiji, and run it.

### Step 6. (Optional) Installing DeepSlice locally

While you can use the web-based DeepSlice interface, installing it locally can streamline the registration process.

To install DeepSlice locally, please follow the instructions specified in the [BIOP wrappers repository](https://github.com/BIOP/ijl-utilities-wrappers#deepslice). In brief, the installation consists of:
* installing miniforge
* creating a conda environment for deepslice
* adding conda to the PATH environment variable (windows)
* specifying the conda environment location in Fiji

## Option 3 - Installing ABBA plugin in python

ABBA is available as a [PyPI dependency](https://pypi.org/project/abba-python/). For installation instructions and startup commands, refer to the [abba_python README](https://pypi.org/project/abba-python/).

# QuPath + ABBA extension installation

1. Install [QuPath](https://qupath.github.io/).
2. Download the latest [ABBA extension zip file](https://github.com/BIOP/qupath-extension-abba/releases/latest) (named `qupath-extension-abba-x.y.z.zip`).
3. Unzip it.
4. Drag and drop the .jar files into QuPath's main window.

:::{note}
If you're using OMERO for your data, you'll need the [QuPath OMERO RAW extension](https://github.com/BIOP/qupath-extension-biop-omero). Follow the [installation guide](https://github.com/BIOP/qupath-extension-biop-omero/blob/omero-raw/README.md).
:::

5. Restart QuPath. You should now see the following extensions under `Extensions>Manage extensions`:
* ABBA
* Image Combiner Warpy
* Warpy
* OMERO BIOP
