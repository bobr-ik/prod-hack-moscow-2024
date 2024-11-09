 async function fetchLenders() {
        // Здесь должен быть ваш код для запроса к базе данных
        // Возвращаем для примера статичные данные
        data = {'lenders_tg': '@ivan'}
        res = await fetch('http://127.0.0.1:5000/get_user_lenders?debtor_tg=@ivan')
        res = await res.json();
        console.log(res);
        return res
        // resolve([
        //     { lenders_tg: 'user1', amount: 100 },
        //     { lenders_tg: 'user2', amount: 200 },
        //     { lenders_tg: 'user3', amount: 150 }
        // ]);
    }


// Функция для создания HTML элементов карточек пользователей
function createCard(lender) {
    const card = document.createElement('div');
    card.classList.add('card');
    card.id = `user-${lender.lenders_tg}`; // Устанавливаем уникальный id для каждой карточки

    const nameElement = document.createElement('p');
    nameElement.textContent = `${lender.lenders_tg}`;  
    const amountElement = document.createElement('p');
    nameElement.classList.add('name_of_user');
    amountElement.textContent = `Сумма: ${lender.amount} ₽`;

    const payButton = document.createElement('button');
    payButton.textContent = 'pay';
    payButton.classList.add('pay_button');
    payButton.addEventListener('click', () => {
        const targetCard = document.getElementById(`user-${lender.lenders_tg}`);
        targetCard.style.display = 'none';
        fetch('http://127.0.0.1:5000/remove_debt?lender_tg=' + lender + '&debtor_tg=' + '@ivan', {method: 'DELETE'});
    });

    card.appendChild(nameElement);
    card.appendChild(amountElement);
    card.appendChild(payButton);

    return card;
}

// Выбираем контейнер, в который будем добавлять карточки пользователей
const container = document.getElementById('users-container');

// Получаем данные о должниках и отображаем карточки на странице
fetchLenders().then(lenders => {
    lenders.forEach(lender => {
        const card = createCard(lender);
        container.appendChild(card);
    });
}).catch(error => {
    console.error('Ошибка при получении данных: ', error);
});
