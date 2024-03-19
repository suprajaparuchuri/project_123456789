function submitForm() {
    var dropdown1Value = document.getElementById("dropdown1").value;
    var dropdown2Value = document.getElementById("dropdown2").value;


    if (dropdown1Value === "optionA" && dropdown2Value === "option2") {
        window.location.href='/query';
    }
    else if (dropdown1Value === "optionA" && dropdown2Value === "option1") {
        window.location.href = '/queries2';
    }

    else {
        alert("Dropdown values are different");
    }
}
