#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];

fs.readfile(filePath, 'utf8', function(err, data) {
	if (err) {
		console.error(err);
	} else {
		console.log(data);
	}
});

