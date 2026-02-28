const fs = require('fs');

function countStudents(path) {
    let content;
    try {
        content = fs.readFileSync(path, 'utf-8');
    } catch (err) {
        throw new Error('Cannot load the database');
    }

    const lines = content.split('\n').filter((l) => l.trim() !== '');
    if (lines.length === 0) {
        console.log('Number of students: 0');
        return;
    }

    // ilk satır başlık olduğu için atla
    const header = lines.shift();
    const fields = {};
    lines.forEach((line) => {
        const parts = line.split(',');
        if (parts.length < 4) return; // geçersiz
        const field = parts[3].trim();
        const firstname = parts[0].trim();
        if (firstname === '' || field === '') return;
        if (!fields[field]) {
            fields[field] = [];
        }
        fields[field].push(firstname);
    });

    const total = Object.values(fields).reduce((acc, arr) => acc + arr.length, 0);
    console.log(`Number of students: ${total}`);
    Object.keys(fields).forEach((f) => {
        console.log(`Number of students in ${f}: ${fields[f].length}. List: ${fields[f].join(', ')}`);
    });
}

module.exports = countStudents;
