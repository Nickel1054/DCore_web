// let select_field = document.getElementById("id_commodity");
// select_field.setAttribute("onchange", "dynamic_form()")


// date_field1.classList.add("form-control");
// date_field2.classList.add("form-control");

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

function clear_fields_all() {
    let selects = document.querySelectorAll(".select-hid select");
    selects.forEach(element => element.value = 'empty')
    let spans_titles = document.querySelectorAll('div.select-hid .select2-selection__rendered');
    spans_titles.forEach(element => {
        element.textContent = '--';
        element.title = '--';
    })
}

function commodity_change() {
    let selected_value = document.getElementById('id_commodity').value;
    // console.log(selected_value);
    if (selected_value === 'empty') {
        make_invis_all();
        clear_fields_all();
    } else if (selected_value === 'gas') {
        make_invis_all();
        let select_divs = document.querySelectorAll('[id^="exchange_gas"]');
        // let select_div = document.getElementById('exchange_gas-div-id');
        for (let i = 0; i < select_divs.length; i++) {
            // console.log(select_divs[i].className);
            make_vis(select_divs[i]);
            clear_fields_all();
        }

    } else if (selected_value === 'electricity_spot') {
        make_invis_all();
        let select_divs = document.querySelectorAll('[id^="exchange_ee_spot"]');
        // let select_div = document.getElementById('exchange_gas-div-id');
        for (let i = 0; i < select_divs.length; i++) {
            // console.log(select_divs[i].className);
            make_vis(select_divs[i]);
            clear_fields_all();
        }
    } else if (selected_value === 'electricity_futures') {
        make_invis_all();
        let select_divs = document.querySelectorAll('[id^="exchange_ee_futures"]');
        // let select_div = document.getElementById('exchange_gas-div-id');
        for (let i = 0; i < select_divs.length; i++) {
            // console.log(select_divs[i].className);
            make_vis(select_divs[i]);
            clear_fields_all();
        }
    } else if (selected_value === 'co2') {
        make_invis_all();
        let select_divs = document.querySelectorAll('[id^="exchange_co2"]');
        // let select_div = document.getElementById('exchange_gas-div-id');
        for (let i = 0; i < select_divs.length; i++) {
            // console.log(select_divs[i].className);
            make_vis(select_divs[i]);
            clear_fields_all();
        }
    }
    button_change();
}

function gas_source_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    let selected_value = document.getElementById(element_id).value;
    // console.log(selected_value);
    if (selected_value === 'empty') {
        make_invis_all('select-zone select-column-' + column_number);
        clear_fields_all();
    } else if (selected_value === 'icis') {
        clear_fields_all();
        make_invis_all('select-zone select-column-' + column_number);
        // console.log('zone_icis_gas_' + column_number + '-div-id');
        let select_div = document.getElementById('zone_icis_gas_' + column_number + '-div-id');
        // console.log(select_div);
        make_vis(select_div);
    } else if (selected_value === 'eex') {
        clear_fields_all();
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
        clear_fields_all();
    } else if (selected_value === 'spot') {
        clear_fields_all();
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
        clear_fields_all();
    } else if (selected_value === 'tge') {
        clear_fields_all();
        make_invis_all('select-zone select-column-' + column_number);
        let select_div = document.getElementById('zone_ee_futures_tge_' + column_number + '-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    } else if (selected_value === 'eex') {
        clear_fields_all();
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
        clear_fields_all();
    } else if (selected_value === 'eex') {
        make_invis_all('select-zone select-column-' + column_number);
        let select_div = document.getElementById('zone_co2_' + column_number + '-div-id');
        // console.log("CLASS" + select_div.className);
        make_vis(select_div);
    }
    button_change();
}


// function clear_fields_all(field_level, column) {
//     let zones;
//     if (field_level === 'source') {
//         zones = document.querySelectorAll('.select-exchange select');
//         // console.log(zones);
//     } else if (field_level === 'zone') {
//         zones = document.querySelectorAll('.select-zone.select-column-' + column + ' select');
//     } else {
//
//         zones = document.querySelectorAll('.select2-hidden-accessible select');
//         // zones = document.querySelectorAll('.select-' + field_level + '.select-column-' + column + ' select');
//     }
//     // console.log('ZONES TO CLEAR:');
//     console.log(zones);
//     zones.forEach(element => element.value = 'empty');
// }

