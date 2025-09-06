// 2-read_file.js
const fs = require('fs');

function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(path, 'utf-8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = content
    .split('\n')
    .filter((line) => line.trim().length > 0);

  if (lines.length <= 1) {
    console.log('Number of students: 0');
    return;
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

  console.log(`Number of students: ${total}`);
  Object.keys(studentsByField)
    .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
    .forEach((field) => {
      const list = studentsByField[field].join(', ');
      console.log(`Number of students in ${field}: ${studentsByField[field].length}. List: ${list}`);
    });
}

module.exports = countStudents;
