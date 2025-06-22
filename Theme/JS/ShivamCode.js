function DoGraph(containerName,catZ,req,Actual){
    RBGcharts.chart(containerName, {
        plotOptions: {
            area: {
                color: ' rgba(169, 239, 140, 0.80)',
                lineColor: 'red', lineWidth: 1,
                marker: { enabled: false }
            }
        },
        chart:{plotBackgroundColor:"rgba(0,255,0,0.5)"},
        title: null,
        subtitle: { text: 'Average Volatag Gate wise' },
        xAxis: {  categories: catZ, crosshair: true },
        yAxis: { min:11.0, title: { text: ' Voltage' } },
        
        series: [
            { type: 'areaspline', name: 'RequiredVoltabe', data: req, color: "rgba(255,155,155,1)",
                 marker: { enabled: false, states: { hover: { enabled: false } } } },
            { type: 'spline', name: 'ActualAverage',dataLabels: { enabled: true,format: '{point.y:.2f}' }, data: Actual, color: "black", 
                marker: { enabled: true, states: { hover: { enabled: false } } } }]
        });
}

function DoGraph1(containerName,catZ,actual,req){
    RBGcharts.chart(containerName, {
        plotOptions: {
            area: {
                color: ' rgba(169, 239, 140, 0.80)',
                lineColor: 'red', lineWidth: 1,
                marker: { enabled: false }
            }
        },
        chart:{plotBackgroundColor:"rgba(0,255,0,0.5)"},
        title: null,
        subtitle: { text: 'Average SOC Gate wise' },
        xAxis: {  categories: catZ, crosshair: true },
        yAxis: { min:11.0, title: { text: ' Voltage' } },
        
        series: [
            { type: 'areaspline', name: 'RequiredSOC', data: req, color: "rgba(255,155,155,1)",
                marker: { enabled: false, states: { hover: { enabled: false } } } },
            { type: 'spline', name: 'ActualAverage',dataLabels: { enabled: true,format: '{point.y:.2f}' }, data: actual, color: "black", 
                marker: { enabled: true, states: { hover: { enabled: false } } } }]
        });
}