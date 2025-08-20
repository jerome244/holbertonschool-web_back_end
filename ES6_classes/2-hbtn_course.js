// 2-hbtn_course.js

export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    if (typeof length !== 'number') throw new TypeError('Length must be a number');
    if (!Array.isArray(students) || !students.every((s) => typeof s === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() { return this._name; }

  set name(n) {
    if (typeof n !== 'string') throw new TypeError('Name must be a string');
    this._name = n;
  }

  get length() { return this._length; }

  set length(l) {
    if (typeof l !== 'number') throw new TypeError('Length must be a number');
    this._length = l;
  }

  get students() { return this._students; }

  set students(s) {
    if (!Array.isArray(s) || !s.every((x) => typeof x === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = s;
  }
}
