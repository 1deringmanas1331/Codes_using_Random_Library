// Import required modules
const http = require('http');

// Declare the function
function generateRandomPort() {
  return Math.floor(Math.random() * (9100 - 2500 + 1)) + 2500;
}


const server = http.createServer((req, res) => {
// Print the status code
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello, this is a random server!\n');
});

// Generate the random port number
const port = generateRandomPort();


server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
