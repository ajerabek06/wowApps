import json
import requests
import pandas as pd


class scoreSearch():
    url = "https://raider-io.p.rapidapi.com/api/v1/characters/profile"
    name = 'Läzerchïcken'
    region = 'us'
    realm = 'Tichondrius'
    #name=
    #name =
    #region =
    #realm =

    # querystring for accessing raider.io api
    querystring = {"name": name, "region": region, "realm": realm,
                   "fields": "mythic_plus_scores"}
    headers = {
        'x-rapidapi-host': "raider-io.p.rapidapi.com",
        'x-rapidapi-key': "69ebc4fe50mshc1e2a3b006f1fa8p1520a5jsn5dfec97ff0fb"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    new_output = json.loads(response.text)

    # Convert to a panda series to seperate data
    profile_se = pd.Series(new_output, name="Profile")

    # Convert series to a dataframe to access data easier
    profile_se.to_frame()

    # assign part of the dataframe to a variable to print later
    # prof_basic = profile_se.loc["name":"active_spec_role"]

    # Guild information/varable assignment
    # guild_ds = pd.Series(profile_se.loc["guild"], name="Guild")
    # guild_ds.to_frame()

    # Mythic Score information
    mythic_sc = pd.Series(profile_se.loc["mythic_plus_scores"], name="Mythic Scores")
    mythic_sc.to_frame()
    mythic_sc_ds = mythic_sc.loc["all"]

    ### Lets print it all out!!
    # print("Your basic character profile: ", prof_basic.to_string(index=False))
    # print("Your current Mythic Plus Score is: ", mythic_sc_ds)
    mythicscore = str(mythic_sc_ds)
    print(mythicscore)

    def __str__(self):
        return self.mythicscore
