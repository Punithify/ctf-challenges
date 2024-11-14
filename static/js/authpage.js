function submitLogin() {
  const password = document.getElementById("password").value;
  const responseBox = document.getElementById("response-box");

  const correctPassword = "letmeinnnnnnnnNMNMNnnnn"; 

  if (password === correctPassword) {

    fetch("/authpage/login", {
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ password: password })
      })
      .then(response => response.json())
      .then(data => {
          responseBox.innerText = data.message;
      })
      .catch(error => {
          responseBox.innerText = "An error occurred. Please try again.";
          console.error("Error:", error);
      });
  } else {
      responseBox.innerText = "Nuh uh!";
  }
}