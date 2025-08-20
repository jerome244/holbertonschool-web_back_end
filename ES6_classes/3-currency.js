// 3-currency.js

export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() { return this._code; }

  set code(c) { this._code = c; }

  get name() { return this._name; }

  set name(n) { this._name = n; }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
