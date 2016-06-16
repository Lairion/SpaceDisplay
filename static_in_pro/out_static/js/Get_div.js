jQuery(document).ready(function ($) {
    $('.spaceRow').click(description_crew);
    function description_crew() {
        $.ajax({
            type: "GET",
            url: "/shipdisplay/description_crew/",
            data:{
                'view':$(this).attr('crewman'),
            },
            dataType: "html",
            cache: false,
       });
    }
});