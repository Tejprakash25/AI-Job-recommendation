function load() {
  fetch("http://localhost:8080/api/recommendations")
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").textContent =
        JSON.stringify(data, null, 2);
    });
}
