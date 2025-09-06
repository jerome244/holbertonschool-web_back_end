// 1-stdin.js
process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.setEncoding('utf8');

process.stdin.on('data', (chunk) => {
  // Echo the input as-is (don't trim), so tests comparing \r / \n pass
  process.stdout.write(`Your name is: ${chunk}`);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
