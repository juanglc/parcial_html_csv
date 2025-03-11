document.addEventListener("DOMContentLoaded", function() {
    var deleteIdInput = document.getElementById("delete-id");
    var dataLength = deleteIdInput.getAttribute("data-length");

    if (dataLength) {
        deleteIdInput.placeholder = "El ID debe estar entre 0 y " + (parseInt(dataLength) - 1);
    }
});
