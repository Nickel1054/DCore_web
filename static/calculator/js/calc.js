// let select_field = document.getElementById("id_commodity");
// select_field.setAttribute("onchange", "dynamic_form()")


function dynamic_form() {
    let select = document.getElementById("id_commodity");
    let form = document.getElementById("calulator-form");
    let value = select.value;
    console.log(value);

    if (value === 'gas'){
        let label_form = document.createElement("label");
        label_form.textContent='Hub';
        label_form.setAttribute("for", "form-gas");


        let div_form = document.createElement("select");
        div_form.setAttribute("class", "form-group");
        div_form.setAttribute("id", "form-gas");
        div_form.setAttribute("value", "Hub");
        form.appendChild(div_form);
    }
}
