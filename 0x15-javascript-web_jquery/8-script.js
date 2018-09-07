let reqURL = 'https://swapi.co/api/films/?format=json';
$.get(reqURL, function (data, status) {
  let films = data;
  for (let i = 0; i < films.results.length; i++) {
    $('#list_movies').append('<li>' + films.results[i].title + '</li>');
  }
});
