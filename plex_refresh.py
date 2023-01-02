#!/usr/bin/env python3

import argparse
from os import getenv

import requests


PLEX_TOKEN = getenv('PLEX_TOKEN')
PLEX_URL = getenv('PLEX_URL')


def list_libraries():
    url = f'{args.url}/library/sections'
    headers = {
        'X-Plex-Token': args.token,
        'Accept': 'application/json',
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()['MediaContainer']['Directory']


def scan_library(key: str, path: str):
    url = f'{args.url}/library/sections/{key}/refresh'
    headers = {
        'X-Plex-Token': args.token,
        'Accept': 'application/json',
    }
    params = {
        'path': path,
    }
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()


def scan_paths(paths: list[str]):
    for path in paths:
        for library in list_libraries():
            for location in library['Location']:
                lib_path = location['path']
                if path.startswith(lib_path):
                    scan_library(library['key'], path)
                    yield library['title'], path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Refresh Plex library by paths')
    parser.add_argument('--token', required=not PLEX_TOKEN, default=PLEX_TOKEN, help='Plex token (or set PLEX_TOKEN)')
    parser.add_argument('--url', required=not PLEX_URL, default=PLEX_URL, help='Plex URL - full URL including port (or set PLEX_URL)')
    parser.add_argument('path', nargs='+', help='Paths to refresh')
    args = parser.parse_args()

    PLEX_TOKEN = args.token
    PLEX_URL = args.url

    did_scan = False
    for library, path in scan_paths(args.path):
        did_scan = True
        print(f"Scanned {library} at {path}")
    
    if not did_scan:
        print("No libraries found for paths", args.path)
