const form = document.getElementById("form");
form.addEventListener("submit", function () {
    document
        .querySelectorAll("input[type=checkbox]:not(:checked)")
        .forEach(function (item) {
            item.value = "0";
            item.checked = true;
        });
});
