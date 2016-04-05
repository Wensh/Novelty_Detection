__author__ = 'wenjiezhong'

import pandas as pd

#input
span_scores = pd.read_csv('Data/span_scores.csv')
checked_words = []

#output
relevance_scores = {}

def process():
    i = 0
    while i < len(span_scores['Relevant Span']):
        if span_scores['Relevant Span'][i] not in checked_words:
            counter = 0
            score = 0
            j = i
            word = span_scores['Relevant Span'][i]
            while j < len(span_scores['Relevant Span']):
                checked_words.append(word)
                if word == span_scores['Relevant Span'][j]:
                    score += float(span_scores['Relevant Span Score'][j])
                    counter += 1
                j += 1
            if counter is 0:
                relevance_scores[word] = score/1
            else:
                relevance_scores[word] = score/counter
        i += 1

process()

relevance_scores_df = pd.DataFrame(list(relevance_scores.iteritems()), columns=['Relevant Span','Relevant Span Score'])
relevance_scores_df.to_csv('relevance_scores.csv',index=False,header=True)