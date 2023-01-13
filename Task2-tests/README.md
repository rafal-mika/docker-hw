## Task2 Docker - testing while image building

Dockerfile configuration allows running application tests while image building.

Tests are running by default.
You can change the setting by passing build argument RUN_TESTS, set 'true' or 'false'

Building docker image will be stopped if tests failed.

To build docker image, run ``docker build --build-arg RUN_TESTS=<true/false> -t <image-name> <dockerfile-path>``
