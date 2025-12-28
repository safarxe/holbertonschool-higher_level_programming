const header = document.querySelector('header');
const redDiv = document.getElementById('red_header');

redDiv.addEventListener('click', () => {
  header.classList.add('red');
});