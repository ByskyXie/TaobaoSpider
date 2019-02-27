function getDomainFromUrl(url){
    var host = "null";
    if(typeof url == "undefined" || url == null)
        url = window.location.href;
    var regex = /.*\:\/\/([^\/]*).*/;
    var match = url.match(regex);
    if(typeof match != "undefined" && match != null)
        host = match[1];
    return host;
}

function checkWeatherShow(tabId, changeInfo, tab){
    host = getDomainFromUrl(tab.url).toLowerCase();
    if(host == "www.jd.com" || host == "www.taobao.com" || host == "www.tmall.com"){
        chrome.pageAction.show(tabId);
    }
}

chrome.tabs.onUpdated.addListener(checkWeatherShow);