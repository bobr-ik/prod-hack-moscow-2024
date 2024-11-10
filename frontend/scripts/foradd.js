var main_dictionary = new Map();
var debtors = new Array();
var general_summ = 0;
var save_general_summ = 0;
var flag = 0;
var main_person_name = 0;
var main_person_summ = 0;

function get_info(value) {
    switch (value) {
        case 1:
            const ivent_name = document.getElementById('event').value;
            break;

        case 2:
            general_summ = document.getElementById('summ').value;
            save_general_summ = general_summ;
            break;

        case 3:
            main_person_name = document.getElementById('name_person_who_pay').value;
            break;

        case 4:
            const new_person_name = document.getElementsByClassName('style_person_name')[
                document.getElementsByClassName('style_person_name').length - 1].value;
            break
    }
}

var singles;

function get_summ() {
    var persons = document.getElementsByClassName('check');
    singles = 0;
    general_summ = save_general_summ;
    for (i = 0; i < persons.length; i++) {
        if (persons[i].value) {
            general_summ -= persons[i].value;

            if (general_summ <= 0) {
                alert("Сумма чека равна 0");
                flag = 1;
            }

            if (singles > 1) {
                singles -= 1;
            }
        } else {
            singles += 1;
        }
    }
}

function add_person() {
    get_summ(); //Обновляем сумму
    if (flag != 1) {
        const person_block = document.createElement('div');
        person_block.classList.add("style_person_block");
        document.getElementById("add_person").appendChild(person_block);

        const person_name = document.createElement('input');
        person_name.classList.add("style_person_name");
        person_name.setAttribute('value', '@');
        person_name.onchange = () => get_info(4);
        person_block.appendChild(person_name);

        const person_summ = document.createElement('input');
        person_summ.classList.add("style_person_summ");
        person_summ.classList.add("check");
        person_summ.setAttribute('placeholder', (general_summ / (singles + 1)).toFixed(2));
        person_block.appendChild(person_summ); 

        var array = document.getElementsByClassName('check');
        for (i = 0; i < array.length; i++) {
            array[i].setAttribute("placeholder", (general_summ / (singles + 1)).toFixed(2));
        }

        if (document.getElementById("send_list_button") == null) {
            const check_list = document.createElement('button');
            check_list.classList.add("general_button");
            check_list.innerHTML = "Подтвердить";
            check_list.style = "width: 95%";
            check_list.id = "check_list_button";
            check_list.onclick = update_event;
            document.body.appendChild(check_list);
        }

        if (document.getElementById("send_list_button") == null) {
            const send_list = document.createElement('button');
            send_list.classList.add("send_button");
            send_list.innerHTML = "Добавить мероприятие";
            send_list.id = "send_list_button";
            send_list.onclick = send_event;
            document.body.appendChild(send_list);
        }
    }
}

function update_event() {
    var array = document.getElementsByClassName('check');
    for (i = 0; i < array.length; i++) {
        if (array[i].value == "") {
            array[i].value = (general_summ / (singles + 1)).toFixed(2);
        }
    }
}

function send_event() {
    var persons_name = document.getElementsByClassName('style_person_name');
    var persons_summ = document.getElementsByClassName('style_person_summ');

    for (i = 0; i < persons_name.length; i++) {
        var person = new Map();
        person.set(persons_name[i].value, persons_summ[i].value);

        debtors.push(person);
    }
    
    main_dictionary.set("lender_tg", document.getElementById('name_person_who_pay').value);
    main_dictionary.set("debtors_tg_list", debtors);
    main_dictionary.set("event", document.getElementById('event').value);
    console.log(main_dictionary);

    document.getElementById('papa_popup').classList.toggle("none_for_popup");
}

function add_single_event() {
    var new_content = document.getElementById("all_popup_content")
    new_content.innerHTML = "Успешно";
    new_content.classList.add("content_after_save");

    const dobri_galochka = document.createElement('div');
    dobri_galochka.classList.add('galochka');
    new_content.appendChild(dobri_galochka);
}

$(document).ready(function() {
    $('.header_burger').click(function(event) {
        $(this).toggleClass('active');
        $('.header_menu').toggleClass('active');
        $('body').toggleClass('lock');
    });
});

// function add_payment() {
//     document.getElementById("button_who_pay").remove();

//     const person_pay = document.createElement('input');
//     person_pay.id = "input_person_who_pay";
//     person_pay.classList.add("input_class");
//     person_pay.setAttribute("value", "@");
//     person_pay.onchange = () => get_info(3);
//     document.getElementById("who_pay").appendChild(person_pay);

//     const cansel_add = document.createElement('button');
//     cansel_add.classList.add("cancel_button");
//     cansel_add.id = "cancel_add";
//     cansel_add.onclick = () => remove_changes("input_person_who_pay", "replace_button", "button_who_pay", "who_pay", "Добавить оплатившего", "add_payment()");
//     document.getElementById("who_pay").appendChild(cansel_add);
// }

// function remove_changes(remove_id, return_elem, elem_id, parent_id, text, func) {
//     document.getElementById(remove_id).remove();
//     document.getElementById("cancel_add").remove();
    
//     const was_elem = document.createElement("button");
//     was_elem.classList.add(return_elem);
//     was_elem.innerHTML = text;
//     was_elem.id = elem_id;
//     was_elem.setAttribute("onclick", func);
//     document.getElementById(parent_id).appendChild(was_elem);
// }
fetch(`https://158.160.85.97:5000/insert_debt?lender_tg=${JSON.stringify(main_dictionary['lender_tg'])}&debtors_tg_debpt_dict=${JSON.stringify(main_dictionary['debtors_tg_list'])}&event_name=${JSON.stringify(main_dictionary['event'])}`, {method: 'POST'})