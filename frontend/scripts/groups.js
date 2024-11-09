async function fetchTrips() {
    // Здесь  код для запроса к базе данных
    data = {'lenders_tg': '@ivan'}
    res = await fetch('http://158.160.85.97:5000/get_trips?tg_tag=@ivan')
    res = await res.json();
    console.log(res);
    return res
    // Возвращаем для примера статичные данные
    // resolve([
    //     { lenders_tg: 'user1', amount: 100 },
    //     { lenders_tg: 'user2', amount: 200 },
    //     { lenders_tg: 'user3', amount: 150 }
    // ]);
}


// Функция для создания HTML элементов карточек пользователей
function createCard(trip) {
const card = document.createElement('div');
card.classList.add('card');
card.id = `user-${trip}`; // Устанавливаем уникальный id для каждой карточки
const nameElement = document.createElement('p');
nameElement.textContent = `${trip}`;  
nameElement.classList.add('name_of_user');
card.appendChild(nameElement);

return card;
}

// Выбираем контейнер, в который будем добавлять карточки пользователей
const container = document.getElementById('trips-container');

// Получаем данные о должниках и отображаем карточки на странице
fetchTrips().then(trips => {
trips.forEach(trip => {
    const card = createCard(trip);
    container.appendChild(card);
});
}).catch(error => {
console.error('Ошибка при получении данных: ', error);
});
