#!/usr/bin/env python3

from bs4 import BeautifulSoup
from canvasapi import Canvas
import markdown
import os
import re
import sys

CANVAS_API_KEY = os.environ['CANVAS_API_KEY']
CANVAS_API_URL = os.environ['CANVAS_API_URL']

def hello(course_id):
    '''
    hello allows users to confirm that they can connect to the Canvas
    course that they're interested in modifying.

    Format for command line input is as follows:

    python github-2-canvas hello [course_id]
    '''

    # Instantiate Canvas object with environment variables
    canvas = Canvas(CANVAS_API_URL, CANVAS_API_KEY)
    print('Hello from ' + str(canvas.get_course(course_id)))

def convert(md_filename):
    '''
    convert allows users to convert their markdown code to HTML.

    Format for command line input is as follows:

    python github-2-canvas convert [md_filename]

    convert returns the absolute path of the newly created HTML file.
    '''

    # Instantiate a markdown object to be used for conversion to HTML
    md = markdown.Markdown()

    assert re.match('^[\w\-. ]+.md$', md_filename), \
        "Input must be valid Markdown filename"

    # Open Markdown, convert with md, close file
    md_file = open(md_filename)
    html = md.convert(md_file.read())
    md_file.close()

    # Open new file, write with converted Markdown, and close
    html_filename = os.path.abspath(md_filename).split('.')[0] + '.html'
    html_file = open(html_filename, 'w')
    html_file.write(html)
    html_file.close()

    return html_filename

def create():
    '''
    create allows users to create new pages inside of their Canvas course.

    Format for command line input is as follows:

    python github-2-canvas.py create [md_filename] [course_id]

    create returns the absolute path of the newly created HTML file so that it
    may be destroyed after a new page is created.
    '''

    html_filename = convert()
    canvas = Canvas(CANVAS_API_URL, CANVAS_API_KEY)

    html = open(html_filename, 'r')
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.select('h1')[0].text.strip()
    bs.select_one('h1').decompose()
    
    course_id = sys.argv[3]
    course = canvas.get_course(course_id)
    page = {'title': title,
            'body': bs.prettify()}

    course.create_page(page)

    return html_filename

# Control flow
if sys.argv[1] == 'hello':
    hello(sys.argv[2])

elif sys.argv[1] == 'convert':
    convert(sys.argv[2])

elif sys.argv[1] == 'create':
    html_filename = create()
    os.remove(html_filename)
