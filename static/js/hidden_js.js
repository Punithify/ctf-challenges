document.addEventListener('DOMContentLoaded', function () {

  const welcomeMessage = "Σηκώστε το πέπλο. Αναχαιτίστε τα μηνύματα καθώς περνά μέσα από αόρατα βασίλεια.";
  const welcomeDiv = document.getElementById('welcome');
  welcomeDiv.innerHTML = `<span class="greeky-style">${welcomeMessage}</span>`;

  fetch('/veil_of_secrets/get_scatter_text', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  }
})
  .then(response => response.json())
  .then(data => {
    const scatter_text = data.scatter_text;
    const container = document.getElementById('scatteredContainer');

    for (let i = 0; i < scatter_text.length; i++) {
      const letterSpan = document.createElement('span');
      letterSpan.textContent = scatter_text[i];
      letterSpan.className = 'letter';

      const randomX = Math.random() * window.innerWidth;
      const randomY = Math.random() * window.innerHeight;

      letterSpan.style.left = `${randomX}px`;
      letterSpan.style.top = `${randomY}px`;

      container.appendChild(letterSpan);
    }
  })
  .catch(error => console.error('Error fetching scatter text:', error));
});