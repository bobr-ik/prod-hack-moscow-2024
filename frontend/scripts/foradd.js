var main_dictionary = new Map();
var debtors = new Array();
var general_summ = 0;
var persons_normal = 2;

function get_info(value) {
    switch (value) {
        case 1:
            const ivent_name = document.getElementById('event').value
            break;

        case 2:
            general_summ = document.getElementById('summ').value
            break;

        case 3:
            const name_who_pay = document.getElementById('person_who_pay').value

            main_dictionary.set(name_who_pay, general_summ);
            break;

        case 4:
            const person_name = document.getElementById('new_person_name').value
            const person_summ = document.getElementById('new_person_summ').value
            document.getElementById("new_person_summ").classList.toggle("style_person_summ");
            document.getElementById("new_person_summ").classList.toggle("style_person_summ_check");

            general_summ = general_summ - person_summ;  
            var were_values = document.getElementsByClassName("style_person_summ");
            for (let i = 0; i < were_values.length; i++) { 
                were_values[i].value = general_summ / persons_normal;
            }   

            document.getElementById('new_person_name').id = "new_person_name_done";
            document.getElementById('new_person_summ').id = "new_person_summ_done";
    }
}

function add_person() {
    if (document.getElementById("new_person_summ") != null) {
        persons_normal += 1;
        let moment_summ = general_summ / persons_normal;

        document.getElementById('new_person_name').id = "new_person_name_done";
        document.getElementById('new_person_summ').id = "new_person_summ_done";

        var were_values = document.getElementsByClassName("style_person_summ");
        for (let i = 0; i < were_values.length; i++) { 
            were_values[i].value = moment_summ;
        }
    } 
    const person_block = document.createElement('div');
    person_block.classList.add("style_person_block");
    document.getElementById("add_person").appendChild(person_block);

    const person_name = document.createElement('input');
    person_name.classList.add("style_person_name");
    person_name.id = "new_person_name";
    person_name.setAttribute('value', '@');
    person_block.appendChild(person_name);

    const person_summ = document.createElement('input');
    person_summ.classList.add("style_person_summ");
    person_summ.classList.add("send");
    person_summ.id = "new_person_summ";
    let moment_summ = general_summ / persons_normal;
    person_summ.onchange = () => get_info(4);
    person_summ.setAttribute("placeholder", moment_summ);
    person_block.appendChild(person_summ); 

    if (document.getElementById("send_list_button") == null) {
        const send_list = document.createElement('button');
        send_list.classList.add("send_button");
        send_list.innerHTML = "Добавить мероприятие";
        send_list.id = "send_list_button";
        send_list.onclick = send_event;
        document.body.appendChild(send_list);
    }
}

function send_event() {
    var persons_name = document.getElementsByClassName("style_person_name");
    var persons_summ = document.getElementsByClassName("send");
    for (let i = 0; i < persons_name.length; i++) {
        var person = new Map();
        person.set(persons_name[i].value, persons_summ[i].value);
        debtors.push(person);
    }

    main_dictionary.set("debtors_tg_list", debtors);
    main_dictionary.set("event_name", document.getElementById("event").value);

    console.log(main_dictionary);
}

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