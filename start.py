import dota2api
api = dota2api.Initialise('148C910CE1B3D72BD96B7DF714DD0531', raw_mode=True, language='zh_CN')

allGame = api.get_match_details(match_id=1640)
print(allGame)