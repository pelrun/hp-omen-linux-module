import logging
from pathlib import Path

DIR_OF_THIS_SCRIPT = Path( __file__ ).parent 

# compilation database is created with command
# pio run -t compiledb
# last part of the path, 'uno', probably should be determined from 'platformio.ini'
compilation_database_folder = DIR_OF_THIS_SCRIPT / '.pio' / ' build' / 'uno'

database = None
if compilation_database_folder.exists():
    try:
        import ycm_core
        database = ycm_core.CompilationDatabase(compilation_database_folder)
    except ImportError:
        pass


flags_general = [
   '-Wall'
  ,'-Wextra'
  ,'-Werror'
  ,'-Wno-attributes'
  ,'-std=c++17'
  ,'-I/usr/src/linux-hwe-5.8-headers-5.8.0-45/include'
]

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.ino', '.m', '.mm' ]


def IsHeaderFile( filename ):
    return filename.suffix.lower() in [ '.h', '.hxx', '.hpp', '.hh' ]


def FindCorrespondingSourceFile( filename ):
    filename = Path(filename)
    if IsHeaderFile( filename ):
        for extension in SOURCE_EXTENSIONS:
            if filename.with_suffix(extension).exists():
                return filename.with_suffix(extension)
            if filename.with_suffix(extension.upper()).exists():
                return filename.with_suffix(extension.upper())

    return filename


def GetCompilationInfoFromCLS():
    include_flags = []
    cflags = []
    cxxflags = []
    
    ccls_path = DIR_OF_THIS_SCRIPT / '.ccls'
    if ccls_path.exists():
        for l in ccls_path.open('rt'):
            l = l.strip()
            if l.startswith('-I'):
                include_flags.append(l)
            if l.startswith('%c '):
                cflags.append(l[3:])
            if l.startswith('%cpp '):
                cflags.append(l[5:])
            if l.startswith('-D'):
                cflags.append(l)
                cxxflags.append(l)
    return include_flags, cflags, cxxflags


def Settings ( **kwargs ):
    logger = logging.getLogger('ycm-extra-conf') 
    # logger.setLevel(logging.DEBUG)
    logger.debug(kwargs)
       
    language = kwargs[ 'language' ]
  
    if language == 'cfamily':
      # If the file is a header, try to find the corresponding source file and
      # retrieve its flags from the compilation database if using one. This is
      # necessary since compilation databases don't have entries for header files.
      # In addition, use this source file as the translation unit. This makes it
      # possible to jump from a declaration in thetheader file to its definition
      # in the corresponding source file.
        filename = FindCorrespondingSourceFile( kwargs[ 'filename' ] )
        logger.debug(filename)

        include_flags, cflags, cxxflags = GetCompilationInfoFromCLS()

        return_flags = flags_general + include_flags + (cflags if filename.suffix.lower() == '.c' else cxxflags)

        settings = {
                'include_paths_relative_to_dir': str(DIR_OF_THIS_SCRIPT.resolve()),
                'override_filename': str(filename),
                'do_cache': True
                }

        if not database:
            settings.update({'flags': return_flags})
            return settings

        compilation_info = database.GetCompilationInfoForFile( str(filename) )
        if not compilation_info.compiler_flags_:
            logger.info('No compilation info for {} return flags from .ccls'.format(filename))
            settings.update({'flags': return_flags})
            return settings

        # compliler_flags_ is actually a list-like object, containing full command line for compiler 
        # get only flags (starting from -)
        final_flags = list(filter(lambda f: f[0] == '-', compilation_info.compiler_flags_))
        final_flags += return_flags

        # remove duplicates
        final_flags = [*{*final_flags}]

        logger.debug('Final flags {}'.format(final_flags))
        settings.update({'flags': final_flags})
        return settings


if __name__ == '__main__':
    print(Settings(filename='src/lesson2_running_light.cpp', language='cfamily'))

