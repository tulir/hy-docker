# DinD build and hub push
## Usage
1. Build the builder with
   ```bash
   docker build -t dind-builder .
   ```
2. Add an alias for easy usage
   ```bash
   alias 'build-hub'='docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v '$HOME'/.docker:/.docker dind-builder'
   ```
3. Use alias to build and push images
   ```bash
   build-hub <git repo> <docker hub tag>
   ```

## Info
The [Dockerfile](Dockerfile) simply extends the official docker in docker image
([_/docker](https://hub.docker.com/_/docker), installs bash and copies the
build script.

The [build script](build.sh) logs in if necessary, clones the repo given in the
first parameter, builds the image with the tag given in the second parameter
and pushes the result to docker hub.

The alias (step 2 above) makes it easy to run with the necessary mounts.

## Caveats
The docker image runs as root, as the script requires access to the mounted
`/var/run/docker.sock` and there is no way to set the permissions of volume
mounts. This means that logging in inside the builder will cause the users
docker config to be owned by root. This could perhaps be avoided by changing
user inside the build script.
