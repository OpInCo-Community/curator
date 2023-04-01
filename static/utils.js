//filter widget setup
const selectElement = document.querySelector('#filter');
const formElement = document.querySelector("#searchForm")
selectElement.addEventListener('change', (event) => {
 formElement.submit()
});