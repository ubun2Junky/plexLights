import argparse

parser=argparse.ArgumentParser(description="Plex media player ID script.")

parser.add_argument('id', nargs = '+')

args = parser.parse_args()

print("DEVICE ID: " + str(args.id)