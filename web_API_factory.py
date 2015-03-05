#!/usr/bin/python
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