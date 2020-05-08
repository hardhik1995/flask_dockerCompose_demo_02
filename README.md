# flask_dockerCompose_demo_02

https://pythonise.com/series/learning-flask/building-a-flask-app-with-docker-compose


#Docker -Compose
Every docker-compose.yml file must start with the version, followed by the services we want to build using services: and indenting any individual services thereafter. In our case - version: "3.7".

We've defined 2 individual services in the services block and named them flask and nginx respectively.

    build: ./flask - Instructs Docker to build the image using the Dockerfile found in the flask directory (relative to the docker-compose.yml file)
    container_name: flask - Gives our container the name of flask, also assigning it that hostname as we mentioned earlier
    restart: always - Makes the container always restart
    environment - A place for us to define environment variables for the container.
    expose - Exposes internal ports to other containers and services on the same network
