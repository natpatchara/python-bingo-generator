# Bingo generator

Bingo generator python source code by natpatchra pongjirapat based on script by furas

For project in community medicine academic year 2021

ref: https://stackoverflow.com/questions/60234264/program-to-create-an-image-grid-dynamically-from-a-folder-with-images-in-it

## Table of content
* [project structure](#project-structure)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)
* [Status](#status)
* [Reference](#reference)

## project structure
```
    .
    ├── font                    # Directory for font used in bingo card
    ├── pic                     # Directory for image material(empty folder template is given)
    ├── source                  # Directory for source code including module
    ├── output                  # Directory for Exported jpg bingo card
    ├── script(hidden)          # Directory for hidden utilities script(eg. mass rename etc.)
    ├── __pycache__(hidden)     # Directory for hidden cache files
    ├── main.py                 # Main python script for running preset script
    └── README.md

```

## technologies

    - python 3.9.7
    - Pillow 9.0.1

## setup
Clone this project then install requirement libraries with following command
```
    >pip install -r requirement.txt
```
Or install to your virtual environment of choice (eg. poetry, conda, etc.)

Then try run following script to check your installation
```
    > python
    >>> import PIL
    >>> PIL.__version__
    '9.0.1'
```
if your console return similar output then your installation is finished

## usage
There are two main usage of this script availables at a time of writing this document
- The first use is to use main.py as a all in one script for create bingo card
    To use this script some modification is needed before you can run your script. 
    
    The most importance one is to import your image material for your bingo slot into pic folder. The pattern of file names can be changed according to your liking. 
    
    However, our seggested method is in format of "some_pattern_{i}.jpg." This is mainly to make python easyly recognised your files.

    after your preparation is completed run following command to create bingo card.
    ```
        > python main.py "pic/some_pattern_*.jpg" nrows ncols size_per_slot number_cards
    ```  
    after a few moment a script should stopped and your output card should be in your output folder

- The scond use is to use our bingo_generator.py as a dependencies for your project
    This usage is for more advance user who our preset script is not suit your usage

    There are two main functions in our files including draw_table and create_bingo_card

    Detailed of each function can be found in seperate markdown inside source folder and docstring of bingo_generator file.

## status
As of writing this markdown file, our project is at a stage of a small scale real world usage. However, there are no benchmarking and intense testing done yet.

In summary our current features and to do include:

* features
    * Working main script for creating bingo card
    * Main depencdencies file with working function

* todo
    * Improve documentation for dependencies
    * Intensive testing
    * Optimization

## reference
- Original source code by furas replied from [stackoverflow](https://stackoverflow.com/questions/60234264/program-to-create-an-image-grid-dynamically-from-a-folder-with-images-in-it)
- [Pillow documentation](https://pillow.readthedocs.io/en/stable/)
