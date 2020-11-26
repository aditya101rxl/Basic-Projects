console.log("This is Today's news");

// apikey = 7b7b18e9d570431e905c090773613592


// getting position to load on server.
let newsList = document.getElementById('newsList');

// this is my apikey request link;
// http://newsapi.org/v2/top-headlines?sources=bbc-news&apikey=7b7b18e9d570431e905c090773613592

// fatching data, using ajax
let lang = 'en';
let country = 'in';
let apiKey = '492ba7f915d485580d99f0f7dbfa5fbd'

fetch('https://gnews.io/api/v4/top-headlines?lang=en&token=492ba7f915d485580d99f0f7dbfa5fbd', {
    "method": "GET"
})
    .then(response => response.json())
    .then(data => {
        console.log(data.articles);
        let articles = data.articles;
        // console.log(articles);
        let headlines = "";
        articles.forEach(element => {
            // console.log(element);
            headlines += `<div class="media">
                            <img src="${element.image}" width="200" height="130" class="mr-3" alt="...">
                            <div class="media-body">
                                <h3 class="mt-0"><u>${element.title}</u></h3>
                                <i><b> -> ${element.description} </b></i><br>
                                ${element.content}
                                <a href="${element.url}" target="_blank"> Read more...</a><br>
                                Published At : ${element.publishedAt}
                            </div>
                        </div><hr>`
        });
        newsList.innerHTML = headlines;
    })
    .catch(err => {
        console.log(err);
    })
// Create an ajax get request
// const xhr = new XMLHttpRequest();
// http://newsapi.org/v2/top-headlines?sources=bbc-news&apikey=7b7b18e9d570431e905c090773613592
// xhr.open('GET', `https://gnews.io/api/v4/top-headlines?lang=en&token=492ba7f915d485580d99f0f7dbfa5fbd`, true);

// // What to do when response is ready
// xhr.onload = function () {
//     if (this.status === 200) {
//         let json = JSON.parse(this.responseText);
//         let articles = json.articles;
//         // console.log(articles);
//         let headlines = "";
//         articles.forEach(element => {
//             // console.log(element);
//             headlines += `<div class="media">
//                             <img src="${element.image}" width="200" height="130" class="mr-3" alt="...">
//                             <div class="media-body">
//                                 <h3 class="mt-0"><u>${element.title}</u></h3>
//                                 <i><b> -> ${element.description} </b></i><br>
//                                 ${element.content}
//                                 <a href="${element.url}" target="_blank"> Read more...</a><br>
//                                 Published At : ${element.publishedAt}
//                             </div>
//                         </div><hr>`
//         });
//         newsList.innerHTML = headlines;
//     }
//     else {
//         console.log("Some error occured")
//     }
// }

// xhr.send()


