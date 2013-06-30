from distutils.core import setup
import py2exe

setup(name='Aplicacion de ejemplo',
    version='0.1',
    description='Ejemplo del funcionamiento de distutils',
    author='Alex',
    author_email='Alexgmail',
    url='https://github.com/aherrero',
    license='GPL',
    scripts=['hello.py'],
    console=['hello.py'],
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None
)
