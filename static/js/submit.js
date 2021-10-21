const form = document.querySelector('form');
const message = document.querySelector('#message');
const token = document.querySelector('input[name=csrfmiddlewaretoken]');
const csrftoken = token.value;

form.addEventListener('submit', (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const ajax = {
    method: 'POST',
    credentials: 'same-origin',
    headers: { 'X-CSRFToken': csrftoken },
    body: formData,
  };

  fetch('/send', ajax)
    .then((response) => response.text())
    .catch((err) => console.error(err))
    .then((data) => console.log(data));

  message.value = '';
});
