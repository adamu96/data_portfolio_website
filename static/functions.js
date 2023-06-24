  // Line Chart
  $.getJSON({
    url: "/callback-filter-line", data: { 'metric': metric, 'country': country }, success: function (result) {
    Plotly.newPlot('line-chart', result, {staticPlot: true});
    }
});

function plotGraph(data) {
  Plotly.plot('line-chart', data, {});
}

function loadNotebook(location) {
  $("#notebookContent").load(location); 
}
// 946 the ark - not safe