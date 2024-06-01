const encryptText = () => {
    let s_text = source_text.innerText;
    let d_string = "";
    for (const char of s_text) {
      let nc = String.fromCharCode(char.charCodeAt(0) + 3);
      d_string = d_string.concat(nc);
    }
    result_text.innerText = d_string;
  };
  const decryptText = () => {
    let s_text = source_text.innerText;
    let d_string = "";
    for (const char of s_text) {
      let nc = String.fromCharCode(char.charCodeAt(0) - 3);
      d_string = d_string.concat(nc);
    }
    result_text.innerText = d_string;
  };
  const saveButtonClick = () => {
    if(dest_filename.value){
      window.electron.writeFile(dest_filename.value, result_text.innerText);
      window.location.reload();
    }
    else{
      dest_filename.style.borderColor="red"
      setTimeout(()=>dest_filename.style.borderColor="var(--border-color-1)", 400);
    }
  };
  const deleteButtonClick = () => {
    window.electron.deleteFile(source_filename.innerText);
    window.location.reload();
  }
  const source_filename = window.document.querySelector("#source-file-name");
  const dest_filename = window.document.querySelector("#dest-file-name");
  const source_text = window.document.querySelector("#source-text");
  const result_text = window.document.querySelector("#result-text");
  const encryptButton = window.document.querySelector("#encrypt-button");
  const decryptButton = window.document.querySelector("#decrypt-button");
  const saveButton = window.document.querySelector("#save-button");
  encryptButton.addEventListener("click", encryptText);
  decryptButton.addEventListener("click", decryptText);

  const addFileListItem = (fileName) => {
    let div = window.document.createElement("div");
    div.className = "file-block";
    let p = window.document.createElement("p");
    let span = window.document.createElement("span");
    let file_title = window.document.querySelector("#source-file-name");

    p.innerText = fileName;
    p.className = "file-name";
    span.className = "material-symbols-outlined";
    span.innerText = "description";
    div.appendChild(span);
    div.appendChild(p);
    div.addEventListener("click", () => {
      file_title.innerText = fileName;
      source_text.innerText = window.electron.readFile(fileName);
      result_text.innerText = "";
    });
    window.document.querySelector("#file_list").appendChild(div);
  };

  const getFileList = () => {
    let files = window.electron.getFileNames();
    if (files) {
      let filesArray = files.split("\n");
      filesArray.map((elem) => addFileListItem(elem));
    }
  };
  getFileList();
// Modal
let modal = document.getElementById("helpModal");

let btn = document.getElementById("help-button");

let span = document.getElementById("modal-close");

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}