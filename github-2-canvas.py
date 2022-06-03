#!/usr/bin/env python3

from canvasapi import Canvas
import markdown
import os
import re
import sys

CANVAS_API_KEY = os.environ['CANVAS_API_KEY']
CANVAS_API_PATH = os.environ['CANVAS_API_PATH'].replace('/api/v1','')

def say_hello():
    '''
    Attempt to connect to Canvas.
    '''

    # Instantiate Canvas object with environment variables
    canvas = Canvas(CANVAS_API_PATH, CANVAS_API_KEY)
    print('Hello from ' + str(canvas.get_course(sys.argv[2])))

def convert_to_html():
    '''
    Take command line input and convert a markdown file into an HTML file.
    This HTML file is saved in the directory from which the command was
    executed (which I'm realizing is not very smart).
    '''

    # Instantiate a markdown object to be used for conversion to HTML
    md = markdown.Markdown()

    # Parse user input (if necessary) to get Markdown file name
    if len(sys.argv) > 2:
        md_filename = sys.argv[2].split('/')[-1]
        assert re.match('^[\w\-. ]+.md$', md_filename), \
            "Input must be valid Markdown filename"
    else:
        md_filename = "README.md"

    # Generate name for new HTML file
    html_filename = md_filename.split('.')[0] + '.html'

    # Open Markdown, convert with md, close file
    md_file = open(md_filename)
    html = md.convert(md_file.read())
    md_file.close()

    # Open new file, write with converted Markdown, and close
    html_file = open(html_filename, 'w')
    html_file.write(html)
    html_file.close()

    # Return filename if other functions need it
    return html_filename

def create_lesson():
    '''
    Create a Canvas lesson using a README.md file.
    '''

    html_filename = convert_to_html()

# Control flow
if sys.argv[1] == 'hello':
    say_hello()

elif sys.argv[1] == 'convert':
    convert_to_html()

elif sys.argv[1] == 'create':
    pass
