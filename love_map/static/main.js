var map = L.map('mapid').setView([-23.5505, -46.6333], 13);
var mmIcon = L.icon({
    iconUrl: "../images/mm_logo.png",
    iconSize: [75, 30],
    iconAchor: [37.5, 15],
    popupAnchor: [0, 0]
})


L.tileLayer("https://api.maptiler.com/maps/streets-v2/256/{z}/{x}/{y}.png?key=nChY42iRzfUmnzqCRf5z", {
    maxZoom: 18,
}).addTo(map);

fetch("https://ourlovemap-api.onrender.com/api/date_markers")
  .then(response => response.json())
  .then(markers => {
    markers.forEach(marker => {
      var m = L.marker(marker.location, {icon: mmIcon}).addTo(map);
      m.bindPopup(`<h1>${marker.title}</h1><h4>${marker.subtitle}</h4><p>${marker.description}</p><img src='../images/mm_logo.png' width=75px height=30px/>`).openPopup();
    });
  });

  // fetch("http://127.0.0.1:5000/api/date_markers")
  // .then(response => response.json())
  // .then(markers => {
  //   markers.forEach(marker => {
  //     var m = L.marker(marker.location, {icon: mmIcon}).addTo(map);
  //     m.bindPopup(`<h1>${marker.title}</h1><h3>${marker.subtitle}</h3><p>${marker.description}</p><img src='../images/mm_logo.png' width=100% height=100%/>`).openPopup();
  //   });
  // });