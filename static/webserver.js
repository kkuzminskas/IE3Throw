$(window).on('keypress', function(e) {
    var key = e.key;
    $.ajax({
        data :{
            keyboard : key
        },
        type : 'POST',
        url: '/postmethod'
    }

    );
    // $.post("/postmethod", {
    //     keyboard : key
    // });

    switch(key){
        case "a":
            alert("go left");
            break;
        case "s":
            alert("go backward");
            break;
        case "w":
            alert("go forward");
            break;
        case "d":
            alert("go right");
            break;
    }
});