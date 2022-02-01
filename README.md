# Security-Notebooks

This repo houses all Notebooks for the Security Analysis Class of '2022'

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Adrija-B/Security-Notebooks/HEAD)

The built image is [hosted on Docker-Hub](https://hub.docker.com/layers/190215741/adrijab/my-datascience-notebook/latest/images/sha256-b8ee56e16d518c1fbbb712a55e98d620456f3cc36ae7b2f52fcc3aab38685fc3?context=repo).

## Using this repo
### With `docker`
Build:

```bash
docker build --rm -t adrijab/my-datascience-notebook .
docker image ls
# Should explain how to build the image, including tagging it
```

Run:

```bash
docker run --rm -it -p 8888:8888 adrijab/my-datascience-notebook
# - Should publish port 8888
# - Should mount the local directory as a volume in the
#   container's home directory
# - Should `--rm` container when done
# - Should use `-it` mode
```

### With `docker-compose`
Build and run:

```bash
docker-compose up
# - It should publish port 8888
# - It should mount the local directory as a volume in the container's
#   home directory
```
