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
    let label_element = document.querySelector(div_selector + ' label');
    jQuery(label_element).detach().appendTo(dest_tr + ' td.label-1');

    // console.log(label_element);
    let div_element = document.querySelector(div_selector);
    jQuery(div_element).detach().appendTo(dest_tr + ' td.column-1');
}
// TODO create (or adapt) function for moving td`s from hidden table to form table.

move_element('#commodity-div-id', '#commodity-tr');
