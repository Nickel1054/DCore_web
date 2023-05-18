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

for (let field of [date_start_field1, date_start_field2, date_end_field1, date_end_field2]) {
    field.setAttribute('min', '2018-01-01');
    field.setAttribute('max', '2025-12-31');
}
