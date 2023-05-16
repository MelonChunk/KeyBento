# Use the official Node.js image as the base
FROM node:14-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire frontend code
COPY . .

# Set the environment variable for the API URL
ARG REACT_APP_BASE_API_URL
ENV REACT_APP_BASE_API_URL=${REACT_APP_BASE_API_URL}

# Build the React app
RUN npm run build

# Expose the port on which the React app will run (e.g., 3000)
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
