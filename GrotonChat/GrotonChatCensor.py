import requests
import json

SENTIM = "https://sentim-api.onrender.com/api/v1/"

# TODO: Add elements to each of the lists below.  Then
# good_things list should contain strings relevant to Groton.
# The bad_things list should contain strings relevant to
# St. Marks (or some other objectively bad place).
good_things = ["groton", "schoolhouse", "zebra" "tight-knit community"]
bad_things = ["st.marks", "lion", "southborough" ]

#TODO:  Initialize the dictionary below by adding in the special
# "<ADMIN>" key.  Set it to an initial value of 0.
scores = {"<ADMIN>":0}

def check_needs_score(good_things : list, \
                      bad_things : list , \
                      message : str) -> (bool, str):
    lowercase_message = message.lower()
    for word in lowercase_message.split():
        print(word)
        for good_thing in good_things:
            if good_thing.lower() == word:
                return True, "positive"
        for bad_thing in bad_things:
            if bad_thing.lower() == word:
                return True, "negative"
    return False, "positive" 

def get_adjustment(text:str, desired_type:str) -> float:
    resp = requests.post(SENTIM, json={"text": text})
    j = resp.json()
    polarity = j["result"]["polarity"]
    analysis_type = j["result"]["type"]
    if analysis_type == desired_type:
        adjustment = abs(polarity)
    else:
        adjustment = -abs(polarity)
    
    return adjustment

def score(message:str) -> (str, float, float, str):
    user, text = message.split('\t')

    # TODO: Update the line below to call the check_needs_score
    # function with the appropiate parameters to
    # determine if the message needs to be scored.
    needs_score, desired_type = check_needs_score(good_things, bad_things, text)
    print(check_needs_score(good_things, bad_things, text))
    adjustment = 0
    polarity = 0

    if needs_score:
        # Call the get_adjustment function to determine the score adjustment
        adjustment = get_adjustment(text, desired_type)

    # Update the user's score based on the adjustment calculated above
    scores[user] = scores.get(user, 0) + adjustment

    # Check conditions for banning users or censoring messages
    if scores.get(user, 0) < -2:
        user = "<ADMIN>"
        text = "You have been banned."
    elif adjustment < -0.5:
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
    
    if len(text)<=40:
        return user, scores[user], adjustment, text
    
    segments = []
    length = len(text)
    i = 0
    while i < length:
        segment = text[i:i+40]
        segments.append(segment)
        i += 40
    return user, scores[user], adjustment, segments

