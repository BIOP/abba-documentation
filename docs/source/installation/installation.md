# Installation

ABBA is a Fiji plugin. There are four ways to get it: they all run the same ABBA, with the same window.

| | What you get | Choose it if |
|---|---|---|
| [With an AI assistant](#install-assistant) (recommended) | ABBA in its own Fiji, driven by an assistant in VS Code or another AI application. Its window stays on your screen: you follow along and take over at any time. | You want an assistant to run the registration with you, and a script that replays it. |
| [ABBA installer](#install-installer) | ABBA in its own Fiji, started from an **ABBA** shortcut. | You have no Fiji, you prepare a workshop or an offline computer, or you install ABBA for every user of a shared Windows computer. |
| [In your Fiji](#install-fiji) | ABBA in the Fiji you already use, updated with it. | You already use Fiji and want ABBA next to your other plugins. |
| [From Python](#install-python) | ABBA from Python scripts and notebooks (`abba_python`). | You script your analyses in Python. Not for ABBA's window on macOS. |

The assistant and the installer run a **pinned** environment: the same ABBA, Fiji and Java on every computer,
without touching a Fiji you may already have.

Whatever the way, DeepSlice, Elastix and BrainGlobe are installed by ABBA itself, in their own Python environments,
the first time you use them: this needs an internet connection and takes a few minutes (DeepSlice alone is about
3 GB). Nothing to configure: no conda, no elastix executable, no paths to set. DeepSlice and Elastix need an
Apple-silicon Mac: they cannot run on Intel Macs, where ABBA itself still runs.

You will also want [QuPath and its ABBA extension](#install-qupath), to prepare your slices and analyse them once
registered.

(install-assistant)=
## With an AI assistant

`abba-mcp` is an [MCP](https://modelcontextprotocol.io) server: it lets an AI assistant drive ABBA. The assistant
runs ABBA's commands, looks at what they produced, and once the result is right saves the session (`.abba` state
file) and a Groovy script that replays every step. ABBA's window opens on your screen as usual: you can select
slices for the assistant, correct its work, or carry on by hand.

:::{note}
abba-mcp is experimental. Reports and suggestions are welcome on the [image.sc forum](https://forum.image.sc/tag/abba).
:::

### Before you start

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), which runs the server:

- Windows, in a PowerShell terminal: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- macOS and Linux, in a terminal: `curl -LsSf https://astral.sh/uv/install.sh | sh`

Java, Fiji and ABBA are downloaded for you on the first run.

### VS Code

In [VS Code](https://code.visualstudio.com/), the assistant is GitHub Copilot's chat, in **Agent** mode. Once uv
is installed, click:

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_ABBA_MCP-0098FF?logo=visualstudiocode)](https://vscode.dev/redirect/mcp/install?name=abba&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22abba-mcp%22%5D%7D)

VS Code asks to confirm the installation of the `abba` server. Or, from a terminal:

```
code --add-mcp '{"name":"abba","command":"uvx","args":["abba-mcp"]}'
```

Then open Copilot's chat, choose **Agent** mode and a model that reads images (the assistant looks at pictures of
your slices), and ask, for example: *register the slices of my QuPath project `D:\data\mouse1\project.qpproj` to
the Allen mouse brain atlas*.

### Claude, Codex and other assistants

- **Claude Desktop**: download `abba-mcp-<version>.mcpb` from the
  [abba-mcp releases](https://github.com/unige-biochem/abba-mcp/releases) and double-click it.
- **Claude Code**: `claude mcp add abba -- uvx abba-mcp`
- **Codex** (command line, IDE extension) and the **ChatGPT desktop app**, which shares Codex's configuration:
  `codex mcp add abba -- uvx abba-mcp`. ChatGPT on the web cannot start a local server like this one.
- **Any other application** that starts local MCP servers (Cursor, Gemini CLI...): the server talks MCP over
  stdio, command `uvx`, arguments `abba-mcp`. Most applications take this in their MCP settings:

  ```json
  {
    "mcpServers": {
      "abba": {
        "command": "uvx",
        "args": ["abba-mcp"]
      }
    }
  }
  ```

The server tells the assistant how to work with ABBA. Some applications do not pass these instructions on: if the
assistant seems not to know how to proceed, ask it to read `guides/abba.md` with the `abba_docs_read` tool first.

### First run

The first time the assistant uses Fiji, Java, Fiji and ABBA are downloaded, then started: allow several minutes.
Meanwhile the assistant is told that Fiji is starting, and tries again. Later starts are much faster.

The server's version is the ABBA version it runs, with `.post1`, `.post2`... for a fix of the server alone:
`uvx abba-mcp` runs the latest release, `uvx abba-mcp@0.25.0` a given one. Its Fiji, its log (`fiji.log`) and its
files are in `~/.abba-mcp` (the `ABBA_MCP_HOME` environment variable sets another folder); your own Fiji is
neither used nor modified.

### Without a window

For a server or a remote machine, set the environment variable `ABBA_MCP_HEADLESS=true` for the server: ABBA then
runs without a window, the assistant shows you pictures instead, and manual registrations are not available.

- In the JSON settings: `"env": {"ABBA_MCP_HEADLESS": "true"}` next to `"args"`.
- `claude mcp add abba -e ABBA_MCP_HEADLESS=true -- uvx abba-mcp`, or `codex mcp add abba --env ABBA_MCP_HEADLESS=true -- uvx abba-mcp`.
- In Claude Desktop: turn on *Run Fiji without a window* in the extension's settings.

### Privacy

What the assistant looks at (pictures of your slices, the session state, file names) is sent to your AI provider,
as anything else you show it. Fiji itself can only be reached from your own computer (port 9090 on `127.0.0.1`).

### If something goes wrong

- **"The Fiji on port 9090 runs ..."**: another Fiji with an MCP server is already running (your own, or one
  started by another version of abba-mcp). Close it and ask again.
- **Fiji does not start**: read its log, `fiji.log` in `~/.abba-mcp`.

(install-installer)=
## ABBA installer

The installer sets up ABBA in its own Fiji, without installing Fiji, Java or Python first: ABBA 0.25.0, Fiji
2.18.0, Java 21 (Zulu). Your own Fiji, if you have one, is neither used nor modified.

Download `ABBA-0.25.0.zip` from the [ABBA 0.25.0 release](https://github.com/BIOP/ijp-imagetoatlas/releases/tag/0.25.0)
and extract it. Then:

| | **For you** | **For every user** (Windows) |
|---|---|---|
| Run | `Install for me.cmd` (macOS, Linux: `bash install-for-me.sh`) | `Install for all users.cmd` (asks for administrator rights) |
| Installs into | the extracted folder | `C:\Program Files\ABBA` |
| Java, ABBA, Fiji, DeepSlice, Elastix, BrainGlobe | **Install everything** in the window, or on first use | all downloaded during the installation |
| Then | the **ABBA** shortcut: next to the installer, in your Start Menu, on your Desktop | the **ABBA** shortcut in every user's Start Menu and Desktop |

Both open the same window, with a progress bar. Everything takes about 6 GB, and 10 to 20 minutes depending on
the connection.

![The ABBA installer window](/assets/img/abba_installer_window.png)

:::{note}
The installer is new: on macOS and Linux it has not been tested yet, reports are welcome.
:::

### For you

`Install for me.cmd` installs [uv](https://docs.astral.sh/uv/) if it is missing (it builds the launcher's Python
environment, and is the only thing installed outside the folder), writes the **ABBA** shortcuts, and opens the
window:

- **Install everything** downloads Java, ABBA, Fiji, DeepSlice, Elastix and BrainGlobe now: do it before a
  workshop or before going offline. *Choose…* leaves out what you don't need.
- Or **Start ABBA** straight away: what ABBA needs is downloaded when first used.

Once installed, the window opens on **Start ABBA**, which starts Fiji: then [start ABBA](../guide/start_and_import.md)
as in any Fiji. Closing the installer window leaves Fiji open.

### For every user (Windows)

`Install for all users.cmd` installs into `C:\Program Files\ABBA` (or the folder given as its argument). It
downloads everything during the installation, so that users have nothing to fetch. Users can read that folder but
not write to it; their window only offers **Start ABBA**.

Atlases are downloaded when a user first opens one, into `C:\ProgramData\ABBA`, which every user can write: an
atlas downloaded by one user is there for all. To keep them elsewhere (a larger disk), set `ABBA_SHARED_DATA`
before installing.

For unattended deployment, `/quiet` installs without the window, printing the progress instead; the exit code
says whether it worked:

```bat
set ABBA_SHARED_DATA=D:\ABBA
"Install for all users.cmd" /quiet
```

### Without internet

Also download `ABBA-0.25.0-jars.zip` (ABBA and Fiji's jars) from the same release and put it next to the
installer, without extracting it. Java and the Python environments still need a connection: install once on a
connected computer, or prepare the computer before going offline.

### Update, uninstall

To update, run the installer of the new version. To uninstall, delete the installation folder and the two
shortcuts and, for every user, `C:\ProgramData\ABBA` with its atlases.

### Command line

The window's actions, for a terminal or a script, from the extracted folder:

```bash
uv run abba start                    # start Fiji with ABBA
uv run abba start --memory 16G       # Java's maximum memory (default: from the computer's memory)
uv run abba prepare --all            # install everything; or --deepslice --elastix --brainglobe
uv run abba info                     # versions, and where everything is
```

(install-fiji)=
## In your Fiji

ABBA needs Java 21, which an up-to-date Fiji has.

1. If Fiji is not installed yet, download it from [fiji.sc](https://fiji.sc/) and install it. Otherwise, update it
   with {menuselection}`Help --> Update...`. If your Fiji still runs an older Java, download a new Fiji
   instead.
2. Click {menuselection}`Help --> Update... --> Manage update sites`, tick the `UNIGE-Biochem` update site, then
   click `Apply and close` and `Apply changes`.
3. Restart Fiji, then [start ABBA](../guide/start_and_import.md).

ABBA is then updated with Fiji, through {menuselection}`Help --> Update...`.

:::{note}
Up to version 0.11, ABBA came from the `PTBIOP` update site. ABBA is now on `UNIGE-Biochem`: PTBIOP stays at
ABBA 0.11.1 for now, and ABBA will be removed from it. Keep PTBIOP if you use its other plugins, but tick
`UNIGE-Biochem` to get ABBA.
:::

(install-python)=
## From Python

[abba_python](https://github.com/BIOP/abba_python) runs ABBA from Python: every ABBA command is a Python method,
and Fiji with ABBA's window can be started from Python too. You need Python 3.10 or later; Java and ABBA are
downloaded on the first run (a few hundred MB).

```
pip install abba-python
```

`pip install` works in any environment: a virtual environment (`uv venv`), a conda environment... With
[pixi](https://pixi.sh):

```
pixi init abba-project
cd abba-project
pixi add python=3.13
pixi add --pypi abba-python
```

Then, in Python (`pixi run python` with pixi):

```python
from abba_python import abba
ij = abba.start_imagej()   # Fiji with ABBA, and its window
```

:::{warning}
On macOS, ABBA's window does not work when started from Python. Scripts that do not show it work; for the
window, use one of the other ways.
:::

How to script ABBA from Python is described in the [abba_python repository](https://github.com/BIOP/abba_python).

(install-qupath)=
## QuPath and its ABBA extension

ABBA is best used with [QuPath](https://qupath.github.io/): a QuPath project holds the slices to register, and the
registration results are imported back into QuPath, to detect and count cells per atlas region. ABBA reads QuPath
projects by itself; importing its results into QuPath needs the ABBA extension for QuPath 0.7:

1. Install [QuPath 0.7](https://qupath.github.io/).
2. Click {menuselection}`Extensions --> Manage extensions`, then `Manage extension catalogs`, and add the catalog
   `https://github.com/BIOP/qupath-biop-catalog`.
3. Install the ABBA extension with its (+) button, and restart QuPath.
