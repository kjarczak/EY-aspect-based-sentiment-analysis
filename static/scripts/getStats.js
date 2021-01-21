document.addEventListener("DOMContentLoaded", function () {
    let inputForm = document.getElementById("inputForm");
    inputForm.addEventListener("submit", function (event) {
        event.preventDefault();
        let url = '/get-model';

        let params = {
            method: 'POST',
            body: new FormData(inputForm),
            redirect: "follow",
        };

        fetch(url, params).then(function (response) {
            if (response.status === 200) {
                response.json().then(data => {
                    getPlots(data);
                });
            } else {
                console.log('error');
            }
        });

        function getPlots(data) {
            getAveragePlot(data).then(function () {
                getCountsPlot(data);
            });
        }

        function getAveragePlot(data) {
            let plot = document.getElementById("average");
            let url = "/plot-average";
            let params = {
                method: "POST",
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                }
            }

            return fetch(url, params).then(response => {
                response.blob().then(blob => {
                    let urlCreator = window.URL || window.webkitURL;
                    let imageUrl = urlCreator.createObjectURL(blob);
                    plot.src = imageUrl;
                    plot.hidden = false;
                });
            });
        }

        function getCountsPlot(data) {
            let plot = document.getElementById("counts");
            let url = "/plot-counts";
            let params = {
                method: "POST",
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                }
            }

            fetch(url, params).then(response => {
                response.blob().then(blob => {
                    let urlCreator = window.URL || window.webkitURL;
                    let imageUrl = urlCreator.createObjectURL(blob);
                    plot.src = imageUrl;
                    plot.hidden = false;
                });
            });
        }
    });
});