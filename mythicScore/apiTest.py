import json
import requests
import numpy as np
import pandas as pd


def mythic_score(name, region, realm):
    url = "https://raider-io.p.rapidapi.com/api/v1/characters/profile"
    querystring = {"name": name, "region": region, "realm": realm, "fields":
        "guild,mythic_plus_ranks,mythic_plus_scores"}
    headers = {
        'x-rapidapi-host': "raider-io.p.rapidapi.com",
        'x-rapidapi-key': "69ebc4fe50mshc1e2a3b006f1fa8p1520a5jsn5dfec97ff0fb"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    new_output = json.loads(response.text)
    # Convert to a panda series to seperate data
    profile_se = pd.Series(new_output, name="Profile")
    # print(profile_se)
    # Convert series to a dataframe to access data easier
    profile_se.to_frame()
    # assign part of the dataframe to a variable to print later
    prof_basic = profile_se.loc["name":"active_spec_role"]
    # print(prof_basic.to_string(index=False))
    # Guild information/varable assignment
    guild_ds = pd.Series(profile_se.loc["guild"], name="Guild")
    guild_ds.to_frame()
    # print(guild_ds.to_string(index=False))
    # Mythic Score information
    mythic_sc = pd.Series(profile_se.loc["mythic_plus_scores"], name="Mythic Scores")
    mythic_sc.to_frame()
    mythic_sc_ds = mythic_sc.loc["all"]
    displayProfile = prof_basic.to_string(index=false)
    displayScore = mythic_sc_ds
    return displayProfile, displayScore
