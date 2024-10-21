https://dataspace.copernicus.eu/
https://documentation.dataspace.copernicus.eu/APIs/Token.html

probably python?

https://pipx.pypa.io/stable/installation/

set up virtualenv
```bash
pipx install virtualenv
```

create virtual env
```bash
python3 -m venv .venv
```

activate virtual env
```bash
source .venv/bin/activate
```

* pull sentinel 2 images
* make low-ish (but not too low-ish) resolution picture of the world
* overlay with borders and cities (openstreetmaps?)
* make app using webasembly, that lets you move the globe around, and switch to a "color where I've been" mode
* make app that allows for the same
* refresh the image of the world every week (?)

do I store any user data?
