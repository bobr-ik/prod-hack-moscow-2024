async function fetchTrips() {
    // Здесь  код для запроса к базе данных
    data = {'lenders_tg': '@ivan'}
    // res = await fetch('http://158.160.30.88:5000/get_trips?tg_tag=@ivan')
    // res = await res.json();
    res=[{1:1,'trip_name':'trip1'},{2:2,'trip_name':'trip2'},{3:3,'trip_name':'trip3'}]
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
const nameElement = document.createElement('button');
nameElement.id=trip['trip_name']+'button';
nameElement.textContent = `${trip['trip_name']}`;  
nameElement.classList.add('name_of_user');
card.appendChild(nameElement);
/* <div class="main_popup none_for_popup" id="papa_popup">
      <div class="popup_body">
        <div class="popup_name">
          <p>Куда добавить мероприятие</p>
        </div>
        <div class="popup_content" id="all_popup_content">
          <button id="Button_for_save" class="general_button" style="font-size: 2vh; height: 5vh; margin-top: 5vh;" onclick="add_single_event()">
            Добавить как отдельное мероприятие
          </button>
          <div class="block_trips">

          </div>
        </div>
      </div>
    </div> */
    const papa_popup_element=document.createElement("div");
    const popup_content_element=document.createElement("div");
    papa_popup_element.appendChild(popup_content_element);
    const popup_content_text=document.createElement("p");
    popup_content_text.textContent = `Поездка ${trip['trip_name']}`;  
    popup_content_element.appendChild(popup_content_text);
    const close_button=document.createElement("button");
    close_button.textContent = `Закрыть`;
    close_button.classList.add('close_pay_button');

    papa_popup_element.appendChild(close_button);
    const buttton_info = document.createElement('button');
    buttton_info.textContent = `Инфо`;
    const del_trip_button = document.createElement('button')
    del_trip_button.textContent = `Удалить`;
    del_trip_button.style.display="block";
    buttton_info.style.display="block";
    del_trip_button.style.textAlign="center";
    buttton_info.style.textAlign="center";
    del_trip_button.classList.add('pay_button_new');
    buttton_info.classList.add('pay_button_new');
    papa_popup_element.appendChild(del_trip_button);
    papa_popup_element.appendChild(buttton_info);
    card.appendChild(papa_popup_element);
    papa_popup_element.id=trip['trip_name'];
    papa_popup_element.style.display="none";
    nameElement.addEventListener('click', () => {
        const targetCard = document.getElementById(trip['trip_name']);
        targetCard.style.display = 'block';
        
    });
    close_button.addEventListener('click', () => {
        const targetCard = document.getElementById(trip['trip_name']);
        targetCard.style.display = 'none';
        
    });
    del_trip_button.addEventListener('click', () => {
        const targetCard = document.getElementById(trip['trip_name']+'button');
        const targetCard2 = document.getElementById(trip['trip_name']);
        targetCard.style.display = 'none';
        targetCard2.style.display = 'none';
        //fetch('http://158.160.30.88:5000/remove_trip?lender_tg=' + lender.lenders_tg + '&debtor_tg=' + '@' +'data["user"]["username"]', {method: 'DELETE'});
        
    });




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


$(document).ready(function() {
  $('.header_burger').click(function(event) {
      $(this).toggleClass('active');
      $('.header_menu').toggleClass('active');
      $('body').toggleClass('lock');
  });
});