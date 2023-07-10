import sys
import getopt
import os
import json

import openai


def usage():
    sys.stderr.write('-t <temperature>\n')
    sys.stderr.write('-h: print this help and exit\n')


openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)
options, args = getopt.getopt(sys.argv[1:], 't:h')
for opt, par in options:
    if opt == '-t':
        temperature = float(par)
    elif opt == '-h':
        usage()
        sys.exit(0)
if len(args) < 1:
    raise Exception('no animal (species) specified')
animal = args[0]
temperature = 0.6
prompt = """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: %s
Names:""" % animal
response = openai.Completion.create(model='text-davinci-003', prompt=prompt, temperature=temperature)
print(type(response))
print('response: %s' % response)
j = json.loads(str(response))
print(j)
