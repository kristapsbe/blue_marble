https://dataspace.copernicus.eu/
https://documentation.dataspace.copernicus.eu/APIs/Token.html

https://documentation.dataspace.copernicus.eu/Applications/JupyterHub.html
a bunch of samples available here https://jupyterhub.dataspace.copernicus.eu/
looks like the examples are available here as well https://github.com/eu-cdse/notebook-samples/tree/main

## Run

```bash
using IJulia
notebook()
```

## Install

### Julia

```bash
brew install --cask julia
```

```bash
using Pkg
Pkg.add("IJulia")
```

```bash
using IJulia
notebook()
```

http://localhost:8888/

### Python

create virtual env

```bash
python3 -m venv .venv
```

activate virtual env

```bash
source .venv/bin/activate
```

```bash
python -m jupyterlab
```
