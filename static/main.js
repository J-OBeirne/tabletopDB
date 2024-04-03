function loadCharacters() {
  const request = new XMLHttpRequest();
  request.open("GET", "/characters", true);

  request.onload = () => {
    if (request.status >= 200 && request.status < 400) {
      const characters = JSON.parse(request.responseText);
      const list = document.getElementById("characters");

      list.innerHTML = characters
        .map((character) => `<li><a>load</a> ${character.Name}</li>`)
        .join("");
    }
  };

  request.onerror = () => {
    console.log("error loading characters");
  };

  request.send();
}
