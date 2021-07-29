import json
import sys

def generateFakeData(arguments):
  fakeData = {}
  for index,arg in enumerate(arguments):
      fakeData[arg] = {
        'positive': 100,
        'negative': 3,
        'topics': ['cool', 'topic', 'bro']
      }
  return fakeData;

def writeFakeData(dir, data):
  print(dir + '/data.json')
  with open(dir + '/executors/data.json', 'w') as file:
    json.dump(data, file)

def main():
  args = sys.argv
  print(args)
  print('Generating Fake data...')
  fakeData = generateFakeData(args)
  print('Writing Fake data...')
  writeFakeData(sys.argv[0], fakeData)
  print('Complete!')


main();