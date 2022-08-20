function formValidation() {
    var fname = document.getElementById("id_name").value;
    var email = document.getElementById("id_email").value;
    var phone = document.getElementById("id_phone").value;
    

    var fnamepattern = /^[a-zA-Z. ]+$/;
    var phonePattern = /^(\+88|88)?01[3-9]\d{8}$/;
    var emailPattern = /^[a-zA-Z0-9_-]{3,}@[a-zA-Z0-9_-]{3,}\.[a-zA-Z]{2,4}$/
   

    if (fnamepattern.test(fname)) {
        document.getElementById("error").innerHTML = "";

    } else {
        document.getElementById("error").innerHTML = "**Only Character Are Allowed** In Name";
        return false;
    }

    if (emailPattern.test(email)) {
        document.getElementById("error").innerHTML = "";

    } else {
        document.getElementById("error").innerHTML = "**Email Is Invalid**";
        return false
    }

    if (phonePattern.test(phone)) {
        document.getElementById("error").innerHTML = "";

    } else {
        document.getElementById("error").innerHTML = "**Phone Number Is Invalid**";
        return false;
    }

    
}