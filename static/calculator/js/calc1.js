// let select_field = document.getElementById("id_commodity");
// select_field.setAttribute("onchange", "dynamic_form()")


// date_field1.classList.add("form-control");
// date_field2.classList.add("form-control");

function move_element_to_table(element, dest_tr) {
    let column_num = element.id.split('-')[0].slice(-1);

    let label_element = document.querySelector('#' + element.id + ' label');
    // console.log(dest_tr + ' td.label-' + column_num);
    jQuery(label_element).detach().appendTo('#' + dest_tr + '-tr' + ' td.label-' + column_num);

    // console.log(label_element);
    let div_element = document.querySelector('#' + element.id);
    jQuery(div_element).detach().appendTo('#' + dest_tr + '-tr' + ' td.column-' + column_num);

    document.querySelectorAll('#calculator-form table span.select2-container--default')[0].setAttribute('style', 'width: 100%')
}

function move_element_from_table(element) {
    let column_num = element.id.split('-')[0].slice(-1);

    let label_element = document.querySelector('#' + element.id + ' label');
    // console.log(dest_tr + ' td.label-' + column_num);
    jQuery(label_element).detach().appendTo('#' + dest_tr + '-tr' + ' td.label-' + column_num);

    // console.log(label_element);
    let div_element = document.querySelector('#' + element.id);
    jQuery(div_element).detach().appendTo('#' + dest_tr + '-tr' + ' td.column-' + column_num);

    document.querySelectorAll('#calculator-form table span.select2-container--default')[0].setAttribute('style', 'width: 100%')
}


function make_vis(element) {
    if (element.classList.contains('table-row-hidden')) {
        element.classList.remove('table-row-hidden');
        element.classList.add('table-row-visible');
    }
}

function make_invis(element) {
    if (element.classList.contains('table-row-visible')) {
        element.classList.remove('table-row-visible');
        element.classList.add('table-row-hidden');
    }
}

function make_invis_all(in_element = '') {
    let selector;
    if (in_element !== '') {
        // in_element = in_element.replace(' ', '.');
        selector = in_element;
    } else {
        selector = 'table.table-form tr.table-row-visible';
    }
    let rows = document.querySelectorAll(selector);

    for (let r of rows) {
        make_invis(r);
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

function clear_fields_all(selector_like = '') {
    let selects;
    if (selector_like !== '') {
        selects = document.querySelectorAll(selector_like);
    } else if (selector_like.startsWith('$')) {
        selects = selector_like;
    } else {
        selects = document.querySelectorAll("tr.table-row-hidden select");
    }
    selects.forEach(element => element.value = 'empty')
    let spans_titles = document.querySelectorAll('tr.table-row-hidden .select2-selection__rendered');
    spans_titles.forEach(element => {
        element.textContent = '--';
        element.title = '--';
    })
}

function equalize_table() {
    document.querySelectorAll('.table-row-empty').forEach(element => element.remove());

    let length_1 = document.querySelectorAll('#form-table-1 tr.table-row-visible').length
    let length_2 = document.querySelectorAll('#form-table-2 tr.table-row-visible').length

    if (length_1 !== length_2) {
        let increase_tr_table;
        if (length_1 > length_2) {
            increase_tr_table = '2'
        } else {
            increase_tr_table = '1'
        }
        console.log(increase_tr_table);
        let tr = document.createElement('tr');
        tr.classList.add('table-row-visible', 'table-row-empty')

        document.getElementById('form-table-' + increase_tr_table).appendChild(tr);
    //     TODO write deletion function for 'table-row-empty'
    }
}

function commodity_change() {
    let selected_value = document.getElementById('id_commodity').value;
    make_invis_all();

    // console.log(selected_value);
    if (selected_value === 'empty') {
        clear_fields_all();
    } else {
        let select_divs = null;
        switch (selected_value) {
            case 'gas':
                select_divs = document.querySelectorAll('[id^="exchange_gas_tr"]');
                break;
            case 'electricity_spot':
                select_divs = document.querySelectorAll('[id^="exchange_ee_spot"]');
                break;
            case 'electricity_futures':
                select_divs = document.querySelectorAll('[id^="exchange_ee_futures"]');
                break;
            case 'co2':
                select_divs = document.querySelectorAll('[id^="exchange_co2"]');
                break;
        }
        for (let i = 0; i < select_divs.length; i++) {
            make_vis(select_divs[i]);
            clear_fields_all();
        }
    }
    button_change();
}

function gas_source_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    let selected_value = document.getElementById(element_id).value;
    make_invis_all('.row-zone.tr-column-' + column_number);
    if (selected_value === 'empty') {
        clear_fields_all();
    } else {
        if (selected_value === 'icis') {
            clear_fields_all('.row-zone.tr-column-' + column_number);
            make_invis_all('.row-zone.tr-column-' + column_number);

            let select_div = document.getElementById('zone_icis_gas_tr_' + column_number);
            make_vis(select_div);

        } else if (selected_value === 'eex') {
            clear_fields_all('.row-zone.tr-column-' + column_number);
            make_invis_all('.row-zone.tr-column-' + column_number);

            let select_div = document.getElementById('zone_eex_gas_tr_' + column_number);
            make_vis(select_div);
        }
        button_change();
    }
}

function ee_spot_source_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    let selected_value = document.getElementById(element_id).value;
    make_invis_all('.row-zone.tr-column-' + column_number);
    if (selected_value === 'empty') {
        clear_fields_all();
    } else {
        clear_fields_all('.row-zone.tr-column-' + column_number);
        make_invis_all('.row-zone.tr-column-' + column_number);

        let select_div = document.getElementById('zone_ee_spot_tr_' + column_number);
        make_vis(select_div);
    }
    button_change();
}

