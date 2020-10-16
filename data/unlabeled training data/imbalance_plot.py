"""Imbalance in politeness, sentiment and planning for broken friendships

Reproduces the first plot in http://vene.ro/betrayal/

"""

# Author: Vlad Niculae <vlad@cs.cornell.edu>
# License: BSD 3-clause

import json

from scipy.stats import sem
import numpy as np
import matplotlib.pyplot as plt


def last_support(entry):
    """Find the last friendly action between the players"""
    seasons = entry['seasons']
    last_support = None
    for season in seasons[:-1]:
        if 'support' in season['interaction'].values():
            last_support = season['season']
    return last_support


def msgs_features(msgs):
    """Feature extractor for a list of messages"""
    n_sents = sum(m['n_sentences'] for m in msgs) * 1.0

    future = sum(len(m['lexicon_words'].get("disc_temporal_future", []))
                    for m in msgs) / n_sents
    return dict(
        polite=sum(m['politeness'] for m in msgs) / len(msgs),
        sent=sum(m['sentiment']['positive']  for m in msgs) / n_sents,
        future=future)


def features_for_plot(entries, betrayal, sent):
    """Feature extractor for an entire diplomacy dataset"""
    return [
        msgs_features(season['messages']['betrayer' if sent else 'victim'])
        for entry in entries
        for season in entry['seasons']
        if entry['betrayal'] == betrayal
        and season['season'] <= last_support(entry)
        and len(season['messages']['betrayer']) > 0
        and len(season['messages']['victim']) > 0
    ]


if __name__ == '__main__':
    with open("diplomacy_data.json") as f:
        data = json.load(f)

    flip_sent = features_for_plot(data, True, True)
    flip_rcvd = features_for_plot(data, True, False)
    stay_sent = features_for_plot(data, False, True)
    stay_rcvd = features_for_plot(data, False, False)

    # compute the features
    plot_data = {
        key: {'stay_imba': [a[key] - b[key]
                            for a, b in zip(stay_sent, stay_rcvd)],
              'flip_imba': [a[key] - b[key]
                            for a, b in zip(flip_sent, flip_rcvd)]}
        for key in ['future', 'sent', 'polite']}

    # take mean and standard error of features
    # in the paper this uses bootstrapping instead
    plot_data = {key: {inner_key: (np.mean(inner_val), sem(inner_val))
                       for inner_key, inner_val in val.items()}
                 for key, val in plot_data.items()}

    stay_col = (1, 1, 1, 0.5)
    flip_col = "#CF6C84"  # colors[2]
    lw = 2

    plt.figure(figsize=(7, 4))
    labels = dict(sent="positive\nsentiment",
                  polite="politeness",
                  future="planning")

    for k, key in enumerate(["sent", "polite", "future"]):
        data = plot_data[key]
        ax_diff = plt.subplot(1, 3, 1 + k)

        width = 0.45

        val, err = data["stay_imba"]
        ax_diff.bar(0,
                    val,
                    yerr=err,
                    width=width,
                    color=stay_col, label='no betrayal',
                    linewidth=lw,
                    error_kw=dict(elinewidth=2, capthick=2, ecolor='k'))

        val, err = data["flip_imba"]
        ax_diff.bar(width,
                    val,
                    yerr=err,
                    width=width,
                    color=flip_col, label='betrayal',
                    linewidth=lw,
                    error_kw=dict(elinewidth=2, capthick=2, ecolor='k'))

        plt.xticks([width], [labels[key]], fontsize=20)
        if k == 0:
            plt.ylabel("imbalance", fontsize=20)
        if k != 0:
            plt.yticks(())
        plt.xlim(-0.05, 0.95)
        plt.ylim(-0.027, 0.037)
        plt.axhline(0, color='k')

        plt.yticks(fontsize=16)
        if k == 2:
            plt.legend(fontsize=16, loc="upper left", handlelength=0.8)
    plt.tight_layout()
    plt.show()
