Diplomacy Betrayal Dataset
==========================

This dataset contains a collection of interaction sequences between allies in
online Diplomacy [1] games. A sequence consists of consecutive game seasons
during which the two players exchange messages and help each other in the game.
Half of the sequences end with betrayal, while the other half are part of
lasting friendships.

URL: http://vene.ro/betrayal

License: Open Data Commons Attribution (ODC-By 1.0)
         Summary: http://opendatacommons.org/licenses/by/summary/
         See LICENSE.txt for more details.

Authors: Vlad Niculae <vlad@cs.cornell.edu>
         Srijan Kumar <srijan@cs.umd.edu>
         Jordan Boyd-Graber <Jordan.Boyd.Graber@colorado.edu>
         Cristian Danescu-Niculescu-Mizil <cristian@cs.cornell.edu>

Version: 1.0 (02/23/2016)

The dataset is further described in our paper:
    Vlad Niculae, Srijan Kumar, Jordan Boyd-Graber
        and Cristian Danescu-Niculescu-Mizil.
    Linguistic harbingers of betrayal: A case study on an online strategy game.
    In: Proceedings of ACL, 2015.


Description
-----------

Diplomacy [1] is a popular and engaging strategic board game that is often
played online [2, 3].  It is based heavily on communication between the
players.  Due to its military domination setting, Diplomacy is a well suited
environment for studying naturally occurring betrayal and deception.

From a collection of Diplomacy game logs, we identified and extracted *ongoing,
established, and reciprocal* friendships: relationships that contain at least
two consecutive and reciprocated acts of support that span at least three
seasons in game time, with no more than five seasons passing between two acts
of friendship.

We then identified 250 *betrayals*: the subset of friendships described above
that are followed by at least two attacks.  To match each betrayal, we selected
a friendship that is not followed by any offensive action, but is otherwise
nearly identical (in terms of length and relative time within the game).
The current dataset consists of these selected betrayals and friendships only.

Each relationship contains a sequence of seasons.  Within each season, we
provide features extracted from the messages sent by each player.  More
details about the message representation are available in the "Data format"
section of this README.


Files
-----

 *  diplomacy_data.json - a JSON file containing the dataset;
 *  imbalance_plot.py - a sample Python script to reproduce one of the
      images from the website (http://vene.ro/betrayal/imba.png);
 *  README.txt - this readme;
 *  LICENSE.txt - full text of the ODC-BY-1.0 license.

If redistributing any subset of the dataset, please include the README.txt
and LICENSE.txt files.

Data format
-----------

The dataset is a UTF-8 encoded JSON file:

    >>> import json
    >>> from io import open
    >>> with open("diplomacy_data.json", "r") as f:
    ...     diplomacy = json.load(f)
    ...

It is structured as a list of dictionaries, one for each of the 500 sequences.

    >>> len(diplomacy)
    500

This is an example of one such entry, with the fields explained:

    >>> entry = diplomacy[0]
    >>> entry
    {
        'idx': 0,           # unique identifier of the dataset entry
        'game': 74,         # unique identifier of the game it comes from
        'betrayal': True,   # whether the friendship ended in betrayal
        'people': u'AT',    # the countries represented by the two players
                            # (in this case, Austria and Turkey)
        'seasons': ...
    }

The 'seasons' field is again a list of dictionaries, one for each game season
in the friendship sequence.  In the example below, there are 8 seasons, each
identified by the game year.  Decimal notation is used to denote the season in
each year.  For example, 1906.0 is the spring of 1906 and 1906.5 is the fall of
1906.  Each season is also marked with what interaction the two players have
at the end of the discussion:  whether the players supported one another
('support'), attacked one another ('attack'), or did not have explicit military
interactions (null).

    >>> seasons = entry['seasons']
    >>> len(seasons)
    8
    >>> seasons[0]
    {
        'season': 1906.5,           # fall of the year 1906 (game time)
        'interaction': {
            'victim': u'support',   # the victim supported the betrayer
            'betrayer': u'support'  # the betrayer supported the victim
        },
        'messages': {
            'victim': ...,
            'betrayer': ...
        }
}

The ['messages']['victim'] and ['messages']['betrayer'] fields are lists of
features of each message sent by the victim to the betrayer, and by the
betrayer to the victim, respectively:

    >>> msgs = seasons[0]['messages']['betrayer']
    >>> len(msgs)
    6
    >>> msgs[0]
    {
        "n_words": 146,             # number of words in the message
        "n_sentences": 9,           # number of sentences in the message

        "n_requests": 7,            # number of request sentences
        "politeness": 0.8320,       # politeness of the requests (from 0 to 1)
                                    # (using the Stanford Politeness
                                    # Classifier available at [4])
        "sentiment": {
            "positive": 1,          # no. sentences with positive sentiment
            "neutral": 3,           #      "      "      neutral sentiment
            "negative": 5           #      "      "      negative sentiment
        },                          # (using Stanford Sentiment Analysis [5])

        "lexicon_words": {          # words and phrases matching several
            "disc_expansion": [     # linguistic and psycholinguistic lexicons
                "until",            # (see below for details)
                "yet",
                "instead"
            ],
            "premise": [
                "for",
                "for"
            ],
            ...
        },
        "frequent_words": [         # frequent words in the message
            "more",                 # (occurring in at least 50 messages
            "let",                  # and 5 friendships overall)
            "keep",
            "...
        ]
    }

The words in each list are in random order. The order of messages within a
season is also randomized.  This measure is in place to protect the privacy of
the players and of their conversations.

The lexicons used to construct the "lexicon_words" field are:

 *  'claim', 'premise':  Argumentation structure markers [6]
 *  'allsubj': Subjective markers [7]
 *  'disc_*':  Discourse markers from the Penn Discourse Treebank. [8]
        Includes 'disc_comparison', 'disc_expansion', 'disc_contingency',
        'disc_temporal_future' and 'disc_temporal_rest' (we manually split
        'temporal' from PDT into 'temporal_future' and 'temporal_rest' to
        capture planning).


References
----------

[1] https://en.wikipedia.org/wiki/Diplomacy_%28game%29
[2] http://www.floc.net/dpjudge/
[3] http://usak.asciiking.com/
[4] http://politeness.mpi-sws.org/
[5] http://nlp.stanford.edu/sentiment/
[6] C. Stab and I. Gurevych. Identifying Argumentative Discourse Structures in
    Persuasive Essays. In: Proceedings of EMNLP, 2014.
    https://www.ukp.tu-darmstadt.de/data/argumentation-mining/
[7] E. Riloff and J. Wiebe. Learning extraction patterns for subjective
    expressions. In: Proceedings of EMNLP, 2003.
    http://www.anthology.aclweb.org/W/W03/W03-1014.pdf
[8] https://www.seas.upenn.edu/~pdtb/
