// Create root element
// https://www.amcharts.com/docs/v5/getting-started/#Root_element
// let root = am5.Root.new("chartdiv");

let graphs = document.getElementById('graphs');

let rows = graphs.getElementsByClassName('row');

let chart_values = [];

let roots_timedata = {};
let roots_spreads = {};

function form_timedata(year) {
    let data_time = [];
    let data_spread = [];
    for (const key in dict_data[year]['trading_date']) {
        data_time.push(
            {
                date: new Date(dict_data[year]['trading_date'][key]).getTime(),
                value1: dict_data[year]['price_1'][key],
                value2: dict_data[year]['price_2'][key],
                previousDate: dict_data[year]['trading_date'][key],
            }
        );
        data_spread.push(
            {
                date: new Date(dict_data[year]['trading_date'][key]).getTime(),
                value: dict_data[year]['delta'][key],
                previousDate: dict_data[year]['trading_date'][key],
            }
        )
    }
    console.log(data_spread);
    return [data_time, data_spread];
}

function create_timedata_graph(year, data) {
    roots_timedata[year] = am5.Root.new("timedata-" + year);

    roots_timedata[year].setThemes([
        am5themes_Animated.new(roots_timedata[year])
    ]);


// Create chart
// https://www.amcharts.com/docs/v5/charts/xy-chart/
    var chart = roots_timedata[year].container.children.push(am5xy.XYChart.new(roots_timedata[year], {
        panX: true,
        panY: true,
        wheelX: "panX",
        wheelY: "zoomX",
        pinchZoomX: true
    }));

    chart.get("colors").set("step", 3);


// Add cursor
// https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
    var cursor = chart.set("cursor", am5xy.XYCursor.new(roots_timedata[year], {}));
    cursor.lineY.set("visible", false);


// Create axes
// https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
    var xAxis = chart.xAxes.push(am5xy.DateAxis.new(roots_timedata[year], {
        maxDeviation: 0.3,
        baseInterval: {
            timeUnit: "day",
            count: 1
        },
        renderer: am5xy.AxisRendererX.new(roots_timedata[year], {}),
        tooltip: am5.Tooltip.new(roots_timedata[year], {})
    }));

    var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(roots_timedata[year], {
        maxDeviation: 0.3,
        renderer: am5xy.AxisRendererY.new(roots_timedata[year], {})
    }));




// https://www.amcharts.com/docs/v5/charts/xy-chart/series/
    var series = chart.series.push(am5xy.LineSeries.new(roots_timedata[year], {
        name: "BUY",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value1",
        valueXField: "date",
        tooltip: am5.Tooltip.new(roots_timedata[year], {
            labelText: "BUY: {valueY}\nSELL: {value2}"
        }),
        stroke: am5.color('#00f')
    }));

    series.strokes.template.setAll({
        strokeWidth: 2
    });

    series.get("tooltip").get("background").set("fillOpacity", 0.5);

    // Add series
    var series2 = chart.series.push(am5xy.LineSeries.new(roots_timedata[year], {
        name: "SELL",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value2",
        valueXField: "date",
        stroke: am5.color('#f00')
    }));

    series2.strokes.template.setAll({
        // strokeDasharray: [2, 2],
        strokeWidth: 2
    });

// Set date fields
// https://www.amcharts.com/docs/v5/concepts/data/#Parsing_dates
    roots_timedata[year].dateFormatter.setAll({
        dateFormat: "yyyy-MM-dd",
        dateFields: ["valueX"]
    });

    let legend = chart.children.push(am5.Legend.new(roots_timedata[year], {
        x: am5.percent(22),
        centerX: am5.percent(50),
        markerLabelGap: 80,
        layout: roots_timedata[year].verticalLayout
    }));
    legend.data.setAll(chart.series.values);

    series.data.setAll(data);
    series2.data.setAll(data);

    roots_timedata[year]._logo.dispose();
}

function create_spread_graph(year, data_spreads) {
    roots_spreads[year] = am5.Root.new("spreads-" + year);

    roots_spreads[year].setThemes([
        am5themes_Animated.new(roots_spreads[year])
    ]);


// Create chart
// https://www.amcharts.com/docs/v5/charts/xy-chart/
    var chart = roots_spreads[year].container.children.push(am5xy.XYChart.new(roots_spreads[year], {
        panX: true,
        panY: true,
        wheelX: "panX",
        wheelY: "zoomX",
        pinchZoomX: true
    }));

    chart.get("colors").set("step", 3);


// Add cursor
// https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
    var cursor = chart.set("cursor", am5xy.XYCursor.new(roots_spreads[year], {}));
    cursor.lineY.set("visible", false);


// Create axes
// https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
    var xAxis = chart.xAxes.push(am5xy.DateAxis.new(roots_spreads[year], {
        maxDeviation: 0.3,
        baseInterval: {
            timeUnit: "day",
            count: 1
        },
        renderer: am5xy.AxisRendererX.new(roots_spreads[year], {}),
        tooltip: am5.Tooltip.new(roots_spreads[year], {})
    }));

    var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(roots_spreads[year], {
        maxDeviation: 0.3,
        renderer: am5xy.AxisRendererY.new(roots_spreads[year], {})
    }));


// Add series
// https://www.amcharts.com/docs/v5/charts/xy-chart/series/
    var series_spread = chart.series.push(am5xy.LineSeries.new(roots_spreads[year], {
        name: "Series 1",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        valueXField: "date",
        tooltip: am5.Tooltip.new(roots_spreads[year], {
            labelText: "Spread: {valueY}"
        }),
        // stroke: am5.color('#00f')
    }));

    series_spread.strokes.template.setAll({
        strokeWidth: 2
    });

    series_spread.get("tooltip").get("background").set("fillOpacity", 0.5);

    // Set date fields
// https://www.amcharts.com/docs/v5/concepts/data/#Parsing_dates
    roots_spreads[year].dateFormatter.setAll({
        dateFormat: "yyyy-MM-dd",
        dateFields: ["valueX"]
    });


    series_spread.fills.template.setAll({
        fillOpacity: 0.5,
        visible: true
    });

    var rangeDataItem = yAxis.makeDataItem({
        value: -1000,
        endValue: 0
    });

    var range = series_spread.createAxisRange(rangeDataItem);
    range.strokes.template.setAll({
        stroke: am5.color(0xff621f),
    });

    range.fills.template.setAll({
        fill: am5.color(0xff621f),
        fillOpacity: 0.5,
        visible: true
    })

    series_spread.data.setAll(data_spreads);

    series_spread.appear(1000);
    chart.appear(1000, 100);

    roots_spreads[year]._logo.dispose();
}


for (const year in dict_data) {
    // if (parseInt(year) < 2019) {
    //     continue;
    // }
    console.log(year);

    // console.log('data1', data_timedata);

    let values = form_timedata(year);
    let data_timedata = values[0];
    let data_spreads = values[1];

    create_timedata_graph(year, data_timedata);

    create_spread_graph(year, data_spreads);
    // console.log('data', data);


// Make stuff animate on load
// https://www.amcharts.com/docs/v5/concepts/animations/


}

// var root = am5.Root.new("chartdiv");




