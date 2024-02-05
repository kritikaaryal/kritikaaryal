import requests
import json

SENTIM = "https://sentim-api.onrender.com/api/v1/"

# TODO: Add elements to each of the lists below.  Then
# good_things list should contain strings relevant to Groton.
# The bad_things list should contain strings relevant to
# St. Marks (or some other objectively bad place).
good_things = [good, awesome, great]
bad_things = [terrible, awful, bad]

#TODO:  Initialize the dictionary below by adding in the special
# "<ADMIN>" key.  Set it to an initial value of 0.
scores = {}

def check_needs_score(good_things : list, \bad_things : list , \message : str) -> (bool, str):
    lowercase_message = message.lower()
    for good_thing in good_things:
        if good_thing.lower() in lowercase_message:
            return True, "positive"
    for bad_thing in bad_things:
        if bad_thing.lower() in lowercase_message:
            return True, "negative"
    return False, "positive" 

def get_adjustment(text:str, desired_type:str) -> float:
    # TODO: Use the requests library to send a JSON requests
    # to the sentimental analysis API.  Then, process the result.
    # If the desired_type passed in is the same as the "type" of
    # the "result" returned, return the absolute value of the
    # "polarity". Otherwise, return the negative of the absolute
    # value of the polarity.
    return 0

def score(message:str) -> (str, float, float, str):
    # TODO: Update the line below to split the message parameter
    # by the tab character to get the username and the text
    # of the message in two variables.
    user, text = message.split('\t')

    # TODO: Update the line below to call the check_needs_score
    # function with the appropiate parameters to
    # determine if the message needs to be scored.
    needs_score, desired_type = False, "positive"

    adjustment = 0
    polarity = 0
    # TODO: Check the needs_score variable to see if the
    # message needs to be scored.  If it does, call the
    # get_adjustment function to determine the score
    if False:
        adjustment = 0

    # TODO: Update the user's score based on the adjustment
    # calculated above.  Dictionaries have a "get" function
    # that will be helpful here, as it allows you to retrieve
    # a value from a dictionary if it exists and specify a default
    # if it does not.  The syntax is: d.get(key, default), where
    # d is the name of the dictionary, key is the element for which
    # you're searching, and default is the value that should be
    # returned if the key isn't found.
    scores[user] = 0

    # TODO: Update the conditions below to reflect the
    # following business logic: users who accumulate
    # a score less than -2 are automatically banned.
    # Individual messages that score less than -0.5
    # are censored.
    if False:
        user = "<ADMIN>"
        text = "You have been banned."
    elif False:
        user = "<ADMIN>"
        text = "Your message has been censored."

    # TODO: The line below truncates the text to be displayed
    # at 40 characters since this is what fits naturally in
    # the GUI.  However, the server includes support for
    # multi-line messages.  If, the last element of this
    # function's return value is a list of strings instead of
    # an individual one, the server will send out a burst of messages
    # that are indented to indicate that a line has been wrapped.
    # To support this, you need to make an empty list.  Then,
    # loop through the text 40 characters at a time (you will want
    # an integer counter to do this), appending slices of the message
    # to your list.  Finally, return the list you constructed
    # instead of the truncated text.
    return user, scores[user], adjustment, text[0:40]
