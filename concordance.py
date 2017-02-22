"""
	Author:		Dominik Suwala <dxs9411@rit.edu>
	Date:		2017-02-16
	Purpose:	Generate a concordance on a given input
"""

import re, string

"""
	Removes common punctuation from sentences in order to capture words
"""
def removePunctuation( mystr, removeEndOfSentence=False ):
	# Punctuation can be attached to words. We will sanitize the input
	removePunctuation = [ ',', ';', ':', '\'s', '\'', '"', '...' ]
	for removable in removePunctuation:
		mystr = mystr.replace( removable, ' ' )
	mystr = mystr.strip()
	if( removeEndOfSentence ):
		removePunctuation += [ '.', '!', '?' ]
		if( mystr[ -1 ] in removePunctuation ):
			mystr = mystr.replace( mystr[ -1 ], '' )

	return mystr

def removeWhitespaces( mystr ):
	for whitespace in string.whitespace:
		mystr = mystr.replace( whitespace, ' ' )
	return mystr

def main():

	print( 'Enter the filename:' )
	filename = raw_input()

	alltext = removePunctuation( open( filename, 'r' ).read() )
	# Split when a capitalized letter comes after an end of sentence
	# 	punctuation. The last sentence will not have a capital letter.
	sentences = re.finditer( '[(\\.,\?\!)+]\s+[A-Z]', alltext )
	# my regex: [(\\.,\?\!)+]\s+[A-Z]
	# wiki:     ((?<=[a-z0-9][.?!])|(?<=[a-z0-9][.?!]\"))(\s|\r\n)(?=\"?[A-Z])
	# https://en.wikipedia.org/wiki/Sentence_boundary_disambiguation
	splitIndeces = []

	# Track index of sentence ending
	for s in sentences:
		splitIndeces.append( s.end( 0 ) - 1 )
	splitIndeces.append( len( alltext ) )

	sentenceNums = {}

	# Populate dictionaries with occurrences and sentence numbers
	for i in range( len( splitIndeces ) ):
		startIndex = 0
		if( i != 0 ):
			startIndex = splitIndeces[ i - 1 ]
		curSentence = removeWhitespaces( removePunctuation(
			alltext[ startIndex : splitIndeces[ i ] ].strip().lower(), True )
		)
		for word in curSentence.split( ' ' ):
			if( len( word ) > 0 ):
				index = i + 1 # Sentence numbers
				try:
					sentenceNums[ word ]
				except KeyError:
					sentenceNums[ word ] = {}
				try:
					sentenceNums[ word ][ str( index ) ] += 1
				except KeyError:
					sentenceNums[ word ][ str( index ) ] = 1
	# Print out occurrences of words in alphabetical order and where they occur
	ctr = 0
	wordWidth = 28
	alphaSize = len( string.ascii_lowercase )

	for word in sorted( sentenceNums.keys() ):
		prefix = chr( ord( 'a' ) + ( ctr % alphaSize ) )
		prefix *= ( 1 + ctr // alphaSize )
		prefix += '. '
		pword = word
		if( len( pword ) > wordWidth - len( prefix ) - 3 ):
			pword = pword[ :wordWidth - len( prefix ) - 3 ] + '...'
		prefix += pword
		sentences = ''
		totalOccurrences = 0
		for sentenceNum in sorted( sentenceNums[ word ].keys() ):
			curCount = sentenceNums[ word ][ sentenceNum ]
			totalOccurrences += curCount
			sentences += ( ',' + sentenceNum ) * curCount
		sentences = sentences[ 1: ]
		print( '%s{%s:%s}' % (
			prefix.ljust( wordWidth ),
			str( totalOccurrences ),
			sentences )
		)
		ctr += 1

if __name__ == "__main__":
	main()