function zone_change(element_id) {
    let zone = document.getElementById(element_id).value
    let column_number = element_id.split('_').at(-1);
    // console.log(column_number);
    let commodity = document.getElementById('id_commodity').value;
    let source = document.querySelector('.select-exchange.select-vis.select-column-' + column_number + ' select').value;
    clear_fields_all();
    // console.log('zone changed');
    if (['electricity_futures'].indexOf(commodity) >= 0) {
        // console.log('ee');
        let loads = document.getElementById('load_type_' + column_number + '-div-id');
        make_invis_all('select-load select-column-' + column_number);

        if (zone !== 'empty') {
            make_invis_all('select-load select-column-' + column_number);
            make_vis(loads);
        }
    }
    // console.log('passed');
    if (zone === 'empty') {
        // console.log('empty');
        make_invis_all('select-product select-column-' + column_number);
        clear_fields_all();
    } else {
        make_invis_all('select-product select-column-' + column_number);
        let select_div;
        if (commodity === 'co2') {
            select_div = document.getElementById('product_types_co2_' + column_number + '-div-id');
        } else {
            select_div = document.getElementById('product_types_' + source + '_' + column_number + '-div-id');
        }
        // console.log('product_types_' + source + '_' + column_number + '-div-id');
        make_vis(select_div);

    }
    button_change()
}

function product_change(element_id) {
    let product_dict = {
        'day': ['period_deliverystart_', "period_deliveryend_"],
        'day_eex': 'period_deliverystart_',
        'da': ['period_deliverystart_', "period_deliveryend_"],
        'week': 'period_week_',
        'weekend': 'period_weekend_',
        'month': 'period_month_',
        'quarter': 'period_quarter_',
        'season': 'period_season_',
        'year': 'period_year_',
        'gas_year': 'period_gas_year_',
    };
    let product = document.getElementById(element_id).value;
    let column_number = element_id.split('_').at(-1);
    let source = document.querySelector('.select-vis.select-exchange.select-column-' + column_number + ' select').value
    // console.log('PRODUCT: ' + product);
    clear_fields_all()
    make_invis_all('select-period select-column-' + column_number);
    if (product !== 'empty') {
        if (product === 'day' || product === 'da') {
            if (source === 'eex') {
                let select_div = document.getElementById(product_dict['day_eex'] + column_number + '-div-id');
                // console.log(element + column_number + '-div-id');
                make_vis(select_div);
            } else {
                for (let element of product_dict[product]) {
                    let select_div = document.getElementById(element + column_number + '-div-id');
                    // console.log(element + column_number + '-div-id');
                    make_vis(select_div);
                }
            }
        } else {
            let select_div = document.getElementById(product_dict[product] + column_number + '-div-id');
            // console.log(product_dict[product] + column_number + '-div-id');
            make_vis(select_div);
        }
    }
    let delivery_year = document.getElementById('year_' + column_number + '-div-id');
    make_invis(delivery_year);
    clear_fields_all();
    button_change()
}

function delivery_period_change(element_id) {
    let delivery_period = document.getElementById(element_id).value;
    let column_number = element_id.split('_').at(-1);
    let product_type = document.querySelector('.select-product.select-vis.select-column-' + column_number + ' select').value;
    // console.log(delivery_period);
    // console.log(product_type);
    clear_fields_all()
    // make_invis_all('select-period select-column-' + column_number);
    make_invis_all('select-year select-column-' + column_number);

    let del_start = document.getElementById('period_deliverystart_' + column_number + '-div-id');
    let del_end = document.getElementById('period_deliveryend_' + column_number + '-div-id');
    make_invis(del_start);
    make_invis(del_end);

    let year_field = document.getElementById('year_' + column_number + '-div-id');
    if (['week', 'weekend', 'month', 'quarter', 'season',].includes(product_type) && delivery_period !== 'empty') {
        make_vis(year_field);
    } else {
        make_invis(year_field);
        clear_fields_all();
    }
    button_change();


    // if (delivery_period !== 'empty' && delivery_period !== '') {
    //
    //     let select_div = document.getElementById(product_dict[product] + column_number + '-div-id');
    //     // console.log(product_dict[product] + column_number + '-div-id');
    //     make_vis(select_div);
    // } else {
    //     clear_fields_all()
    //     make_invis_all('select-year select-column-' + column_number);
}

