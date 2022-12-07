"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    ("/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/customtkinter", "customtkinter"),
    ("./data", "data")
]
OPTIONS = {
    'iconfile': 'data/medical.png',
    'env': {
        'DATA_DIR': 'data',
    },
    'plist': {
        'CFBundleName': 'MediTrack',
        'CFBundleDisplayName': 'MediTrack',
        'CFBundleGetInfoString': 'MediTrack',
        'CFBundleIdentifier': 'com.meditrack',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleSignature': '????',
        'CFBundleExecutable': 'MediTrack',
        'CFBundleInfoDictionaryVersion': '6.0',
        'CFBundlePackageType': 'APPL',
        'CFBundleDevelopmentRegion': 'English',
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeExtensions': ['*'],
                'CFBundleTypeName': 'All Files',
                'CFBundleTypeRole': 'Viewer',
                'LSItemContentTypes': ['public.data'],
            },
        ],
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)