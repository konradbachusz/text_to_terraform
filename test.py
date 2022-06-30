import re


org_string = """[31m╷[0m[0m
[31m│[0m [0m[1m[31mError: [0m[0m[1mArgument or block definition required[0m
[31m│[0m [0m
[31m│[0m [0m[0m  on main.tf line 1:
[31m│[0m [0m   1: [4mdfvfdv[0m[0m
[31m│[0m [0m
[31m│[0m [0mAn argument or block definition is required here. To set an argument, use
[31m│[0m [0mthe equals sign "=" to introduce the argument value.
[31m╵[0m[0m"""
pattern = r'31'
# Replace all occurrences of character s with an empty string
mod_string = re.sub(pattern, '', org_string )
print(mod_string)

def 