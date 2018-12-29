# Usage with Docker
```
$ docker build -t yle-dl .
$ alias yle-dl='docker run --user $(id -u):$(id -g) -v $(pwd):/output yle-dl'
$ yle-dl https://areena.yle.fi/1-4234958
```
