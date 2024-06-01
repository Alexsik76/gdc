// See the Electron documentation for details on how to use preload scripts:
// https://www.electronjs.org/docs/latest/tutorial/process-model#preload-scripts
const {contextBridge} = require('electron');
const path = require('path');
const fs = require('fs');

const getFilePath = (fileName) => path.join(__dirname, 'files', fileName);


contextBridge.exposeInMainWorld('electron',{
    desktop: true,
    getFileNames: () =>{
        let files = fs.readdirSync(path.join(__dirname, 'files'));
        console.log(__dirname);
        return files.join('\n');
    },
    readFile: (fileName) =>{
        let fileText = fs.readFileSync(getFilePath(fileName), 'utf8');
        return fileText;
    },
    writeFile: (file_name, text) => {
        fs.writeFileSync(getFilePath(`${file_name}.txt`), text);
    },
    deleteFile: (fileName) => fs.unlinkSync(getFilePath(fileName))
})