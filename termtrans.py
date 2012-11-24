#!/usr/bin/env python

import json
import bottle
from bottle import route, run
with open('translation.json', 'rb') as fp:
    data = json.load(fp)

def main():

    @route('/', method='GET')
    def homepage():
        return 'Web services server for translation of terms<br />   \
          Enter &quot;translate/&lt;term&gt;&quot; to translate a term (returns JSON)<br /> \
          Enter &quot;add/&lt;canonical term&gt;/&lt;common term&gt;&quot; to add a term'

    @route('/translate/:term', method='GET')
    def translate_term(term):
        return dict(translation = data[term])

    @route('/add/:canonical/:common', method=['GET', 'POST'])
    def add_term(canonical, common):
        data[common]=canonical
        with open('translation.json', 'wb') as fp:
            json.dump(data, fp)


    bottle.debug(True)
    run()

if __name__ == '__main__':
    main()
