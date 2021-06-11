# Continuous Requests in Python

A simple container that executes a get request from a Python script. It can repeat the get request indefinitely with a custom interval.

The container is based on Alpine Linux 3.7 and the Python `requests` library.

## Usage

```sh
docker run [-d|--rm] [OPTION...] continuous-curl URL
```

### Available options as environment variables

- URL: the destination URL
- INTERVAL: the time (in seconds) between requests

## Examples

```sh
docker run --rm --env URL=https://google.com --env INTERVAL=2 julianosk/continuous-requests-py:latest
```

```sh
docker run -d --rm --env URL=https://google.com --env INTERVAL=5 julianosk/continuous-requests-py:latest
```

## Source

<https://github.com/julianosk/continuous-requests-py>
