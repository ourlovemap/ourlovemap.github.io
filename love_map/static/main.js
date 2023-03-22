var map = L.map('mapid').setView([-23.5505, -46.6333], 13);
var mmIcon = L.icon({
    iconUrl: "https://pngimg.com/d/m_m_PNG4.png",
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
      m.bindPopup(`<b>${marker.name}</b><br>${marker.description}`).openPopup();
    });
  });