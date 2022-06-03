#!/usr/bin/env python3

from bs4 import BeautifulSoup
from canvasapi import Canvas
import markdown
import os
import re
import sys

CANVAS_API_KEY = os.environ['CANVAS_API_KEY']
CANVAS_API_PATH = os.environ['CANVAS_API_PATH'].replace('/api/v1','')

MD_FILENAME = 'README.md'
HTML_FILENAME = 'README.html'

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

    md_filename = sys.argv[2]

    # Generate name for new HTML file
    html_filename = 'README.html'

    # Open Markdown, convert with md, close file
    md_file = open(md_filename)
    html = md.convert(md_file.read())
    md_file.close()

    # Open new file, write with converted Markdown, and close
    html_file = open(html_filename, 'w')
    html_file.write(html)
    html_file.close()

def create_lesson():
    '''
    Creates Page (only pages at this point) using the following syntax:

    python github-2-canvas.py [create] [path/to/file.md] [course_id]
    '''

    convert_to_html()
    canvas = Canvas(CANVAS_API_PATH, CANVAS_API_KEY)

    html = open(HTML_FILENAME, 'r')
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.select('h1')[0].text.strip()
    bs.select_one('h1').decompose()
    
    course_id = sys.argv[3]
    course = canvas.get_course(course_id)
    page = {'title': title,
            'body': bs.prettify()}

    course.create_page(page)

# Control flow
if sys.argv[1] == 'hello':
    say_hello()

elif sys.argv[1] == 'convert':
    convert_to_html()

elif sys.argv[1] == 'create':
    create_lesson()
    os.remove(HTML_FILENAME)
