// let select_field = document.getElementById("id_commodity");
// select_field.setAttribute("onchange", "dynamic_form()")


function make_vis(element) {
    if (element.classList.contains('select-hid')) {
        element.classList.remove('select-hid');
        element.classList.add('select-vis');
    }
    // console.log(element.className);

}

function make_invis(element) {
    if (element.classList.contains('select-vis')) {
        element.classList.remove('select-vis');
        element.classList.add('select-hid');
    }
}


function make_invis_all(in_element) {
    let divs = document.querySelectorAll("div .select-div");
    console.log(divs);
    for (let i = 0; i < divs.length; i++) {
        make_invis(divs[i]);
        // console.log(divs[i].className);
    }
}


function commodity_change() {
    let selected_value = document.getElementById('id_commodity').value;
    console.log(selected_value);
    if (selected_value === 'empty') {
        make_invis_all();
    } else if (selected_value === 'gas') {
        make_invis_all();
        let select_div = document.getElementById('exchange_gas-div-id');
        console.log(select_div.className);
        make_vis(select_div);
    } else if (selected_value === 'electricity_spot') {
        make_invis_all();
        let select_div = document.getElementById('exchange_ee_spot-div-id');
        console.log(select_div.className);
        make_vis(select_div);
    } else if (selected_value === 'electricity_futures') {
        make_invis_all();
        let select_div = document.getElementById('exchange_ee_futures-div-id');
        console.log(select_div.className);
        make_vis(select_div);
    } else if (selected_value === 'co2') {
        make_invis_all();
        let select_div = document.getElementById('exchange_co2-div-id');
        console.log(select_div.className);
        make_vis(select_div);
    }
    //
    // switch (selected_value) {
    //     case 'empty':
    //         make_invis_all();
    //     case 'gas':
    //         make_invis_all();
    //         let select_div = document.getElementById('exchange_gas-div-id');
    //         console.log(select_div.className);
    //         make_vis(select_div);
    // default:
    // make_invis_all();
    // }
}
