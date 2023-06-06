let date_start_field1 = document.getElementById('id_period_deliverystart_1');
let date_start_field2 = document.getElementById('id_period_deliverystart_2');

let date_end_field1 = document.getElementById('id_period_deliveryend_1');
let date_end_field2 = document.getElementById('id_period_deliveryend_2');
// date_field1.onload = function () {
// date_field1.classList.add("form-control");
// }
// date_field2.onload = function () {
// date_field2.classList.add("form-control");
// }

// for (let field of [date_start_field1, date_start_field2, date_end_field1, date_end_field2]) {
//     field.setAttribute('min', '2018-01-01');
//     field.setAttribute('max', '2025-12-31');
// }

function move_element(div_selector, dest_tr) {
    let column = div_selector.slice(-1);

    let element = document.querySelector(div_selector);
    jQuery(element).detach().appendTo(dest_tr + ' tbody');
    element.classList.add("my-class");
}

function sort_tables() {
    let table_1 = document.getElementById('form-table-1');
    let table_2 = document.getElementById('form-table-2');

    let form_rows = document.querySelectorAll('tr.table-row-hidden');

    for (let element of form_rows) {
        jQuery(element).detach().appendTo('#form-table-' + element.id.slice(-1));
    }
}
// move_element('#exchange_gas_tr_1', '#form-table-1');
sort_tables()