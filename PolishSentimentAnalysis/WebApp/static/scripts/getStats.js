document.addEventListener("DOMContentLoaded", function () {
    let spinner = document.getElementById("spinner");
    let inputForm = document.getElementById("inputForm");
    let tweetTable = document.getElementById("tweets-example");
    inputForm.addEventListener("submit", function (event) {
        event.preventDefault();
        spinner.hidden = false;
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
            }).then(function () {
                getTweetsExample(data);
            }).then(function () {
                spinner.hidden = true;
                tweetTable.hidden = false;
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

        function getTweetsExample(data) {
            appendTableRows();
            let positiveIndices = [];
            let negativeIndices = [];
            let neutralIndices = [];
            let sentimentList = [];
            let contentList = [];

            for (let i in data.sentiment) {
                sentimentList.push(data.sentiment[i]);
            }
            for (let i in data.content) {
                contentList.push(data.content[i]);
            }

            for (let i = 0; i < sentimentList.length; i++) {
                if (sentimentList[i] === -1 && negativeIndices.length < 3) {
                    negativeIndices.push(i);
                } else if (sentimentList[i] === 0 && neutralIndices.length < 3) {
                    neutralIndices.push(i);
                } else if (sentimentList[i] === 1 && positiveIndices.length < 3) {
                    positiveIndices.push(i);
                }
            }
            for (let i = 0; i < negativeIndices.length; i++) {
                appendTweet(-1, i, contentList[negativeIndices[i]]);
            }
            for (let i = 0; i < neutralIndices.length; i++) {
                appendTweet(0, i, contentList[neutralIndices[i]]);
            }
            for (let i = 0; i < positiveIndices.length; i++) {
                appendTweet(1, i, contentList[positiveIndices[i]]);
            }
        }

        function appendTableRows() {
            let table = document.getElementById("table-body");
            for (let i = 0; i < 3; i++) {
                let row = document.createElement("tr");
                row.id = "row-" + i;
                for (let j = -1; j < 2; j++) {
                    let column = document.createElement("td");
                    column.id = "column-" + i + "-" + j;
                    row.appendChild(column);
                }
                table.appendChild(row);
            }
        }

        function appendTweet(sentiment, rowNo, content) {
            let column = document.getElementById("column-" + rowNo + "-" + sentiment);
            column.innerText = content;
        }
    });
});
