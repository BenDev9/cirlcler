# Circler #

Circler is a quick script I put together for International Pi Day that draws (nearly) perfect circles on [this](https://neal.fun/perfect-circle/) website. This is just a fun proof-of-concept project, so please don't use it to cheat in any competitions or anything :)

## Use #

*Note: a lot of these parameters are non-functional, and will be implemented in the future*

```text
usage: circle [-h] [-a] [-r RADIUS] [-t TRIES] [-m] fidelity

Draws a (hopefully) perfect circle on https://neal.fun/perfect-circle/

positional arguments:
  fidelity              the number of vertices of the circle

optional arguments:
  -h, --help            show this help message and exit
  -a, --audio           use audio or not
  -r RADIUS, --radius RADIUS
                        the radius of the circle
  -t TRIES, --tries TRIES
                        the number of tries to do
  -m, --manual          use manual mode or not
```
