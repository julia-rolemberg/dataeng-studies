FROM node

# by default the workdir is the root folder, so we have to change it to /app
WORKDIR /app

COPY package.json .

RUN npm install

# copy all files and folders to be seen by the image inside the folder root directory (/app)
COPY . .

#exposing a port so we can access it outside the container (documentation purpose)
# to make it work, you have to add the flag -p 8080:80 on docker run command (docker run -p 8080:80 image_id)
EXPOSE 80

# CMD just run when the container is running, not during image's build
CMD ["node", "server.js"]