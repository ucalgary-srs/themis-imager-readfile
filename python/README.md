# THEMIS All-Sky Imager Raw PGM Data Readfile

[![Github Actions - Tests](https://github.com/ucalgary-aurora/themis-imager-readfile/workflows/tests/badge.svg)](https://github.com/ucalgary-aurora/themis-imager-readfile/actions?query=workflow%3Atests)
[![PyPI version](https://img.shields.io/pypi/v/themis-imager-readfile.svg)](https://pypi.python.org/pypi/themis-imager-readfile/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![PyPI Python versions](https://img.shields.io/pypi/pyversions/themis-imager-readfile.svg)](https://pypi.python.org/pypi/themis-imager-readfile/)

Python library for reading THEMIS All-Sky Imager (ASI) stream0 raw PGM-file data. The data can be found at https://data.phys.ucalgary.ca or http://themis.igpp.ucla.edu/index.shtml.

## Supported Datasets

- THEMIS ASI raw: [stream0](https://data.phys.ucalgary.ca/sort_by_project/THEMIS/asi/stream0) PGM files

## Installation

The themis-imager-readfile library is available on PyPI:

```console
$ python3 -m pip install themis-imager-readfile
```

## Supported Python Versions

themis-imager-readfile officially supports Python 3.8+.

## Examples

Example Python notebooks can be found in the "examples" directory. Further, some examples can be found in the "Usage" section below.

## Usage

Import the library using `import themis_imager_readfile`

### Read a single file

```python
>>> import themis_imager_readfile
>>> filename = "path/to/data/2020/01/01/atha_themis02/ut06/20200101_0600_atha_themis02_full.pgm.gz"
>>> img, meta, problematic_files = themis_imager_readfile.read(filename)
```

### Read multiple files

```python
>>> import themis_imager_readfile, glob
>>> file_list = glob.glob("path/to/files/2020/01/01/atha_themis02/ut06/*full.pgm*")
>>> img, meta, problematic_files = themis_imager_readfile.read(file_list)
```

### Read using multiple worker processes

```python
>>> import themis_imager_readfile, glob
>>> file_list = glob.glob("path/to/files/2020/01/01/atha_themis02/ut06/*full.pgm*")
>>> img, meta, problematic_files = themis_imager_readfile.read(file_list, workers=4)
```

### Read with no output

```python
>>> import themis_imager_readfile, glob
>>> file_list = glob.glob("path/to/files/2020/01/01/atha_themis02/ut06/*full.pgm*")
>>> img, meta, problematic_files = themis_imager_readfile.read(file_list, workers=4, quiet=True)
```

### Read only the first frame of each file

```python
>>> import themis_imager_readfile, glob
>>> file_list = glob.glob("path/to/files/2020/01/01/atha_themis02/ut06/*full.pgm*")
>>> img, meta, problematic_files = themis_imager_readfile.read(file_list, first_frame=True)
```

### Exclude reading the metadata

```python
>>> import themis_imager_readfile, glob
>>> file_list = glob.glob("path/to/files/2020/01/01/atha_themis02/ut06/*full.pgm*")
>>> img, meta, problematic_files = themis_imager_readfile.read(file_list, no_metadata=True)
```

## Multiprocessing Notes

If you receive error messages about multiprocessing, be sure that your code is wrapped in a `main()` method. This usually resolves the issue. One example implementation is:

```python
import themis_imager_readfile

def main():
    filename = "path/to/data/2020/01/01/atha_themis02/ut06/20200101_0600_atha_themis02_full.pgm.gz"
    img, meta, problematic_files = themis_imager_readfile.read(filename)

if (__name__ == "__main__"):
    main()
```

## Development

Clone the repository and install dependencies using Poetry.

```console
$ git clone https://github.com/ucalgary-aurora/themis-imager-readfile.git
$ cd themis-imager-readfile/python
$ make install
```

## Testing

```console
$ make test
[ or do each test separately ]
$ make test-flake8
$ make test-pylint
$ make test-pytest
```
