import os

IGNORED_FOLDERS = ['docs']
IGNORED_FILES = ['README']
BASE_DIR = './'

def removeSpaces():
    """Remove spaces in directory and file names
    """
    fileList = os.listdir(BASE_DIR)
    fileList.sort()

    for category in fileList:
        if category in IGNORED_FOLDERS: continue
        categoryPath = BASE_DIR + category
        if not os.path.isdir(categoryPath): continue
        if ' ' in category:
            newCategory = category.replace(' ', '')
            newCategoryPath = BASE_DIR + newCategory
            os.rename(categoryPath, newCategoryPath)
            # print('Renamed "%s" to "%s"' % (categoryPath, newCategoryPath))
            category = newCategory
            categoryPath = newCategoryPath
        
        mdFileList = os.listdir(categoryPath)
        mdFileList.sort()
        for mdFile in mdFileList:
            mdFilePath = categoryPath + "/" + mdFile
            if not os.path.isfile(mdFilePath): continue
            if ' ' in mdFile:
                newFile = mdFile.replace(' ', '')
                newFilePath = categoryPath + "/" + newFile
                os.rename(mdFilePath, newFilePath)
                # print('Renamed "%s" to "%s"' % (mdFilePath, newFilePath))
                mdFile = newFile
                mdFilePath = newFilePath


def generateMenu():
    """Generate menu and write to '_sidebar.md'
    """
    menu = "* [Home](/)\n\n"

    fileList = os.listdir(BASE_DIR)
    fileList.sort()

    for category in fileList:
        if category in IGNORED_FOLDERS: continue
        categoryPath = BASE_DIR + category
        if not os.path.isdir(categoryPath): continue
        # print("## " + category)
        # menu += "* [%s](%s/)" % (category, category) + '\n\n'
        menu += "* " + category + '\n\n'

        # Get all markdown files in current category
        mdFileList = os.listdir(categoryPath)
        mdFileList.sort()
        for mdFile in mdFileList:
            mdFilePath = categoryPath + "/" + mdFile
            if not os.path.isfile(mdFilePath): continue
            if mdFile.endswith(".md") or mdFile.endswith(".markdown"):
                fileNameWithoutExt, _ = os.path.splitext(mdFile)
                if fileNameWithoutExt in IGNORED_FILES: continue
                # print(mdFile)
                menu += "  - [%s](%s/%s)" % (fileNameWithoutExt, category, mdFile) + '\n'
        
        menu += '\n'

    # print("---------- Menu --------------")   
    # print(menu)
    with open(BASE_DIR + '_sidebar.md', 'w') as f:
        f.write(menu)


removeSpaces()
generateMenu()

