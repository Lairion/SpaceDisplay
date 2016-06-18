jQuery(document).ready(function ($) {
    $('.navbutton').click(change_window);
    function change_window() {
        $.ajax({
            type: "GET",
            url: "/shipdisplay/desktop/",
            data:{
                'view':$(this).attr('data-tooltip'),
            },
            dataType: "html",
            cache: false,
       });
    $('.spaceRow').click(description_crewman);
    function description_crewman() {
        $.ajax({
            type:"GET",
            ur
        })
    }    
    }
});