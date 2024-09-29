# Use an official Node.js image as the base image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json into the container
COPY package.json package-lock.json ./

# Install the app dependencies
RUN npm install

# Copy the entire app into the container
COPY . .

# Expose the port that Expo runs on
EXPOSE 19000

# Run the Expo development server
CMD ["npm", "start"]
