$(window).on('keypress', function(e) {
    var key = e.key;
    // $.ajax({
    //     data :{
    //         keyboard : key
    //     },
    //     type : 'POST',
    //     url: '/postmethod'
    // }

    // );

    if(key == "a" || key == "s" || key == "d" || key == "w" || key == "k"){
        $.post("/postmethod", {
            keyboard : key
        });
    }
    
});