$.get('./data.json', function (data) {
    const chart = new G2.Chart({
        container: 'container',
        autoFit: true,
        height: 500,
    });

    chart.data(data);
    chart.scale({
        pass_rate: {
            range: [0, 1],
        },
        ct: {
            nice: true,
        },
    });

    chart.tooltip({
        showCrosshairs: true,
        shared: true,
    });

    chart.axis('ct', {
        label: {
            formatter: (val) => {
                return val;
            },
        },
    });

    chart
        .line()
        .position('pass_rate*ct')
        .color('difficulty')
        .shape('smooth');

    chart
        .point()
        .position('pass_rate*ct')
        .color('difficulty')
        .shape('circle');

    chart.render();
});