import re
from setuptools import setup

with open('README.md') as f: readme = f.read()

version = ''
with open('PILSkinMC/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(
    name='PILSkinMC',
    author='SkylasJustVibin',
    url='https://github.com/SkylaDev/PILSkinMC',
    project_urls={'Issue Tracker': 'https://github.com/SkylaDev/PILSkinMC/issues'},
    version=version,
    packages=['PILSkinMC'],
    license='MIT',
    description='PILSkinMC is a basic Minecraft player skin renderer for Python\'s PIL (Pillow) library.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
    install_requires=['Pillow', 'numpy']
)
