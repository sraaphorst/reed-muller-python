#!/usr/bin/env python
"""rmencode.py

By Sebastian Raaphorst, 2012.

Simple command-line application for Reed-Muller encoding of one or more 0-1 strings."""

import sys
import reedmuller

if __name__ == '__main__':
    # Validate the command-line parameters.
    if len(sys.argv) < 4:
        sys.stderr.write('Usage: %s r m word [word [...]]\n' % (sys.argv[0],))
        sys.exit(1)

    r, m = map(int, sys.argv[1:3])
    if (m <= r):
        sys.stderr.write('We require r < m.\n')
        sys.exit(2)

    # Create the code.
    rm = reedmuller.ReedMuller(r, m)
    k = rm.message_length()

    # Now iterate over the words to encode, validate them, and encode them.
    for word in sys.argv[3:]:
        try:
            listword = list(map(int, word))
            if (not set(listword).issubset([0, 1])) or (len(listword) != k):
                sys.stderr.write('FAIL: word %s is not a 0-1 string of length %d\n' % (word, k))
            else:
                print(''.join(map(str, rm.encode(listword))))
        except:
            sys.stderr.write('FAIL: word %s is not a 0-1 string of length %d\n' % (word, k))
