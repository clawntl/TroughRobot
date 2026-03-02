fetch("/api/hello")
  .then(r => r.json())
  .then(data => {
    document.getElementById("message").textContent = data.message;
  })
  .catch(err => console.error(err));
