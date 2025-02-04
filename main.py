import choice_gui
import gml_unpacker

import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Webby's GML Unpacker",
        description="Unpack and pack .gml files.",
        epilog="If no arguments are given, PowerShell dialog is opened.",
    )
    parser.add_argument(
        "-u",
        "--unpack",
        nargs="+",
        metavar=("file", "directory"),
        help="Unpack a gml file. Provide file and optional directory.",
    )
    parser.add_argument(
        "-p",
        "--pack",
        nargs=2,
        metavar=("directory", "file"),
        help="Pack a folder of scripts into a gml file. Provide directory and file.",
    )

    args = parser.parse_args()
    if args.unpack:
        if len(args.unpack) > 2:
            parser.error(
                "argument -u/--unpack: expected at most two arguments")
        file = args.unpack[0]
        dir = (os.path.dirname(file) if len(args.unpack) < 2
               else args.unpack[1])
        gml_unpacker.unpack_gml(
            os.path.normpath(file), os.path.normpath(dir))
    elif args.pack:
        dir = args.pack[0]
        file = args.pack[1]
        gml_unpacker.pack_gml(os.path.normpath(dir), os.path.normpath(file))
    else:
        choice = choice_gui.choice_gui()
        if choice != None:
            if choice[0] == "d":
                gml_unpacker.unpack_gml(choice[1], choice[2])
            elif choice[0] == "c":
                gml_unpacker.pack_gml(choice[1], choice[2])
