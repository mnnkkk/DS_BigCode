const colorMap = {
    Asia: '#1890FF',
    Americas: '#2FC25B',
    Europe: '#FACC14',
    Oceania: '#223273',
};
$.get('./data.json', function (data) {
    const chart = new G2.Chart({
        container: 'container',
        autoFit: true,
        height: 500,
    });
    chart.data(data);
    // 为各个字段设置别名
    chart.scale({
        overall_average_score: {
            alias: '已做题目的平均分',
            nice: true,
        },
        tried_num: {
            type: 'pow',
            alias: '已做题目的数量'
        },
        overall_sum_score: {
            alias: '已做题目的平均分总分',
            nice: true,
        },
        Uid: {
            alias: 'Uid'
        }
    });
    chart.axis('overall_sum_score', {
        label: {
            formatter(value) {
                return (+value / 1000).toFixed(0) + 'k';
            } // 格式化坐标轴的显示
        }
    });
    chart.tooltip({
        showTitle: false,
        showMarkers: false,
    });
    chart.legend('tried_num', false); // 该图表默认会生成多个图例，设置不展示 tried_num 和 Uid 两个维度的图例
    chart.point().position('overall_sum_score*overall_average_score')
        .size('tried_num', [1, 30])  // 气泡大小 [4， 65]
        .color('continent', val => {
            return colorMap[val];
        })
        .shape('circle')
        .tooltip('Uid*tried_num*overall_sum_score*overall_average_score')
        .style('continent', (val) => {
            return {
                lineWidth: 1,
                strokeOpacity: 1,
                fillOpacity: 0.3,
                opacity: 0.65,
                stroke: colorMap[val],
            };
        });
    chart.interaction('element-active');
    chart.render();
});