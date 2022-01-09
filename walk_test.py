import os

MD_EXTENSIONS = ['.md', '.markdown']
BASE_DIR = '.'

IGNORED_FOLDERS = ['.git', '.vscode', '.idea', 'docs', '_image', '_attachment']
IGNORED_MD_FILES = ['README', '_sidebar']     # do NOT include file extensions


def removeSpaces(filepath):
    if ' ' in filepath:
        new_filepath = filepath.replace(' ', '')
        print("[removeSpaces] rename", filepath, "to", new_filepath)
        os.rename(filepath, new_filepath)
        return new_filepath
    else:
        return filepath


# TODO: generate menu (_sidebar.md)
def walk(root):
    root = removeSpaces(root)
    basename = os.path.basename(root)
    # isdir
    if os.path.isdir(root):
        if basename in IGNORED_FOLDERS: return
        # TODO: do something with the folder
        print("Dir:", root)
        # sort and walk every file in this folder
        fileList = os.listdir(root)
        fileList.sort()
        for file in fileList:
            filepath = os.path.join(root, file)
            walk(filepath)
    # isfile
    else:
        fileNameWithoutExt, ext = os.path.splitext(basename)
        if (ext not in MD_EXTENSIONS) or (fileNameWithoutExt in IGNORED_MD_FILES): return
        # TODO: do something with the file
        print("File:", root)


def walkSubdirs(root):
    fileList = os.listdir(root)
    fileList.sort()
    for file in fileList:
        filepath = os.path.join(root, file)
        if os.path.isdir(filepath):
            walk(filepath)


# walk(BASE_DIR)        # walk including BASE_DIR
walkSubdirs(BASE_DIR)   # walk without BASE_DIR itself
