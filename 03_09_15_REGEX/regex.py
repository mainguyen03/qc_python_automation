import re

filename = 'animal_code.google.com'
text = open(filename, "r")
host = re.search(r'_(.*)',filename).group(1)
print (host)
for line in text:
    line = line.strip()
    match_obj = re.search(r'GET (.*?) HTTP', line).group(1)
    path = "http://" + host + '/' + match_obj
    print(path)
