function show_all() {
    let init_table = document.getElementById('short-table');
    let long_table = document.getElementById('long-table');
    let show_all_button = document.getElementById('show-all');

    if (!init_table.classList.contains('hidden-results')) {
        init_table.classList.add('hidden-results');
    }

    if (long_table.classList.contains('hidden-results')) {
        long_table.classList.remove('hidden-results');
    }

    show_all_button.classList.add('hidden-results');
}