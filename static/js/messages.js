const messages = document.querySelector('.messages');
const roomId = messages.getAttribute('data-room');
const userId = messages.getAttribute('data-user');
const userName = document.querySelector('#user').value;

function renderMessage(text, user, date) {
  const userClass = user == userName ? 'user-message' : '';
  const formattedDate = new Date(date).toLocaleDateString('pt-BR');

  let message = document.createElement('div');
  let username = document.createElement('strong');
  let dateInfo = document.createElement('time');
  let content = document.createElement('p');

  message.className = `message-item ${userClass}`.trim();
  username.textContent = user;
  dateInfo.textContent = formattedDate;
  content.textContent = text;

  [username, content, dateInfo].forEach((element) => {
    message.append(element);
  });

  return message;
}

function getMessages() {
  fetch(`/messages/${roomId}`)
    .then((response) => response.json())
    .catch((err) => console.error(err))
    .then((data) => {
      messages.innerHTML = '';

      data.messages.forEach((item) => {
        const { user, value, date } = item;
        const bubble = renderMessage(value, user, date);
        messages.append(bubble);
      });
    });
}

setInterval(getMessages, 1000);
