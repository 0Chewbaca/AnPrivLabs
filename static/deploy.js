function deploy(){
  
    $('#formdeploy').on('submit', function(e){
        e.preventDefault();
        $.ajax({
           type: "POST",
           url: "/save/",
           data: $(this).serialize(),
           success: function() {
             alert('success');
           }
        });
    });

}

  