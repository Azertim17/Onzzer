from cx_Freeze import setup, Executable
base = None

executables = [Executable("Onzzer\Onzzer.py", base=base)]
includefiles = ['README.rst', 'Onzzer\request_albums.py','Onzzer\request_artistes.py' ,'Onzzer\youtube_search.py' , 'Onzzer\request_pistes.py']
includes = []
packages = ["idna","PyQt5"]

setup(
    name = "Onzzer",
    version = "2.0",
    author = '',
    author_email = '',
    description = 'Onzzer application de recherche musicale',

    options = {'build_exe': {'includes':includes,'packages':packages,'include_files':includefiles}}, 

    executables = executables
)