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
        in_element = in_element.replace(' ', '.');
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

function commodity_change() {
    let selected_value = document.getElementById('id_commodity').value;
    console.log(selected_value);
    if (selected_value === 'empty') {
        make_invis_all();
        clear_fields('source');
        clear_fields('zone');
    } else if (selected_value === 'gas') {
        make_invis_all();
        let select_divs = document.querySelectorAll('[id^="exchange_gas"]');
        // let select_div = document.getElementById('exchange_gas-div-id');
        for (let i = 0; i < select_divs.length; i++) {
            console.log(select_divs[i].className);
            make_vis(select_divs[i]);
            clear_fields('source');
            clear_fields('zone');
        }

    } else if (selected_value === 'electricity_spot') {
        make_invis_all();
        let select_divs = document.querySelectorAll('[id^="exchange_ee_spot"]');
        // let select_div = document.getElementById('exchange_gas-div-id');
        for (let i = 0; i < select_divs.length; i++) {
            console.log(select_divs[i].className);
            make_vis(select_divs[i]);
            clear_fields('source');
            clear_fields('zone');
        }
    } else if (selected_value === 'electricity_futures') {
        make_invis_all();
        let select_divs = document.querySelectorAll('[id^="exchange_ee_futures"]');
        // let select_div = document.getElementById('exchange_gas-div-id');
        for (let i = 0; i < select_divs.length; i++) {
            console.log(select_divs[i].className);
            make_vis(select_divs[i]);
            clear_fields('source');
            clear_fields('zone');
        }
    } else if (selected_value === 'co2') {
        make_invis_all();
        let select_divs = document.querySelectorAll('[id^="exchange_co2"]');
        // let select_div = document.getElementById('exchange_gas-div-id');
        for (let i = 0; i < select_divs.length; i++) {
            console.log(select_divs[i].className);
            make_vis(select_divs[i]);
            clear_fields('source');
            clear_fields('zone');
        }
        button_change();
    }
}

function gas_source_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    let selected_value = document.getElementById(element_id).value;
    // console.log(selected_value);
    if (selected_value === 'empty') {
        make_invis_all('select-zone select-column-' + column_number);
        clear_fields('zone', column_number);
    } else if (selected_value === 'icis') {
        clear_fields('zone', column_number);
        make_invis_all('select-zone select-column-' + column_number);
        // console.log('zone_icis_gas_' + column_number + '-div-id');
        let select_div = document.getElementById('zone_icis_gas_' + column_number + '-div-id');
        console.log(select_div);
        make_vis(select_div);
    } else if (selected_value === 'eex') {
        clear_fields('zone', column_number);
        make_invis_all('select-zone select-column-' + column_number);
        let select_div = document.getElementById('zone_eex_gas_' + column_number + '-div-id');
        // console.log(select_div.className);
        make_vis(select_div);
    }
    button_change();
}

function ee_spot_source_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    let selected_value = document.getElementById(element_id).value;
    // console.log("SELECTED " + selected_value);
    if (selected_value === 'empty') {
        make_invis_all('select-zone select-column-' + column_number);
        clear_fields('zone', column_number);
    } else if (selected_value === 'spot') {
        clear_fields('zone', column_number);
        make_invis_all('select-zone select-column-' + column_number);
        let select_div = document.getElementById('zone_ee_spot_' + column_number + '-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    }
    button_change();
}

function ee_futures_source_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    let selected_value = document.getElementById(element_id).value;
    // console.log("SELECTED " + selected_value);
    if (selected_value === 'empty') {
        make_invis_all('select-zone select-column-' + column_number);
        clear_fields('zone', column_number);
    } else if (selected_value === 'tge') {
        clear_fields('zone', column_number);
        make_invis_all('select-zone select-column-' + column_number);
        let select_div = document.getElementById('zone_ee_futures_tge_' + column_number + '-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    } else if (selected_value === 'eex') {
        clear_fields('zone', column_number);
        make_invis_all('select-zone select-column-' + column_number);
        let select_div = document.getElementById('zone_ee_futures_eex_' + column_number + '-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    }
    button_change();
}

function co2_source_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    let selected_value = document.getElementById(element_id).value;
    // console.log("SELECTED " + selected_value);
    if (selected_value === 'empty') {
        make_invis_all('select-zone select-column-' + column_number);
        clear_fields('zone', column_number);
    } else if (selected_value === 'eex') {
        make_invis_all('select-zone select-column-' + column_number);
        let select_div = document.getElementById('zone_co2_' + column_number + '-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    }
    button_change();
}

function clear_fields(field_level, column) {
    let zones;
    if (field_level === 'source') {
        zones = document.querySelectorAll('.select-exchange select');
        // console.log(zones);
    } else if (field_level === 'zone') {
        zones = document.querySelectorAll('.select-zone.select-column-' + column + ' select');
    }
    // console.log('ZONES TO CLEAR:');
    // console.log(zones);
    zones.forEach(element => element.value = 'empty');
}

function zone_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    console.log(column_number);
    let commodity = document.getElementById('id_commodity').value;

    if (['electricity_spot', 'electricity_futures'].indexOf(commodity) >= 0) {
        make_invis_all('select-load select-column-' + column_number);
        let loads = document.getElementById('load_type_' + column_number + '-div-id');
        console.log(loads);
        make_vis(loads);
        // console.log('Electricity selected');
    }
    button_change();
}

function button_change() {
    let zone = document.querySelectorAll('.select-zone select');
    let selected_number = 0
    for (let i = 0; i < zone.length; i++) {
        if (zone[i].value !== 'empty') {
            selected_number++;
            if (selected_number >= 2) {
                // enable_button()
                return 0;
            }
        }
    }
    disable_button();
    return 1;
}

