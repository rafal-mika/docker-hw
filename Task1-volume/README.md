# Task 1 - docker-volume

Application is looking for the config file in path ``/app/data``

1. To build docker image, run command ``docker build -t <your-image-name> <dockerfile-path>``

    e.g. ``docker build -t my-app-img .``   (when dockerfile is located in your current directory)

2. Config file is passed inside container via volume. Default ``config.json`` file is available in ``config`` directory

    To run container, use command ``docker run --name <your-container-name> -v <config-file-path-in-host-os>:/app/data <your-image-name>``
    
    e.g. ``docker run --name py-app -v ${pwd}/config:/app/data my-app-img``


  
