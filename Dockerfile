# add host="0.0.0.0" to app.run() in driver.py file so that we can access container from browser / postman:
# app.run(host="0.0.0.0", port=6000, debug=True) P.S use port 6000 on mac coz 5000 is used for airplay
FROM python:3.9-alpine

COPY . .

RUN pip install -r requirements.txt


# expose ports of container at which our python code will be running, since app inside container will be running on 6000
# expose means make it available
# exposing for both flask app & redis we can map with `docker run -p 80:80 -p 443:443 my-image`
EXPOSE 6000


# use CMD keyword for running command inside container, all the above instrunction will be
# executed while building the image cmd: python3 driver.py
CMD [ "python3", "driver.py" ]


# how to build image + container & run
# docker build --tag <your custom image name> <path/to/Dockerfile>
# or
# cd <to/folder/where/Dockerfile>
# docker build --tag <your custom image tag name> .
# docker run -p hostPort:DockerPort <tag> i.e docker run -p 5000:5000 -p 6379:6379 <your custom image tag name>

# `docker ps -a` lists all the images running (i.e container) and also not running
# `docker images` or `docker image ls` prints all the built images
# `docker ps` lists all the images that are running but do not show the non running images