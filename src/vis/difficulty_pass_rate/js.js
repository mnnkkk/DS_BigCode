$.get('./data.json', function (data) {
    const chart = new G2.Chart({
        container: 'container',
        autoFit: true,
        height: 500,
    });

    chart.data(data);
    chart.scale({
        month: {
            range: [0, 1],
        },
        temperature: {
            nice: true,
        },
    });

    chart.tooltip({
        showCrosshairs: true,
        shared: true,
    });

    chart.axis('temperature', {
        label: {
            formatter: (val) => {
                return val + ' °C';
            },
        },
    });

    chart
        .line()
        .position('month*temperature')
        .color('city')
        .shape('smooth');

    chart
        .point()
        .position('month*temperature')
        .color('city')
        .shape('circle');

    chart.render();
});