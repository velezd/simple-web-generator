// Google Analytics
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {'ad_storage': 'denied', 'analytics_storage': 'denied'}); // Require consent for ad storage and analytics storage.
gtag('js', new Date());
gtag('set', 'allow_google_signals', false); // Disable all advertising features
gtag('config', 'GA_TRACKING_ID', {'anonymize_ip': true}); // Enable IP anonymization - put tracking id here


function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}


function check_consent() {
    var div = document.getElementById("cookies");
    if (getCookie("sv_cookies_consent") == "true") {
        div.style.display = "none";
        gtag('consent', 'update', {'analytics_storage': 'granted'}); 
    }
    else {
        div.style.display = "block";
    }

}


function give_consent() {
    setCookie("sv_cookies_consent", "true", 365)
    var div = document.getElementById("cookies");
    div.style.display = "none";
    gtag('consent', 'update', {'analytics_storage': 'granted'}); 
}


$(window).on('load', function() {
    check_consent()
});
