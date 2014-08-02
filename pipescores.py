"""Scores converter application

Synopsis
========

    pipescores.py infile outfile

Arguments
=========

infile is an existing scores file in the following format:

    'date'  'team1'  'score1'  'team2'  'score2'  'location'

The role of the script is to take the existing scores file and convert it
into a pipe-delimited format.

This is a Python 3.4 application
"""


from collections import namedtuple
import argparse

# Raw input is a History record
History = namedtuple('History',
                        ['date', 'team1', 'score1', 'team2',
                        'score2', 'location'])


class Game:

    """
    An individual game, based on the input file.
    """

    def __init__(self, history):
        self.date = history.date
        self.team1 = history.team1
        self.score1 = history.score1
        self.team2 = history.team2
        self.score2 = history.score2
        self.location = history.location


class HistoryReader:

    """
    Abstract superclass for History readers.
    """

    def __init__(self, source):
        """Initialize the source"""
        raise NotImplementedError

    def __iter__(self):
        """Yield History instances from the source."""
        raise NotImplementedError


class REHistoryReader(HistoryReader):

    """
    Create History instances from text files using Regular Expressions
    to parse the data.
    """

    def __init__(self, source):
        raise NotImplementedError


class CSVHistoryWriter(Game):

    """
    Create the output file containing the games in CSV format.
    """

    def __init__(self, source):
        raise NotImplementedError


class PipeHistoryWriter(Game):

    """
    Create the output file containing the games in pipe-delimited format.
    """

    def __init__(self, source):
        raise NotImplementedError


class TabHistoryWriter(Game):

    """
    Create the output file containing the games in tab-delimited format.
    """

    def __init__(self, source):
        raise NotImplementedError


def main():
    """
    Parse command-line arguments and run the `convert_games` function.
    """

    parser = argparse.ArgumentParser(description='Scores')
    parser.add_argument('input_file', metavar='History File',
                        type=open, nargs='+', help='Files with Game History')
    parser.add_argument('output_file', metavar='Output File',
                        type=open, nargs='+', help='The converted file')
    parser.add_argument('-d', dest='format', action='store')
    args = parser.parse_args()

    reader_class = REHistoryReader

    if args.format is None:
        writer_class = CSVHistoryWriter
    elif args.format == '|':
        writer_class = PipeHistoryWriter
    elif args.format == '\t':
        writer_class = TabHistoryWriter
    else:
        raise Exception("Unknown -d {0}".format(args.format))

    for source in args.input_file:
        reader = reader_class(source)
        convert_games(args, reader, args.output_file)


def convert_games(args, source, outputfile):
    """
    The default command-line app: load and convert.
    """

    with open(args.output_file, 'w') as f:
        f.write('Output file')
    f.close()

if __name__ == "__main__":
    main()
