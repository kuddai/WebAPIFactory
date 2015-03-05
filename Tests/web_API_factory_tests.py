#!/usr/bin/python
import sys
sys.path.append("../")
import web_API_factory
import unittest
import json

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        #fixture data
        #api description https://wiki.teamfortress.com/wiki/WebAPI/GetMatchDetails        
        with open("dot2_scheme.json") as file:
            dota2_scheme = json.loads(file.read())  
            self.dota2 = web_API_factory.WebAPIFactory(dota2_scheme)      
            
    def test_default_url (self):
        self.assertEqual(str(self.dota2), "https://api.steampowered.com/")

    def test_default_args(self):
        result = str(self.dota2.history())
        answer = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=your_steam_key_here"
        self.assertEqual(result, answer)

    def test_required_arg_error(self):
        with self.assertRaises(AttributeError):
            str(self.dota2.details())

    def test_missing_method_error(self):
        with self.assertRaises(AttributeError):
            str(self.dota2.raki_dno())

    def test_missing_arg(self):
        with self.assertRaises(AttributeError):
            str(self.dota2.history().missing_arg())

    def test_aliases(self):
        result = str(self.dota2.history().hero_id("Abaddon"))
        answer = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=your_steam_key_here&hero_id=102"
        self.assertEqual(result, answer)        

    def test_concatenation(self):
        result = str(self.dota2.history().hero_id("Abaddon").min_players(8))
        answer = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?min_players=8&key=your_steam_key_here&hero_id=102"

    def test_independence(self):
        history = self.dota2.history()

        result1 = str(history.skill("Any").game_mode("All Pick"))
        answer1 = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?game_mode=1&skill=0&key=your_steam_key_here"
        self.assertEqual(result1, answer1)

        result2 = str(history.min_players(4))
        answer2 = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?min_players=4&key=your_steam_key_here"
        self.assertEqual(result2, answer2)

if __name__ == '__main__':
    unittest.main()