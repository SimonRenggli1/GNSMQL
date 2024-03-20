from setuptools import setup, find_packages

setup(
  name = 'gnsmql',
  packages = ['gnsmql'],
  version = '0.2.0',
  license='MIT',
  description = 'Database for sleepy people.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author = 'Simon Renggli',
  author_email = 'simon_renggli1@sluz.ch',
  url = 'https://github.com/SimonRenggli1/GNSMQL',
  download_url = 'https://github.com/SimonRenggli1/GNSMQL/archive/refs/tags/latest.tar.gz',
  keywords = ['database', 'sleepy', 'tired', 'zzz'],
  classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)