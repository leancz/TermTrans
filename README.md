TermTrans
=========

Translate common terms to canonical terms.
The idea for this program came about when using an asset management system. There was no
standard name for room numbers. They were documented as RA3, RA03, RA0003 - all for the
same room. I wanted a resource to store all the different possibilities and the canonical
name. Then I could query one of the colloquial names and get the canonical name as a 
response.
This would also apply to suppliers: IBM, I.B.M., and so on. This is also useful for
software naming with Common Platform Enumeration.

This is a Python program and requires Bottle.

The program responds to RESTful web services with JSON.

Original Version 0.1 by Paul Baines (leancz@googlemail.com)
			 
