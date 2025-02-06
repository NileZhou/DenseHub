search for help: [vscode_docs](https://code.visualstudio.com/docs/editor/codebasics)

# Usually Shortcut

## windows
Ctrl + P:  quick search file/directory name, like "Shift Shift" in JB


## mac
Shift + option + F: beautify code
Command + J: show/hide bottom panel


# General Settings

1. Ctrl + Shift + P (MAC: Command + Shift + P)
2. in the input textbox, input "settings"
3. choose [Preferences: Open User Settings (JSON)]

```json
{
    // add indentations in file structure tree
    "workbench.tree.indent": 20,
}

```

# Extensions



# bitter lesson
Don't use the extension:   
**Office Viewer (Markdown Editor)**

It will cause data loss in some conditions.


# Shortcuts settings


1. Ctrl+Shift+P
2. input: Preferences: Open Keyboard Shortcuts (JSON)  then press return
3. edit the keybindings.json:

```
// Place your key bindings in this file to override the defaults
[
    {
        "key": "shift+alt+left",
        "command": "workbench.action.navigateBack",
        "when": "canNavigateBack"
    },
    {
        "key": "ctrl+alt+-",
        "command": "-workbench.action.navigateBack",
        "when": "canNavigateBack"
    },
    {
        "key": "shift+alt+right",
        "command": "workbench.action.navigateForward",
        "when": "canNavigateForward"
    },
    {
        "key": "ctrl+shift+-",
        "command": "-workbench.action.navigateForward",
        "when": "canNavigateForward"
    }
]
```


# MarkDown Visual Editor

Support for editing while preview

https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-office&ssr=false#overview

in vscode, press Ctrl + P then input:

```
ext install cweijan.vscode-office
```

# Markdown All in One

ext install yzhang.markdown-all-in-one


# Autosave

```
{
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
}
```
