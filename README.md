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

TODO: I get 30'000 processing units, can't spam them too much
https://www.sentinel-hub.com/pricing/#tab-plans ?

inspiration https://rawcdn.githack.com/sciecode/three.js/f4e363a8e0cf6c496f4191192d7eb15110442a7c/examples/webgl_paint_texture.html