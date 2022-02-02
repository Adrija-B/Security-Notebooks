# My Security-Notebooks

This repo houses all my Datascience Notebooks for the Security Analysis Class[MSBX 5500] of 2022

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Adrija-B/Security-Notebooks/HEAD)

The built image is hosted on [Docker-Hub](https://hub.docker.com/layers/190215741/adrijab/my-datascience-notebook/latest/images/sha256-b8ee56e16d518c1fbbb712a55e98d620456f3cc36ae7b2f52fcc3aab38685fc3?context=repo).

## Using this repo
### With `docker`
Build:

```bash
docker build --rm -t adrijab/my-datascience-notebook .
#This uses the custom image for jupyter datascience notebook, as built on dockerhub. It is mounted to the current directry.
#The Jupyter Docker Stack used is 'jupyter/my-datascience-notebook', which had the 2022-01-24 tag and was retagged as adrijab/my-datascience-notebook, using the docker tag command.
```

Run:

```bash
docker run --rm -it -p 8888:8888 adrijab/my-datascience-notebook
# - Publishes on port 8888
# - Can also be opened using localhost:8888
```

### With `docker-compose`
Build and run:

```bash
docker-compose up
# This command publishes through port 8888 and custom image adrijab/my-datascience-notebook, as defined in the docker-compose.yml file
#Run this command from the repository terminal/command prompt to build your own container 
```
