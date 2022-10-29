from setuptools import setup

APP = ['slack-dnd.py']
DATA_FILES = ['icon.png']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.png',
    'plist': {
        'CFBundleName': 'Slack DND',
        'CFBundleDisplayName': 'Slack DND',
        'CFBundleGetInfoString': 'Slack DND',
        'CFBundleIdentifier': 'com.github.furkanpehli1.Slack-DND',
        'CFBundleVersion': '0.1',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
