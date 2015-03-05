import pdb

dota2_scheme = {
    "url": "https://api.steampowered.com/",
    "methods": 
    {
        "history": 
        {
            "route": "IDOTA2Match_570/GetMatchHistory/V001/",
            "args": 
            {
                "key": 
                {
                   "default": "EDE9D1BECFFA03CDBEA638475F315DBA",
                   "required": "yes"
                },
                "hero_id": 
                {
                    "aliases": 
                    {    
                        "Abaddon": "102", 
                        "Abyssal Underlord": "108", 
                        "Alchemist": "73", 
                        "Ancient Apparition": "68", 
                        "Anti-Mage": "1", 
                        "Axe": "2", 
                        "Bane": "3", 
                        "Batrider": "65", 
                        "Beastmaster": "38", 
                        "Bloodseeker": "4", 
                        "Bounty Hunter": "62", 
                        "Brewmaster": "78", 
                        "Bristleback": "99", 
                        "Broodmother": "61", 
                        "Centaur Warrunner": "96", 
                        "Chaos Knight": "81", 
                        "Chen": "66", 
                        "Clinkz": "56", 
                        "Clockwerk": "51", 
                        "Crystal Maiden": "5", 
                        "Dark Seer": "55", 
                        "Dazzle": "50", 
                        "Death Prophet": "43", 
                        "Disruptor": "87", 
                        "Doom": "69", 
                        "Dragon Knight": "49", 
                        "Drow Ranger": "6", 
                        "Earth Spirit": "107", 
                        "Earthshaker": "7", 
                        "Elder Titan": "103", 
                        "Ember Spirit": "106", 
                        "Enchantress": "58", 
                        "Enigma": "33", 
                        "Faceless Void": "41", 
                        "Gyrocopter": "72", 
                        "Huskar": "59", 
                        "Invoker": "74", 
                        "Jakiro": "64", 
                        "Juggernaut": "8", 
                        "Keeper of the Light": "90", 
                        "Kunkka": "23", 
                        "Legion Commander": "104", 
                        "Leshrac": "52", 
                        "Lich": "31", 
                        "Lifestealer": "54", 
                        "Lina": "25", 
                        "Lion": "26", 
                        "Lone Druid": "80", 
                        "Luna": "48", 
                        "Lycanthrope": "77", 
                        "Magnus": "97", 
                        "Medusa": "94", 
                        "Meepo": "82", 
                        "Mirana": "9", 
                        "Morphling": "10", 
                        "Naga Siren": "89", 
                        "Nature's Prophet": "53", 
                        "Necrophos": "36", 
                        "Night Stalker": "60", 
                        "Nyx Assassin": "88", 
                        "Ogre Magi": "84", 
                        "Omniknight": "57", 
                        "Oracle": "111", 
                        "Outworld Devourer": "76", 
                        "Phantom Assassin": "44", 
                        "Phantom Lancer": "12", 
                        "Phoenix": "110", 
                        "Puck": "13", 
                        "Pudge": "14", 
                        "Pugna": "45", 
                        "Queen of Pain": "39", 
                        "Razor": "15", 
                        "Riki": "32", 
                        "Rubick": "86", 
                        "Sand King": "16", 
                        "Shadow Demon": "79", 
                        "Shadow Fiend": "11", 
                        "Shadow Shaman": "27", 
                        "Silencer": "75", 
                        "Skeleton King": "42", 
                        "Skywrath Mage": "101", 
                        "Slardar": "28", 
                        "Slark": "93", 
                        "Sniper": "35", 
                        "Spectre": "67", 
                        "Spirit Breaker": "71", 
                        "Storm Spirit": "17", 
                        "Sven": "18", 
                        "Techies": "105", 
                        "Templar Assassin": "46", 
                        "Terrorblade": "109", 
                        "Tidehunter": "29", 
                        "Timbersaw": "98", 
                        "Tinker": "34", 
                        "Tiny": "19", 
                        "Treant Protector": "83", 
                        "Troll Warlord": "95", 
                        "Tusk": "100", 
                        "Undying": "85", 
                        "Ursa": "70", 
                        "Vengeful Spirit": "20", 
                        "Venomancer": "40", 
                        "Viper": "47", 
                        "Visage": "92", 
                        "Warlock": "37", 
                        "Weaver": "63", 
                        "Windranger": "21", 
                        "Winter Wyvern": "112", 
                        "Wisp": "91", 
                        "Witch Doctor": "30", 
                        "Zeus": "22"
                    }
                },
                "game_mode": 
                {
                    "aliases": 
                    {
                        "None": "0",
                        "All Pick": "1",
                        "Captain's Mode": "2",
                        "Random Draft": "3",
                        "Single Draft": "4",
                        "All Random": "5",
                        "Intro": "6",
                        "Diretide": "7",
                        "Reverse Captain's Mode": "8",
                        "The Greeviling": "9",
                        "Tutorial": "10",
                        "Mid Only": "11",
                        "Least Played": "12",
                        "New Player Pool": "13",
                        "Compendium Matchmaking": "14",
                        "Captain's Draft": "16"
                    }
                },
                "skill": 
                {
                    "aliases": 
                    {
                        "Any": "0",
                        "Normal": "1",
                        "High": "2",
                        "very High": "3"
                    }
                },
                "date_min": {},
                "date_max": {},
                "min_players": {},
                "account_id": {},
                "league_id": {},
                "start_at_match_id": {},
                "matches_requested": {},
                "tournament_games_only": {}
            }
        },
        "details": 
        {
            "route": "IDOTA2Match_570/GetMatchDetails/v1/",
            "args": 
            {
                "key": 
                {
                   "default": "EDE9D1BECFFA03CDBEA638475F315DBA",
                   "required": "yes"
                },
                "match_id": 
                { 
                    "required": "yes"
                }
            }
        },
        "heroes":
        {
            "route": "IEconDOTA2_570/GetHeroes/v1/",
            "args":
            {
                "key": 
                {
                   "default": "EDE9D1BECFFA03CDBEA638475F315DBA",
                   "required": "yes"
                },
                "language": {},
                "itemizedonly" : {}
            }
        },
        "leagues": 
        {
            "route": "IDOTA2Match_570/GetLeagueListing/v1/",
            "args": 
            {
                "key": 
                {
                   "default": "EDE9D1BECFFA03CDBEA638475F315DBA",
                   "required": "yes"
                },
                "language": {}
            }
        }        
    }
    
}

