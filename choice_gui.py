import os
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
is_charm = tkinter.BooleanVar(value=False)
charm_checkbox = None
output = None


def get_unpack_filepath():
    global root, is_charm, charm_checkbox, output
    file = None
    dir = None
    if is_charm.get():
        charm_dir = filedialog.askdirectory(title="Select directory of charm")
        playertxt_path = os.path.join(charm_dir, "player.txt")
        normalized_playertxt_path = os.path.normpath(playertxt_path)
        charm_name = open(normalized_playertxt_path).readline()[1:-2]
        file = os.path.join(charm_dir, f"{charm_name}.gml")
    else:
        file = filedialog.askopenfilename(
            title="Select file to unpack",
            filetypes=[("GML Files", "*.gml")])
    if file:
        file_dir = os.path.dirname(file)
        dir = os.path.join(file_dir, "scripts")
        output = ("d", os.path.normpath(file), os.path.normpath(dir))
    root.destroy()


def get_pack_filepath():
    global root, is_charm, charm_checkbox, output
    dir = None
    file = None
    if is_charm.get():
        charm_dir = filedialog.askdirectory(title="Select directory of charm")
        dir = os.path.join(charm_dir, "scripts")
        playertxt_path = os.path.join(charm_dir, "player.txt")
        normalized_playertxt_path = os.path.normpath(playertxt_path)
        charm_name = open(normalized_playertxt_path).readline()[1:-2]
        file = os.path.join(charm_dir, f"{charm_name}.gml")
    else:
        dir = filedialog.askdirectory(title="Select scripts directory")
        file = filedialog.askopenfilename(
            title="Select target file",
            filetypes=[("GML Files", "*.gml")])
    if dir and file:
        output = ("c", os.path.normpath(dir), os.path.normpath(file))
    root.destroy()


def choice_gui():
    global root, is_charm, charm_checkbox, output
    root.title("Webby's GML Unpacker")
    root.minsize(300, 150)
    root.resizable(False, False)

    options_frame = tkinter.Frame(root, padx=25, pady=10, bg="white")
    options_frame_2 = tkinter.Frame(options_frame, bg="white")
    root_label = tkinter.Label(
        options_frame_2, text="\nPlease select what you want to do.\n", bg="white")
    charm_checkbox = tkinter.Checkbutton(
        options_frame_2, text="Boll Deluxe Charm", variable=is_charm, bg="white")

    button_frame = tkinter.Frame(
        root, padx=10, pady=10, relief="raised", borderwidth=2)
    button_frame_2 = tkinter.Frame(button_frame)
    unpack_button = tkinter.Button(
        button_frame_2, text="Unpack", command=get_unpack_filepath, padx=5)
    pack_button = tkinter.Button(
        button_frame_2, text="Pack", command=get_pack_filepath, padx=5)

    root_label.pack(anchor="w")
    charm_checkbox.pack(anchor="w")
    options_frame_2.pack()
    options_frame.pack(fill=tkinter.X)

    unpack_button.pack(side=tkinter.LEFT, padx=10)
    pack_button.pack(side=tkinter.LEFT, padx=10)
    button_frame_2.pack()
    button_frame.pack(fill=tkinter.BOTH, expand=True, side=tkinter.BOTTOM)

    root.mainloop()

    return output


if __name__ == "__main__":
    print(choice_gui())
