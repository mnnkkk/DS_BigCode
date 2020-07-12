$.get('./data2.json', function (data) {
    const chart = new G2.Chart({
        container: 'container',
        autoFit: true,
        height: 500,
        padding: [40, 0],
    });

    chart.data(data);
    chart.coordinate('polar', {
        startAngle: Math.PI, // 起始角度
        endAngle: Math.PI * (3 / 2), // 结束角度
    });

    chart.scale('value', {
        tickCount: 6,
    });

    chart.axis('value', {
        grid: {
            line: {
                type: 'circle',
            },
            closed: false,
        },
        verticalFactor: 1,
        label: {
            offset: 15,
        }
    });

    chart.axis('type', {
        tickLine: {
            alignTick: false
        },
        grid: {
            alignTick: false
        }
    });

    chart.tooltip({
        showMarkers: false
    });
    chart.interaction('element-highlight');

    chart
        .interval()
        .position('type*value')
        .color('type', 'rgb(252,143,72)-rgb(255,215,135)')
        .label('value', {
            offset: -15,
            style: {
                textAlign: 'center',
                fill: '#000',
            },
        })
        .style({
            lineWidth: 1,
            stroke: '#fff',
        });

    chart.render();
});