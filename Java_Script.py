function palindrome(myString) {

    var input = myString.replace(/[^A-Z0-9]/ig, "").toLowerCase();

    var reversed = input.split('').reverse().join('');

    if (input === reversed) {

        document.write("<div>" + myString + " is a palindrome</div>");

    } else {

        document.write("<div>" + myString + " is not a palindrome</div>");

    }
}

palindrome("madam"); 