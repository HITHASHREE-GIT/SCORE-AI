# Use Node 20 image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Build the application
RUN npm run build

# Install serve to serve the built app
RUN npm install -g serve

# Expose the port
EXPOSE 5173

# Serve the built application
CMD ["serve", "-s", "dist", "-l", "5173"]