// let select_field = document.getElementById("id_commodity");
// select_field.setAttribute("onchange", "dynamic_form()")


function make_vis(element) {
    if (element.classList.contains('select-hid')) {
        element.classList.remove('select-hid');
        element.classList.add('select-vis');
    }
}

function make_invis(element) {
    if (element.classList.contains('select-vis')) {
        element.classList.remove('select-vis');
        element.classList.add('select-hid');
    }
}


function make_invis_all(in_element = '') {
    let selector = ".select-div";
    if (in_element !== '') {
        selector = "." + in_element;
    }
    let divs = document.querySelectorAll(selector);
    // console.log(selector);
    // console.log(divs);
    for (let i = 0; i < divs.length; i++) {
        make_invis(divs[i]);
        // console.log(divs[i].className);
    }
}

function enable_button() {
    const btn = document.getElementById('submit-btn');
    btn.removeAttribute('disabled');
}

function disable_button() {
    const btn = document.getElementById('submit-btn');
    btn.setAttribute('disabled', '');
}

// TODO: make function to listen to changes in zone field;

function commodity_change() {
    let selected_value = document.getElementById('id_commodity').value;
    console.log(selected_value);
    if (selected_value === 'empty') {
        make_invis_all();
        clear_fields('source');
        clear_fields('zone');
    } else if (selected_value === 'gas') {
        make_invis_all();
        let select_div = document.getElementById('exchange_gas-div-id');
        // console.log(select_div.className);
        make_vis(select_div);
        clear_fields('source');
        clear_fields('zone');
    } else if (selected_value === 'electricity_spot') {
        make_invis_all();
        let select_div = document.getElementById('exchange_ee_spot-div-id');
        // console.log(select_div.className);
        make_vis(select_div);
        clear_fields('source');
        clear_fields('zone');
    } else if (selected_value === 'electricity_futures') {
        make_invis_all();
        let select_div = document.getElementById('exchange_ee_futures-div-id');
        // console.log(select_div.className);
        make_vis(select_div);
        clear_fields('source');
        clear_fields('zone');
    } else if (selected_value === 'co2') {
        make_invis_all();
        let select_div = document.getElementById('exchange_co2-div-id');
        // console.log(select_div.className);
        make_vis(select_div);
        clear_fields('source');
        clear_fields('zone');
    }
    button_change();
}

function gas_source_change() {
    let selected_value = document.getElementById('id_exchange_gas').value;
    console.log(selected_value);
    if (selected_value === 'empty') {
        make_invis_all('select-zone');
        clear_fields('zone');
    } else if (selected_value === 'icis') {
        make_invis_all('select-zone');
        let select_div = document.getElementById('zone_icis_gas-div-id');
        // console.log(select_div.className);
        make_vis(select_div);
    } else if (selected_value === 'eex') {
        make_invis_all('select-zone');
        let select_div = document.getElementById('zone_eex_gas-div-id');
        // console.log(select_div.className);
        make_vis(select_div);
    }
    button_change();
}

function ee_spot_source_change() {
    let selected_value = document.getElementById('id_exchange_ee_spot').value;
    console.log("SELECTED " + selected_value);
    if (selected_value === 'empty') {
        make_invis_all('select-zone');
        clear_fields('zone');
    } else if (selected_value === 'spot') {
        make_invis_all('select-zone');
        let select_div = document.getElementById('zone_ee_spot-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    }
    button_change();
}

function ee_futures_source_change() {
    let selected_value = document.getElementById('id_exchange_ee_futures').value;
    console.log("SELECTED " + selected_value);
    if (selected_value === 'empty') {
        make_invis_all('select-zone');
        clear_fields('zone');
    } else if (selected_value === 'tge') {
        make_invis_all('select-zone');
        let select_div = document.getElementById('zone_ee_futures_tge-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    } else if (selected_value === 'eex') {
        make_invis_all('select-zone');
        let select_div = document.getElementById('zone_ee_futures_eex-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    }
    button_change();
}

function co2_source_change() {
    let selected_value = document.getElementById('id_exchange_co2').value;
    console.log("SELECTED " + selected_value);
    if (selected_value === 'empty') {
        make_invis_all('select-zone');
        clear_fields('zone');
    } else if (selected_value === 'eex') {
        make_invis_all('select-zone');
        let select_div = document.getElementById('zone_co2-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    }
    button_change();
}

function clear_fields(field_level) {
    let zones;
    if (field_level === 'source') {
        zones = document.querySelectorAll('.select-exchange select');
        console.log(zones);
    } else if (field_level === 'zone') {
        zones = document.querySelectorAll('.select-zone select');
    }
    zones.forEach(element => element.value = 'empty');
}

function button_change() {
    let zone = document.querySelectorAll('.select-zone select');
    for (let i = 0; i < zone.length; i++) {
        if (zone[i].value !== 'empty') {
            enable_button()
            return 0;
        }
    }
    disable_button();
    return 1;
}

