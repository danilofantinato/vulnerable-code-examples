const AdmZip = require("adm-zip");
const upload = require('multer');
const path = require('path');

app.get('/example', upload.single('file'), (req, res) => {
    const zip = new AdmZip(req.file.buffer);
    const zipEntries = zip.getEntries();

    zipEntries.forEach(function (zipEntry) {
        const entryName = zipEntry.entryName;
        const sanitizedPath = path.join('uploads', path.basename(entryName));

        if (!sanitizedPath.startsWith('uploads/')) {
            // Entry path is outside the 'uploads' directory, skip it
            return;
        }

        const writer = fs.createWriteStream(sanitizedPath);
        writer.write(zipEntry.getData().toString("utf8"));
    });
});