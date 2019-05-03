let allowNumbersOnly = (e) => {
    var code = (e.which) ? e.which : e.keyCode;
    if (code > 31 && (code < 49 || code > 57)) {
        e.preventDefault();
    }
}

let getInputString = () => {
    var x = document.getElementsByClassName('box');
    var inputString = '';

    for(let i of x){
        if(i.value === '')
            inputString += '.';
        else
            inputString += i.value;
    }

    return inputString;
}

let reset = () => {
    let boxes = document.getElementsByClassName('box');

    for(let box  of boxes){
        box.value = '';
        box.removeAttribute("disabled");
    }
}

let send = () => {
    const xhttp = new XMLHttpRequest();

    let inputString = getInputString();
    let url = '/solve';

    xhttp.open('POST', url, true);

    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    xhttp.onreadystatechange = function() {
        //Call a function when the state changes.
        if(xhttp.readyState == 4 && xhttp.status == 200) {
            let solved_string = xhttp.responseText;
            if(solved_string === 'Invalid'){
                alert('Wrong Input.\n Numbers should not be repeated in row, column or square.')
            }
            else {
                let boxes = document.getElementsByClassName('box');
                for(let i = 0; i < boxes.length; i++){
                    boxes[i].value = solved_string[i];
                    boxes[i].setAttribute('disabled', 'true');
                }
            }
        }
    }

    xhttp.send('input_string=' + inputString);
}