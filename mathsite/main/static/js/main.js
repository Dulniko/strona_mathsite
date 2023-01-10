document.getElementById("number-input").focus();
document.getElementById("number-input").addEventListener("input", function(event) {
    this.value = this.value.replace(/[^\d]/g, '').slice(0, 3);
    console.log(this.value)
    });
