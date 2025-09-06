// full_server/controllers/StudentsController.js
import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    const dbPath = process.argv[2];

    try {
      const byField = await readDatabase(dbPath);
      const fields = Object.keys(byField)
        .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      const lines = ['This is the list of our students'];
      fields.forEach((field) => {
        const list = byField[field] || [];
        lines.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      });

      return res.status(200).type('text/plain').send(lines.join('\n'));
    } catch (err) {
      return res.status(500).type('text/plain').send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const dbPath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).type('text/plain').send('Major parameter must be CS or SWE');
    }

    try {
      const byField = await readDatabase(dbPath);
      const list = byField[major] || [];
      return res.status(200).type('text/plain').send(`List: ${list.join(', ')}`);
    } catch (err) {
      return res.status(500).type('text/plain').send('Cannot load the database');
    }
  }
}

export default StudentsController;
