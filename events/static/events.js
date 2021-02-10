function toggle(elName) {
    const el = document.querySelector(`#${elName}`);
    const displayList = el.nextElementSibling;
    el.classList.toggle('closed');
    displayList.classList.toggle('closed');
}

// Google Mapß

function initMap() {
    const map = new google.maps.Map(document.querySelector("#eventsMap"), {
        zoom: 9,
        center: {lat: 55.8617792, lng: -3.7054024}
    });
    setMarkers(map);
}

// function setMarkers(map) {
//     const eventsList = document.querySelector(".events__accordion");

//     events.forEach((event) => {
//         const marker = new google.maps.Marker({
//             map: map,
//             position: {lat: event.lat, lng: event.lng},
//             title: event.title,
//             number: event.number
//         });
//         const windowContent = `
//             <h4>${event.title}</h4>
//             <h5>${event.location}</h5>
//             <h6>More info at top of events list</h6>
//             `;
//         const infoWindow = new google.maps.InfoWindow({
//             content: windowContent,
//             number: event.number
//         });
//         const eventListContent = `
//         <div class="form-section main-text row accordian" id="accordian${event.number}">
//             <div class="col">
//                 <div id="heading${event.number}" class="row">
//                     <div class="col-10 event-heading" data-toggle="collapse" data-target="#collapse${event.number}" aria-expanded="false" aria-controls="collapse${event.number}">
//                         <h3>${event.title}</h3>
//                         <h4>${event.datetime}</h4>
//                         <h5>${event.location}</h5>
//                     </div>
//                     <div class="col-2">
//                         <h3><i class="fas fa-calendar-check"></i></h3>
//                     </div>
//                 </div>
//                 <div id="collapse${event.number}" class="collapse row" aria-labelledby="heading${event.number}" data-parent="#accordian">
//                     <div class="main-text col">
//                         <h4>${event.description}</h4>
//                         <h4 class="main-text">Book your place now
//                         <a class="main-text" href="/contact.html" target="_blank"><i class="fas fa-envelope"></i></a>
//                         <a class="main-text" href="https://www.facebook.com/rpoas.lanarkshire" target="_blank"><i class="fab fa-facebook-square"></i></a>
//                         </h4>
//                         <img src="${event.photo}">
//                     </div>
//                 </div>
//             </div>
//         </div>
//         `;        

//         function filter() {
//             const currentAccordian = document.querySelector(`#accordian${event.number}`);
//             const accordiansArray = Array.from(document.querySelectorAll(".accordian"));

//             //opens infoWindow
//             infoWindow.open(map, marker); 
//             //moves event to top of list
//             currentAccordian.remove();
//             eventsList.insertAdjacentElement("afterbegin", currentAccordian);
//             //expands relevant event
//             $(`#collapse${event.number}`).collapse("show");
//         }

//         eventsList.insertAdjacentHTML("beforeend", eventListContent);
//         marker.addListener("click", filter);
//         google.maps.event.addListener(map, "click", function() {
//             infoWindow.close();
//         });
//     });
// }