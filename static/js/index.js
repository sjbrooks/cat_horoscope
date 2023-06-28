const getHoroscope = () => fetch("http://0.0.0.0:4040/cat_horoscope?sun_sign=aries").then(
  resp => {
    console.log(resp);
    return resp.json()
  }).then((json) => {
  console.log(json);
  document.getElementById("root").innerText = json.cat_horoscope;
});

getHoroscope();
