var rows;
var columns;



$("#get").click(function(){
    var vals = getMatrix();
	var valString = vals.toString();
	document.getElementById("id_numbers").value = valString;
	document.getElementById("id_rows").value = document.getElementById("val_m").value;
	document.getElementById("id_cols").value = document.getElementById("val_n").value;
	console.log(valString);
	
	
	
});

$("#set").click(function(){
    var rows = document.getElementById("val_m").value;
	var columns = document.getElementById("val_n").value;
	
	
	var form = document.getElementById("frm");

	for(var i = 0; i < rows; i++)
            {
                for(var j = 0; j < columns; j++)
                {
                    var input = $('<input>')
                        .attr({
                            class: 'matrix_cell',
                            value: i + j});
                    form.appendChild(input[0]);
                }
                var br = $('<br>')[0];
                form.appendChild(br);
            }
	
});

function getMatrix(){
    var matrix_row = [];

    var ind = 0;
    
    $("#frm").contents().each(function(i,e){
        if (this.nodeName == "INPUT")
        {
            if (!matrix_row[ind]){
                matrix_row.push([]);
            }
             matrix_row[ind].push($(this).val());            
        }
        else{
            ind++;
        }
    });
    
    return matrix_row;
}

