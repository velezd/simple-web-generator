/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function showMenu() {
    var x = document.getElementById("menu");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

$(function() {
    var header = document.getElementById("header");
    var menu = document.getElementById("navigation");
    $(window).scroll(function() {    
        var scroll = $(window).scrollTop();
    
        if (scroll >= 100) {
            header.className = "header-small";
            menu.className = "nav-small";
        } else {
            header.className = "";
            menu.className = "";
        }
    });
});