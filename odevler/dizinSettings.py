# from dizinSettings import getParentFolder

def getParentFolder():
    import sys,os,pathlib
    if getattr(sys, 'frozen', False):
        current_direct = str(pathlib.Path(sys.executable).parent.resolve())+'\\'
        parantez = (str(current_direct)[:-1][::-1].find('\\'))
        parentFolder = str(current_direct)[:-1][::-1][parantez:][::-1]
    elif __file__:
        current_direct = str(pathlib.Path(__file__).parent.resolve())+'\\'
        parantez = (str(current_direct)[:-1][::-1].find('\\'))
        parentFolder = str(current_direct)[:-1][::-1][parantez:][::-1]
    return parentFolder
