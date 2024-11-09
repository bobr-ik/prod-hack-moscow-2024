function get_info(value) {
    switch (value) {
        case 1:
            const name = document.getElementById('name').value
            console.log(name);
            break;
        case 2:
            const general_summ = document.getElementById('summ').value
            console.log(general_summ);
            break;
    }
}

function add_payment() {
    document.getElementById("button_who_pay").remove();

    const person_pay = document.createElement('input');
    person_pay.id = "input_person_who_pay";
    person_pay.classList.add("input_class");
    person_pay.setAttribute("placeholder", "Кто оплатил");
    document.getElementById("who_pay").appendChild(person_pay);

    const cansel_add = document.createElement('button');
    cansel_add.classList.add("cancel_button");
    cansel_add.id = "cancel_add";
    cansel_add.onclick = () => remove_changes("input_person_who_pay", "replace_button", "button_who_pay", "who_pay", "Добавить оплатившего", "add_payment()");
    document.getElementById("who_pay").appendChild(cansel_add);
}

function remove_changes(remove_id, return_elem, elem_id, parent_id, text, func) {
    document.getElementById(remove_id).remove();
    document.getElementById("cancel_add").remove();
    
    const was_elem = document.createElement("button");
    was_elem.classList.add(return_elem);
    was_elem.innerHTML = text;
    was_elem.id = elem_id;
    was_elem.setAttribute("onclick", func);
    document.getElementById(parent_id).appendChild(was_elem);
}