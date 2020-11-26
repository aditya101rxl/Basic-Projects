console.log('This is Javascript file');

// variable count of addParams
let addParamsCnt = 2;

document.getElementById('paramsBox').style.display = 'none';

// hidding parameter field when json type is selected
let jsonRadio = document.getElementById('jsonRadio');
jsonRadio.addEventListener('click', () => {
    document.getElementById('paramsBox').style.display = 'none';
    document.getElementById('jsonBox').style.display = 'block';
});

// hidding json field when custom parameter type is selected
let paramsRadio = document.getElementById('paramsRadio');
paramsRadio.addEventListener('click', () => {
    document.getElementById('paramsBox').style.display = 'block';
    document.getElementById('jsonBox').style.display = 'none';
});

// creating div to insert in paramsBox
function createDiv(string) {
    let div = document.createElement('div');
    div.innerHTML = string;
    return div;
}

// listening to addParams button
let addParams = document.getElementById('addParams');
addParams.addEventListener('click', () => {
    let paramsBox = document.getElementById('paramsBox');
    let string = `<div class="form-row my-2">
                    <label for="urlBox" class="col-sm-2 col-form-label">Parameter ${addParamsCnt}</label>
                    <div class="col-md-4">
                        <input type="text" class="form-control" id="key${addParamsCnt}" placeholder="Key">
                    </div>
                    <div class="col-md-5">
                        <input type="text" class="form-control" id="value${addParamsCnt}" placeholder="Value">
                    </div>
                    <button class="btn btn-primary deleteParam"> - </button>
                </div>`;
    addParamsCnt++;
    let child = createDiv(string);
    paramsBox.appendChild(child);
    let remove = document.getElementsByClassName('deleteParam');
    // console.log(remove);
    for (rmv of remove) {
        rmv.addEventListener('click', (e) => {
            e.target.parentElement.remove();
        })
    }
});

// submmission

let submitBtn = document.getElementById('submitBtn');
submitBtn.addEventListener('click', () => {
    // let responseBox = document.getElementById('response').value = 'Please wait... \nFatching Data...';
    let responseBox = document.getElementById('response').innerHTML = 'Please wait... ';

    let url = document.getElementById('url').value;
    let requestType = document.querySelector("input[name='requestType']:checked").value;
    let contentType = document.querySelector("input[name='contentType']:checked").value;
    // console.log(url, requestType, contentType);

    let data;
    if (contentType == 'customParms') {
        data = {};
        for (i = 1; i < addParamsCnt; i++) {
            let key = document.getElementById('key' + i).value;
            if (key == undefined) {
                continue;
            }
            let value = document.getElementById('value' + i).value;
            data[key] = value;
        }
        data = JSON.stringify(data);
    }
    else {
        data = document.getElementById('jsonContent').value;
    }
    // console.log(data);

    // get request
    if (requestType == 'GET') {
        fetch(url, {
            method: 'GET',
        }).then(response => response.text())
            .then((text) => {
                // console.log(text);
                // document.getElementById('response').value = text;
                document.getElementById('response').innerHTML = text;
                Prism.highlightAll();
            });
        }
        else {
            fetch(url, {
                method: 'POST',
                body: data,
                headers: {
                    'Content-type': 'application/json; charset=UTF-8',
                },
            }).then(response => response.text())
            .then((text) => {
                // document.getElementById('response').value = text;
                document.getElementById('response').innerHTML = text;
                Prism.highlightAll();
            })
    }
});