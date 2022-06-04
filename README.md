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

hello allows users to confirm that they can connect to the Canvas course
that they're interested in modifying.

Format for command line input is as follows:

python github-2-canvas hello \[course_id\]

## convert

convert allows users to convert their markdown code to HTML.

Format for command line input is as follows:

python github-2-canvas convert \[md_filename\]

convert returns the absolute path of the newly created HTML file.

## create

Creates Page (only pages at this point) using the following syntax:

python github-2-canvas.py create \[md_filename\] \[course_id\]

## Resources

- [Canvas API](https://canvasapi.readthedocs.io/en/stable/getting-started.html)
- [Python Markdown](https://python-markdown.github.io/)
