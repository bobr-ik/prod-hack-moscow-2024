function fetchDebtors() {
    return new Promise((resolve, reject) => {
        // Здесь должен быть ваш код для запроса к базе данных
        // Возвращаем для примера статичные данные
        resolve([
            { debtor_tg: 'user1', amount: 100 },
            { debtor_tg: 'user2', amount: 200 },
            { debtor_tg: 'user3', amount: 150 }
        ]);
    });
}

// Функция для создания HTML элементов карточек пользователей
function createCard(debtor) {
    const card = document.createElement('div');
    card.classList.add('card');
    card.id = `user-${debtor.debtor_tg}`; // Устанавливаем уникальный id для каждой карточки

    const nameElement = document.createElement('p');
    nameElement.textContent = `Пользователь: ${debtor.debtor_tg}`;

    const amountElement = document.createElement('p');
    amountElement.textContent = `Сумма: ${debtor.amount} ₽`;

    const payButton = document.createElement('button');
    payButton.textContent = 'forgive';
    payButton.classList.add('pay_button');
    payButton.addEventListener('click', () => {
        const targetCard = document.getElementById(`user-${debtor.debtor_tg}`);
        targetCard.style.display = 'none';
    });

    card.appendChild(nameElement);
    card.appendChild(amountElement);
    card.appendChild(payButton);

    return card;
}

// Выбираем контейнер, в который будем добавлять карточки пользователей
const container = document.getElementById('users-container');

// Получаем данные о должниках и отображаем карточки на странице
fetchDebtors().then(debtors => {
    debtors.forEach(debtor => {
        const card = createCard(debtor);
        container.appendChild(card);
    });
}).catch(error => {
    console.error('Ошибка при получении данных: ', error);
});