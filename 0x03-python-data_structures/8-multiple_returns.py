#!/usr/bin/python3


def multiple_returns(sentence):
        if sentence == "":
            return (o, None)
        return (len(sentence), sentence[0])
