// document JavaScript pour les interactions avec la barre latérale et la navigation dynamique sur le site
//pré remplir les inputs date en metant celle d'aujourd'hui
document.querySelector("#today").valueAsDate = new Date();
// variable global
var isOpen = false;

var bootstrapButton = $.fn.modal.noConflict()
var bootstrapButton = $.fn.datetimepicker.noConflict()
// fonction d'ouverture/fermeture du volet latéral
function Nav() {
    if (isOpen) {
        document.getElementById("sideBar").style.width = "0";
        document.getElementById("navBar").style.marginLeft = "0";
        document.getElementById("main").style.marginLeft = "0";
        document.getElementById("footer").style.marginLeft = "0";
        document.getElementById("openNav").style.marginLeft = "0";

    } else {
        document.getElementById("sideBar").style.width = "250px";
        document.getElementById("navBar").style.marginLeft = "250px";
        document.getElementById("main").style.marginLeft = "250px";
        document.getElementById("footer").style.marginLeft = "250px";
        let obj = document.getElementById("openNav");
        obj.style.marginLeft = -1.6 * (obj.getBoundingClientRect().width) + "px";
    }
    isOpen = !isOpen;
}
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

function openTab(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

function setDateDefault() {
  d = new Date();
  year = d.getFullYear().toString();
  month = d.getMonth().toString();
  day = d.getDate().toString();
  dateFormatee =  year + "-" + month + "-" + day;
  document.getElementById("dateCreation").defaultValue = "2018-04-03";
  // document.getElementById('today').innerHTML = '<input type="date" name="Data" value="'+TodayDate()+'" ><br>';
}
// fonction de récupération d'url pour la navigation sur la barre de navigation
function getURL() {
    var url = window.location.pathname;

    //route de la page d'accueil du site
    if (url === '/') {
        document.getElementById('accueil').classList.add('active');

    //route de la section générateur de document
    } else if (url.includes('/generateurDocument/'))  {
        document.getElementById('genDoc').classList.add('active');
    }
}