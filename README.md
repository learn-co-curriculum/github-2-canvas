# GitHub 2 Canvas

## Learning Goals

- Build Canvas lessons from the command line
- Improve the vibes with Python

## Introduction

The current github-to-canvas Ruby gem has caused me enough grief that I have
taken time out of my first build week to rewrite it in Python.

github-2-canvas is still very much under construction, but the functions and
details will be added in as I complete them.

## hello

say_hello allows users to confirm that they can connect to the Canvas course
that they're interested in modifying.

Format for command line input is as follows:

python github-2-canvas hello \[course_id\]

## convert

Take command line input and convert a markdown file into an HTML file. This
HTML file is saved in the directory from which the command was executed (which
I'm realizing is not very smart).

## create

Creates Page (only pages at this point) using the following syntax:

_python github-2-canvas.py_ \[create\] \[path/to/file.md\] \[course_id\]

## Resources

- [Canvas API](https://canvasapi.readthedocs.io/en/stable/getting-started.html)
- [Python Markdown](https://python-markdown.github.io/)
