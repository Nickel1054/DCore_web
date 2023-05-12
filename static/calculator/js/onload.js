let date_field1 = document.getElementById('id_period_date_field_1');
let date_field2 = document.getElementById('id_period_date_field_1');

// date_field1.onload = function () {
// date_field1.classList.add("form-control");
// }
// date_field2.onload = function () {
// date_field2.classList.add("form-control");
// }

date_field1.setAttribute('min', '2018-01-01');
date_field1.setAttribute('max', '2025-12-31');