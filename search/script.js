document.addEventListener("DOMContentLoaded", ()=>{
    let input = document.querySelector('#luckyButton');
    input.addEventListener("click", () => {
        let query = document.querySelector('#searchQuery').value;
        if (query) {
            window.location.href = `https://www.google.com/search?q=${encodeURIComponent(query)}&btnI=I`;
        }
    });
});