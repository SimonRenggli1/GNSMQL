from distutils.core import setup
setup(
  name = 'gnsmql',
  packages = ['gnsmql'],
  version = '0.1',
  license='MIT',
  description = 'Database for sleepy people.',
  author = 'Simon Renggli',
  author_email = 'simon_renggli1@sluz.ch',
  url = 'https://github.com/SimonRenggli1/GNSMQL',
  download_url = 'https://github.com/SimonRenggli1/GNSMQL/archive/refs/tags/v_01.tar.gz',
  keywords = ['database', 'sleepy', 'tired', 'zzz'],
  install_requires=[
          'json',
          'pathlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',

    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13'
  ],
)