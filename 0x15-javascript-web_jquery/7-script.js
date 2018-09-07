let reqURL = 'https://swapi.co/api/people/5/?format=json';
$.get(reqURL, function (data, status) {
  let person = data;
  $('#character').text(person.name);
});
