import facebook

token_file=open("access_token_user","r")
#Access token gets refreshed every 2 hours
access_token=token_file.read()

#initialize Graph API with access token
graph = facebook.GraphAPI(access_token)
#Pull the relevant fields from user's Facebook Profile
info = graph.request("/me?fields=birthday,education")
print("Jasleen's Birthday: "+info["birthday"])
for e in info["education"]:
    print(e["type"]+": "+e["school"]["name"])