class WebAPIFactory: 
    def __init__(self, scheme, query = None):
        self.scheme = scheme
        self.query = query

    def __str__(self):
        from urllib import urlencode
        if self.query is None:
            return self.scheme["url"]  

        def arg_required(arg_scheme):
            if "required" not in arg_scheme:
                return False
            required = arg_scheme["required"]
            return required == "Yes" or required == "yes"
        def get_required_args(method):
            args = method["args"]
            #print args
            return [arg_name for arg_name, arg_scheme in args.iteritems() if arg_required(arg_scheme) ] 
        def validate_args(args, method_name):
            method = self.scheme["methods"][method_name]
            required_args = get_required_args(method)
            for required_arg in required_args:
                if required_arg not in args:
                    message = "Missing required argument '%s' in method '%s'" % (required_arg, method_name)
                    raise AttributeError(message)   

        url = self.scheme["url"]
        method_name = self.query[0]
        method = self.scheme["methods"][method_name]
        route = method["route"]
        args = self.query[1]
        validate_args(args, method_name)     

        return url + route + "?" + urlencode(args , True)      

    def __getattr__(self, attr):
        methods = self.scheme["methods"]
        def build_empty(method_name):
            if not method_name in methods:
                message = "Missing method '%s' in scheme" % method_name
                raise AttributeError(message)
            args_scheme = methods[method_name]["args"]
            #pdb.set_trace()
            default_args = {k: v["default"] for k, v in args_scheme.iteritems() if "default" in v}
            query = (method_name, default_args)
            return WebAPIFactory(self.scheme, query)

        def build_existing(arg_name, arg_value): 
            from copy import deepcopy 

            method_name = self.query[0]
            args_scheme = methods[method_name]["args"]
            if not arg_name in args_scheme:
                message = "Missing argument '%s' in method '%s'" % (arg_name, method_name)
                raise AttributeError(message)
            arg_scheme = args_scheme[arg_name]
            if "aliases" in arg_scheme:
                aliases = arg_scheme["aliases"]
                arg_value = aliases.get(arg_value, arg_value)

            args = deepcopy(self.query[1])
            args[arg_name] = arg_value
            query = (method_name, args)
            return WebAPIFactory(self.scheme, query)

        def build(attr, value):
            if self.query is None:
                return build_empty(attr)
            else:
                return build_existing(attr, value)  
                    
        def callable(value = None):
            return build(attr, value)
        return callable


#dota2 = WebAPIFactory(dota2_scheme)
#print wapi.history().hero_id("Abaddon")
#print dota2.details().match_id("234234234")
#print dota2.leagues()
#print dota2.heroes()

import json 
#with open("dot2_scheme.json", "w") as file:
#    json.dump(dota2_scheme, file, ensure_ascii = False ,  sort_keys = True, indent = 4)
with open("dot2_scheme.json") as file:
    scheme = json.loads(file.read())
    dota2 = WebAPIFactory(scheme)
    print dota2.history().hero_id("Abaddon")