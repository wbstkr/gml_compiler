# Webby's GML Unpacker

Editing long `.gml` files can be daunting, especially without using gm82. Webby's GML Unpacker simplifies this process by unpacking `.gml` files into a folder of separate scripts, making them easier to manage. Once you've made your edits, you can seamlessly repack them back into the original `.gml` file.

This tool provides both a graphical user interface (GUI) and a command-line interface (CLI) to streamline working with GameMaker Language (GML) script files.


## Features

- Unpack a `.gml` file into a folder of individual script files.
- Pack a folder of scripts back into a `.gml` file.
- Simple graphical interface for easy usage.
- Command-line support for automation.


## Installation

Download the latest release from the [Releases](https://github.com/wbstkr/Webby-GML-Unpacker/releases/latest) section.

For Python users, you can also run the script directly:

```pwsh
python main.py
```


## Usage (Executable)

### Graphical Interface

If no arguments are provided, the GUI will open by default.:

```pwsh
gmlunpacker.exe
```

A simple GUI will appear, allowing you to choose between unpacking or packing `.gml` files.

### Command Line

#### Unpacking a `.gml` file

```pwsh
gmlunpacker.exe -u <file.gml> [output_directory]
```

Example:

```pwsh
gmlunpacker.exe -u my_script.gml extracted_scripts/
```

#### Packing `.gml` scripts into a single file

```pwsh
gmlunpacker.exe -p <input_directory> <output_file.gml>
```

Example:

```pwsh
gmlunpacker.exe -p extracted_scripts/ my_script.gml
```


## Usage (Python)

### Graphical Interface

If no arguments are provided, the GUI will open by default.:

```pwsh
python main.py
```

A simple GUI will appear, allowing you to choose between unpacking or packing `.gml` files.

### Command Line

#### Unpacking a `.gml` file

```pwsh
python main.py -u <file.gml> [output_directory]
```

Example:

```pwsh
python main.py -u my_script.gml extracted_scripts/
```

#### Packing `.gml` scripts into a single file

```pwsh
python main.py -p <input_directory> <output_file.gml>
```

Example:

```pwsh
python main.py -p extracted_scripts/ my_script.gml
```
