$(document).ready.(function() {

   $("#button1").click('click', function(){

        var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
        var fd = new FormData();
        var files = $('#img')[0].files;
        // check files
        if(files.length > 0){
        fd.append('file', files[0]);
        }
        console.log("darshil");
        $.ajax({
        url: $SCRIPT_ROOT + "/predict",
        dataType: 'json'
        contentType: false,
        precessData: false,
        type:"POSTi",
        data: fd,
        success: function(data){
	   	    $('#result').text(' Predicted Output: '+data);
        }
        })

        event.preventDefault();
   });
});

<script type="text/javascript">


                               function upload() {
                                    var myform = document.getElementById("form1");
                                    var fd = new FormData(myform );
                                    console.log("darshil");
                                    $.ajax({
                                    cache: false,
                                    processData: false,
                                    contentType: false,
                                    type: "POST",
	   				                url: "/predict",
	   				                data: fd,
                                    success: function(response){
                                    document.getElementById("result").innerHTML = response;
                                    }
                                    })
                                    event.preventDefault();
                               }
                    </script>