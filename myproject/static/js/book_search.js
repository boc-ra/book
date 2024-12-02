document.getElementById('book-title').addEventListener('input', function() {
    let query = this.value;
    if (query.length < 3) {
        document.getElementById('book-suggestions').innerHTML = '';
        return;
    }

    fetch(`https://www.googleapis.com/books/v1/volumes?q=intitle:${query}&key=GOOGLE_BOOKS_API_KEY`)
        .then(response => response.json())
        .then(data => {
            let suggestions = data.items || [];
            let suggestionList = document.getElementById('book-suggestions');
            suggestionList.innerHTML = '';

            suggestions.forEach(function(item) {
                let listItem = document.createElement('li');
                listItem.textContent = item.volumeInfo.title;
                listItem.addEventListener('click', function() {
                    document.getElementById('book-title').value = item.volumeInfo.title;
                    document.getElementById('book-writer').value = item.volumeInfo.authors ? item.volumeInfo.authors.join(', ') : 'Unknown';
                    document.getElementById('book-suggestions').innerHTML = '';
                });
                suggestionList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching books:', error));
});
