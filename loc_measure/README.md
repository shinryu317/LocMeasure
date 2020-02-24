# LocMeasure

## Introduction
 LocMeasure is step counter written by Python3.

## Supported language
* C/C++
* CSS
* Fortran
* Go
* HTML
* Java
* JavaScript
* Lua
* Python
* R
* Ruby
* Scala
* ShellScript
* Perl
* PHP

## Usage
Starts step counting for the specified source code.
```
$ python loc_measure.py source_code.cpp --language C/C++
/path/to/loc_measure/source_code.cpp: 9
```
By specifying a directory, the steps of the source code under the specified directory are counted.
```
python loc_measure.py /path/to/directory/ --language C/C++
/path/to/loc_measure/source_code.cc: 10
/path/to/loc_measure/source_code.cpp: 9
/path/to/loc_measure/source_code.h: 10
```
