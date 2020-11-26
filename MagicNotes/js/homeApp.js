console.log('This is Magic Page');
showNotes();

// targetting add btn to add notes
let addBtn = document.getElementById('addBtn');
addBtn.addEventListener('click', function (e) {

    let addTxt = document.getElementById('addTxt');
    let addTitle = document.getElementById('addTitle');
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }
    // console.log(addTxt.value);
    notesObj.push([addTitle.value,addTxt.value]);
    localStorage.setItem('notes', JSON.stringify(notesObj));
    addTitle.value="";
    addTxt.value = "";
    showNotes();
});

function showNotes() {
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }
    let html = "";
    notesObj.forEach(function (element, index) {
        html += `<div class="noteCard mx-2 my-2 card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title"><u>${element[0]}</u></h5>
                        <p class="card-text">${element[1]}</p>
                        <button id=${index} onclick="deleteNote(this.id)" class="btn btn-primary">Delete Note</button>
                    </div>
                </div>`;
    });
    let setHmtl = document.getElementById('notesTable');
    if (notesObj.length != 0) {
        setHmtl.innerHTML = html;
    }
    else {
        setHmtl.innerHTML = `you haven't any NOTES to show!, Please add some Notes`;
    }
    // console.log(html);
};

function deleteNote(index) {
    // console.log("I'm deleting this note ", index);
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }
    notesObj.splice(index, 1);
    localStorage.setItem('notes', JSON.stringify(notesObj));
    showNotes();
};

let search = document.getElementById('searchArea');
search.addEventListener('input', function (e) {
    let searchVal = search.value.toLowerCase();
    // console.log(search.value);
    let noteCards = document.getElementsByClassName('noteCard');
    // console.log(noteCards);
    Array.from(noteCards).forEach(function (element) {
        let cardTxt = element.getElementsByTagName('p')[0].innerText;
        if (cardTxt.includes(searchVal)) {
            element.style.display = "block";
        }
        else {
            element.style.display = 'none';
        }
        // console.log(cardTxt);
    });
});
// let crd = document.getElementsByClassName('noteCard')[0];
// crd.addEventListener('mouseover', function (e) {
//     document.body.style.backgroundColor = 'red';
// })
// console.log(crd);
// document.getElementsById('notesTable').addEventListener('mouseover',function(e){
//     document.body.style.backgroundColor='red';
// });

/*

further improvement
1. add title.
2. mark as important.
3. separete notes by user.
4. sync and host to the web server.
*/