function ee_futures_source_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    let selected_value = document.getElementById(element_id).value;
    make_invis_all('.row-zone.tr-column-' + column_number);
    if (selected_value === 'empty') {
        clear_fields_all();
    } else {
        if (selected_value === 'tge') {
            clear_fields_all('.row-zone.tr-column-' + column_number);
            make_invis_all('.row-zone.tr-column-' + column_number);

            let select_div = document.getElementById('zone_ee_futures_tge_tr_' + column_number);
            make_vis(select_div);

        } else if (selected_value === 'eex') {
            clear_fields_all('.row-zone.tr-column-' + column_number);
            make_invis_all('.row-zone.tr-column-' + column_number);

            let select_div = document.getElementById('zone_ee_futures_eex_tr_' + column_number);
            make_vis(select_div);
        }
        button_change();
    }
}

function co2_source_change(element_id) {
    let column_number = element_id.split('_').at(-1);
    let selected_value = document.getElementById(element_id).value;
    make_invis_all('.row-zone.tr-column-' + column_number);
    if (selected_value === 'empty') {
        clear_fields_all();
    } else {
        clear_fields_all('.row-zone.tr-column-' + column_number);
        make_invis_all('.row-zone.tr-column-' + column_number);

        let select_div = document.getElementById('zone_co2_tr_' + column_number);
        make_vis(select_div);
    }
    button_change();
}

function zone_change(element_id) {
    let zone = document.getElementById(element_id).value
    let column_number = element_id.split('_').at(-1);
    // console.log(column_number);
    let commodity = document.getElementById('id_commodity').value;
    let source = document.querySelector('.row-exchange.table-row-visible.tr-column-' + column_number + ' select').value;
    // console.log(commodity, source);
    clear_fields_all();
    if (['electricity_futures'].indexOf(commodity) >= 0) {
        // console.log('ee');
        let loads = document.getElementById('load_type_tr_' + column_number);
        make_invis_all('.row-product.tr-column-' + column_number);

        if (zone !== 'empty') {
            make_vis(loads);
        }
    }
    make_invis_all('.row-product.tr-column-' + column_number);
    if (zone === 'empty') {
        clear_fields_all();
    } else {
        let select_div;
        if (commodity === 'co2') {
            select_div = document.getElementById('product_types_co2_tr_' + column_number);
        } else {
            select_div = document.getElementById('product_types_' + source + '_tr_' + column_number);
        }
        // console.log('product_types_' + source + '_' + column_number + '-div-id');
        make_vis(select_div);

    }
    button_change();
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
    let commodity = document.getElementById('id_commodity').value;
    let product = document.getElementById(element_id).value;
    let column_number = element_id.split('_').at(-1);
    let source = document.querySelector('.row-exchange.table-row-visible.tr-column-' + column_number + ' select').value;
    clear_fields_all();
    make_invis_all('.row-period.tr-column-' + column_number);
    if (product !== 'empty') {
        if (product === 'day' || product === 'da') {
            if (source === 'eex' || commodity === 'gas') {
                let select_div = document.getElementById(product_dict['day_eex'] + 'tr_' + column_number);
                // console.log(element + column_number + '-div-id');
                make_vis(select_div);
            } else {
                console.log(product_dict[product]);
                for (let element of product_dict[product]) {
                    let select_div = document.getElementById(element + 'tr_' + column_number);
                    console.log(element + 'tr_' + column_number);
                    make_vis(select_div);
                }
            }
        } else {
            let select_div = document.getElementById(product_dict[product] + 'tr_' + column_number);
            // console.log(product_dict[product] +'tr_' + column_number);
            make_vis(select_div);
        }
    }
    let delivery_year = document.getElementById('year_tr_' + column_number);
    make_invis(delivery_year);
    clear_fields_all();
    button_change();
}

function delivery_period_change(element_id) {
    let delivery_period = document.getElementById(element_id).value;
    let column_number = element_id.split('_').at(-1);
    let product_type = document.querySelector('.row-product.table-row-visible.tr-column-' + column_number + ' select').value;
    // console.log(delivery_period);
    // console.log(product_type);
    clear_fields_all()
    // make_invis_all('select-period select-column-' + column_number);
    make_invis_all('row-year tr-column-' + column_number);

    let del_start = document.getElementById('period_deliverystart_tr_' + column_number);
    let del_end = document.getElementById('period_deliverystart_tr_' + column_number);
    make_invis(del_start);
    make_invis(del_end);

    let year_field = document.getElementById('year_tr_' + column_number);
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
    // console.log(form_filled_1);
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
                    if (Object.keys(dict).length === 5) {
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
    console.log('COUNT', count);
    // console.log(count);
    if (count === 2) {
        enable_button()
    } else {
        disable_button();
    }
    equalize_table();
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
