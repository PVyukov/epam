How to run:
dockermi test; docker build . -t test
docker run -it  -p 5000:5000  -e MY_NAME="Pavel"  --name test --rm test

Note: MY_NAME is optional and can be ommited. In that way a default value ('no_name') will be used.

Note2: for debuging porpose: 
       add into Dockerfile 'ENV FLASK_ENV=development'
       run 'docker run -it  -p 5000:5000  -e MY_NAME="Pavel" -v /home/ubuntu/epam/Docker/task1/code:/code --name test --rm test'
