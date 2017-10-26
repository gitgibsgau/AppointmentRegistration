// form validation code(form is submitted only when all the fields are filled).
function validateForm() {
	var description = true;

    var appointmentDate = document.forms["addForm"]["Date"].value;
    if (appointmentDate == "") {
		document.getElementById("dateErrorMessage").innerHTML ="Date cannot be empty!!!";
    	description = false;
    	}
	
	var appointmentTime = document.forms["addForm"]["Time"].value;
	if (appointmentTime == "") {
		document.getElementById("timeErrorMessage").innerHTML ="Time cannot be empty!!!";
    	description = false;
    	}

	var des = document.forms["addForm"]["Description"].value;
		if (des == "") {
		document.getElementById("descriptionErrorMessage").innerHTML ="Description cannot be empty!!!";
		description = false;
    	}

	return description;
	
}