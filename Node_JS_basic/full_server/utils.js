// full_server/utils.js
import fs from 'fs';

export default function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim().length > 0);

      if (lines.length <= 1) {
        resolve({});
        return;
      }

      const byField = {};

      for (let i = 1; i < lines.length; i += 1) {
        const parts = lines[i].split(',');
        if (parts.length >= 4) {
          const firstname = parts[0].trim();
          const field = parts[3].trim();
          if (firstname && field) {
            if (!byField[field]) byField[field] = [];
            byField[field].push(firstname);
          }
        }
      }

      resolve(byField);
    });
  });
}