function button_change() {
    let form_filled_1 = {};
    let form_filled_2 = {};
    let form_values = $('#calculator-form').serializeArray();
    for (let element of form_values) {
        if (element.value !== '' && element.value !== 'empty') {
            if (element.name === 'commodity') {
                form_filled_1[element.name] = element.value;
                form_filled_2[element.name] = element.value;
            } else if (element.name.includes('period_delivery')) {
                if (element.name.split('_')[element.name.split('_').length - 1] === '1') {
                    form_filled_1[element.name.split('_')[1]] = element.value;
                } else if (element.name.split('_')[element.name.split('_').length - 1] === '2') {
                    form_filled_2[element.name.split('_')[1]] = element.value;
                }
            } else {
                if (element.name.split('_')[element.name.split('_').length - 1] === '1') {
                    form_filled_1[element.name.split('_')[0]] = element.value;
                } else if (element.name.split('_')[element.name.split('_').length - 1] === '2') {
                    form_filled_2[element.name.split('_')[0]] = element.value;
                }
            }
        }
    }

    // console.log('1:');
    console.log(form_filled_1);
    // console.log(Object.keys(form_filled_1).length);
    // console.log('2:');
    // console.log(form_filled_2);
    // console.log(Object.keys(form_filled_1).length);
    // console.log('\n');

    let count = 0;
    for (let dict of [form_filled_1, form_filled_2]) {
        if (dict['commodity'] === 'gas') {
            if (['week', 'weekend', 'month', 'quarter', 'season'].includes(dict['product'])) {
                if (Object.keys(dict).length === 6) {
                    count++;
                }
            } else if (['day'].includes(dict['product'])) {
                if (dict['exchange'] === 'eex') {
                    if (Object.keys(dict).length === 5) {
                        count++;
                    }
                } else {
                    if (Object.keys(dict).length === 6) {
                        count++;
                    }
                }
            } else if (['year', 'gas_year'].includes(dict['product'])) {
                if (Object.keys(dict).length === 5) {
                    count++;
                }
            }
        } else if (dict['commodity'] === 'electricity_spot') {
            if (Object.keys(dict).length === 6) {
                count++;
            }
        } else if (dict['commodity'] === 'electricity_futures') {
            if (['week', 'weekend', 'month', 'quarter', 'season'].includes(dict['product'])) {
                if (Object.keys(dict).length === 7) {
                    count++;
                }
            } else if (['day'].includes(dict['product'])) {
                if (dict['exchange'] === 'eex') {
                    if (Object.keys(dict).length === 6) {
                        count++;
                    }
                }
            } else if (['year'].includes(dict['product'])) {
                if (Object.keys(dict).length === 6) {
                    count++;
                }
            }
        } else if (dict['commodity'] === 'co2') {
            if (Object.keys(dict).length === 6) {
                count++;
            }
        }
    }
    console.log('COUNT');
    console.log(count);
    if (count === 2) {
        enable_button()
    } else {
        disable_button();
    }
}

function check_dates(element_id) {
    let column_number = element_id.split('_').at(-1);
    let field = document.getElementById(element_id);
    let delivery_start = document.getElementById('id_period_deliverystart_' + column_number);
    let delivery_end = document.getElementById('id_period_deliveryend_' + column_number);

    delivery_start.setAttribute('min', '2018-01-01');
    delivery_end.setAttribute('min', '2018-01-01');
    delivery_start.setAttribute('max', '2025-12-31');
    delivery_end.setAttribute('max', '2025-12-31');
    // console.log('COLUMN ' + column_number.toString());
    if (field.value !== '') {
        if (element_id.includes('deliverystart')) {
            delivery_end.setAttribute('min', field.value);
        } else if (element_id.includes('deliveryend')) {
            delivery_start.setAttribute('max', field.value);
        }
    }
}
