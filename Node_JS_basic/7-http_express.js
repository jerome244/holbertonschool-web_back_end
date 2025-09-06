// 7-http_express.js
const express = require('express');
const fs = require('fs');

function buildReportFromData(data) {
  const lines = data
    .split('\n')
    .filter((line) => line.trim().length > 0);

  if (lines.length <= 1) {
    return 'Number of students: 0';
  }

  const studentsByField = {};
  let total = 0;

  for (let i = 1; i < lines.length; i += 1) {
    const parts = lines[i].split(',');
    if (parts.length >= 4) {
      const firstname = parts[0].trim();
      const field = parts[3].trim();
      if (firstname && field) {
        if (!studentsByField[field]) studentsByField[field] = [];
        studentsByField[field].push(firstname);
        total += 1;
      }
    }
  }

  const out = [`Number of students: ${total}`];
  Object.keys(studentsByField)
    .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
    .forEach((field) => {
      out.push(`Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}`);
    });

  return out.join('\n');
}

function getStudentsReport(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      resolve(buildReportFromData(data));
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const dbPath = process.argv[2];
  getStudentsReport(dbPath)
    .then((report) => res.status(200).type('text/plain').send(`This is the list of our students\n${report}`))
    .catch(() => res.status(200).type('text/plain').send('This is the list of our students\nCannot load the database'));
});

app.listen(1245);

module.exports = app;
