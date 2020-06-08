
function tab_control(event, option){
    var i, links, containers;

    links = document.getElementsByClassName('tab-link');
    containers = document.getElementsByClassName('tab-container');

    for(i=0; i<links.length; i++){
        containers[i].style.display = 'none';
        links[i].className = links[i].className.replace(' tab-link-active', "")
    }

    document.getElementById(option).style.display = 'block';
    event.currentTarget.className += ' tab-link-active';
    change_parm('tab', event.currentTarget.id);
}
