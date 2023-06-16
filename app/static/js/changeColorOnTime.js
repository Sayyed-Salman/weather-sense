document.addEventListener('DOMContentLoaded', function(){
    let date = new Date();
    let rightNow = get24hourTime()
    let day = getDate()

    let dateListFromHTML = document.querySelectorAll('#weatherObj #time #date');

    for(let i = 0; i < dateListFromHTML.length; i++){
        if(dateListFromHTML[i].innerHTML.trim() == day){
            dateListFromHTML[i].parentElement.parentElement.classList.add('order-first')
            timeNode = dateListFromHTML[i].parentElement.childNodes[1].innerHTML.trim()
            if(timeNode == rightNow){
                dateListFromHTML[i].parentElement.parentElement.classList.add('bg-blue-500')
            }
        }
    }

})

function get24hourTime() {
    var now = new Date();
    var hour = now.getHours();
    hour = (hour < 10 ? "0" : "") + hour;
    return hour+":00";
}

function getDate() {
    var now = new Date();
    var day = now.getDate();
    var month = now.getMonth() + 1;
    month = (month < 10) ? "0" + month : month;
    var year = now.getFullYear().toString();
    var formattedDate = day + "/" + month + "/"+year;
    return formattedDate;
}
