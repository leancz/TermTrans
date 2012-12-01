#!/usr/bin/env python

import json
import bottle
from bottle import route, run
try:
    with open('translation.json', 'rb') as fp:
        data = json.load(fp)
except IOError:
    # File doesn't exist, create it
    with open('translation.json', 'wb') as fp:
        json.dump({}, fp)
        data={}

def main():

    @route('/', method='GET')
    def homepage():
        return 'Web services server for translation of terms<br />   \
          Enter &quot;translate/&lt;term&gt;&quot; to translate a term (returns JSON)<br /> \
          Enter &quot;add/&lt;canonical term&gt;/&lt;common term&gt;&quot; to add a term'

    @route('/translate/:term', method='GET')
    def translate_term(term):
        if term in data.keys():
            result = dict(translation = data[term])
        else:
            result = dict(error = 'Missing value')
        return result
        
    @route('/add/:canonical/:common', method=['GET', 'POST'])
    def add_term(canonical, common):
        data[common]=canonical
        with open('translation.json', 'wb') as fp:
            json.dump(data, fp)


    bottle.debug(True)
    run()

if __name__ == '__main__':
    main()
