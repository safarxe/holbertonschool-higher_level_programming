document.addEventListener('DOMContentLoaded', () => {
  const btnTranslate = document.getElementById('btn_translate');
  const langSelect = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  btnTranslate.addEventListener('click', () => {
    const lang = langSelect.value;
    if (!lang) return;

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(error => console.error('Xəta:', error));
  });
});