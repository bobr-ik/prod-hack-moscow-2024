async function fetchDebtors() {
    data = {'lenders_tg': '@ivan'}
    res = await fetch('http://158.160.85.97:5000/get_user_debtors?lender_tg=@ivan')
    res = await res.json();
    console.log(res);
    return res
}

// Функция для создания HTML элементов карточек пользователей
function createCard(debtor) {
    const card = document.createElement('div');
    card.classList.add('card');
    card.id = `user-${debtor.debtor_tg}`; // Устанавливаем уникальный id для каждой карточки

    const nameElement = document.createElement('p');
    nameElement.textContent = ` ${debtor.debtor_tg}`;

    const amountElement = document.createElement('p');
    const amountElementCaption=document.createElement('p');
    amountElement.textContent = `Сумма: ${debtor.amount} ₽`;

    const payButton = document.createElement('button');
    payButton.textContent = 'forgive';
    payButton.classList.add('pay_button');
    payButton.addEventListener('click', () => {
        const targetCard = document.getElementById(`user-${debtor.debtor_tg}`);
        targetCard.style.display = 'none';
        fetch('http://158.160.85.97:5000/remove_debt?lender_tg=' + '@ivan' + '&debtor_tg=' + debtor.debtor_tg, {method: 'DELETE'});
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