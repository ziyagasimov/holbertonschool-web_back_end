module.exports = {
  env: {
    browser: true,
    es6: true, // "es2021" əvəzinə "es6" yazın
    jest: true,
    node: true,
  },
  extends: 'eslint:recommended',
  parserOptions: {
    ecmaVersion: 2018, // "latest" əvəzinə 2018 yazmaq daha təhlükəsizdir
    sourceType: 'module',
  },
  rules: {
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
};