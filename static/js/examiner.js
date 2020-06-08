

function get_data(url, callback){
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 &&  this.status == 200){
            callback(this.responseText);
        }
    };

    xhttp.open("GET", url, true);
    xhttp.send();
}

function populate_table(data){
    data = JSON.parse(data);
    var table = document.getElementById("table-tests");

    if(!data){
        var row = table.insertRow(-1);
        var cell = row.insertCell(0);
        cell.colSpan = 9;
        cell.style.text_align = 'center';
        cell.innerHTML = 'There are no tests to show here.';
        return;
    }

    for(i = 0; i < data.length; i++){
        var row = table.insertRow(-1);
        row_data = data[i];

        fields = [
            'title', 
            'description', 
            'date', 
            'subject', 
            'standard', 
            'score_easy', 
            'score_medium', 
            'score_hard', 
            'score_threshold'
        ];

        for(j = 0; j< fields.length; j++){
            var cell = row.insertCell(j);
            if(j == 2){
                cell.innerHTML = new Date(row_data[fields[j]]).toDateString();
                continue;
            }
            cell.innerHTML = row_data[fields[j]];
        }
    }
}

get_data("/examiner/get-tests", populate_table);

