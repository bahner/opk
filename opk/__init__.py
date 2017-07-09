#!/usr/bin/env python3
# pylint: disable=invalid-name,missing-docstring
"""Webgrensesnitt for OPK"""

import sys
import os
from openpyxl import load_workbook
from flask import Flask, render_template, request
from werkzeug import secure_filename
from opk.functions import first_name, last_name, gen_memberlist

app = Flask(__name__)

@app.route('/upload')
def upload_form():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(filename)
        members = gen_memberlist(filename)
        os.remove(filename)
        return render_template('members.html', members=members, number=len(members))
