// See the Electron documentation for details on how to use preload scripts:
// https://www.electronjs.org/docs/latest/tutorial/process-model#preload-scripts
const {app, contextBridge} = require('electron');
const path = require('path');
const fs = require('fs');
const homedir = require('os').homedir();

const getFilePath = (fileName) => path.join(homedir, 'files', fileName);


contextBridge.exposeInMainWorld('electron',{
    desktop: true,
    getFileNames: () =>{
        try {
        fs.mkdirSync(path.join(homedir, 'files'));
        }
        catch(err){
            console.log(err.message);
        }
        let files = fs.readdirSync(path.join(homedir, 'files'));
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