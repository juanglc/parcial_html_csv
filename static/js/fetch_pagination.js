document.addEventListener("DOMContentLoaded", function () {
    const rowsPerPage = 10;
    let currentPage = 1;
    const tableBody = document.querySelector("#data-table tbody");
    const pageNumberSpan = document.getElementById("pageNumber");
    const prevButton = document.getElementById("prevPage");
    const nextButton = document.getElementById("nextPage");

    function fetchData(page) {
        fetch(`/data?page=${page}&per_page=${rowsPerPage}`)
            .then(response => response.json())
            .then(data => {
                tableBody.innerHTML = "";
                data.forEach(row => {
                    const tr = document.createElement("tr");
                    /// tr is table row
                    row.forEach(cell => {
                        const td = document.createElement("td");
                        td.textContent = cell;
                        /// td is table data
                        tr.appendChild(td);
                    });
                    tableBody.appendChild(tr);
                });
                pageNumberSpan.textContent = page;
                prevButton.disabled = page === 1;
                nextButton.disabled = data.length < rowsPerPage;
            });
    }

    prevButton.addEventListener("click", function () {
        if (currentPage > 1) {
            currentPage--;
            fetchData(currentPage);
        }
    });

    nextButton.addEventListener("click", function () {
        currentPage++;
        fetchData(currentPage);
    });

    fetchData(currentPage);
});