var TurndownService = require('turndown')

var turndownService = new TurndownService({ headingStyle: 'atx' })

var fs = require('fs')
const fsjson = require('fs-extra')
const mydata = fsjson.readJsonSync('./webs.json')

for (i = 0; i < Object.keys(mydata).length; i++) {
    fs.writeFile(mydata[i].archive, turndownService.turndown(mydata[i].html), function(err) {
        if (err) {
            return console.log(err);
        }

        console.log("The file was saved!");
    });
}