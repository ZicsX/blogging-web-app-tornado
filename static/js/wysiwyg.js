function link() {
  var url = prompt("Enter the URL");
  document.execCommand("createLink", false, url);
}

function copy() {
  document.execCommand("copy", false, "");
}

function changeColor() {
  var color = prompt("Enter your color in hex ex:#f1f233");
  document.execCommand("foreColor", false, color);
}

function getImage() {
  var file = document.querySelector("input[type=file]").files[0];
  var editorContent = document.querySelector("#editor");

  var reader = new FileReader();

  let dataURI;

  reader.addEventListener(
    "load",
    function() {
      dataURI = reader.result;

      const img = document.createElement("img");
      img.src = dataURI;
      editorContent.appendChild(img);
    },
    false
  );

  if (file) {
    reader.readAsDataURL(file);
  }
}
