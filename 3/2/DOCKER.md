# Usage with Docker
```
$ docker build -t yle-dl .
$ alias yle-dl='docker run -v $(pwd):/output yle-dl'
$ yle-dl https://areena.yle.fi/1-4234958
```
