#!/usr/bin/python2

"""
Select 5000 random Spanish words from the Spanish corpa, then selects nine at random to use as anchor points. The anchor point words are printed to a
file so that human can generate their translations
"""

import logging
import secrets


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('select_for_translation')

    # Read in the Spanish file
    logger.info('Opening Spanish file...')
    lines = []
    with open('../../corpa/spanish/model-ascii.w2v') as f:
        for line in f:
            lines.append(line)

    logger.info('Spanish file read in')

    secrets.SystemRandom().shuffle(lines)
    spanish_vocab = lines[:5000]
    logger.info('Shuffled Spanish words and got the first 5K')

    with open('../../corpa/spanish/model-ascii-5k.w2v', 'w') as f:
        file_data = '\n'.join(spanish_vocab)
        f.write(file_data)

    logger.info('Wrote selected lines to a file')

