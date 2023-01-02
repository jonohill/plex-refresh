# plex-refresh

A hacky script to request Plex to refresh its libraries by path.
Requires `requests`.

## Usage

You'll need a [Plex token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/).

```
usage: plex_refresh.py [-h] --token TOKEN --url URL path [path ...]

Refresh Plex library by paths

positional arguments:
  path           Paths to refresh

optional arguments:
  -h, --help     show this help message and exit
  --token TOKEN  Plex token (or set PLEX_TOKEN)
  --url URL      Plex URL (or set PLEX_URL)
```
