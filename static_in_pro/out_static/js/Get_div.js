jQuery(document).ready(function ($) {
    $('.view').click(changeView);
    function changeView() {
        $.ajax({
            type: "GET",
            url: "/app/change_view/",
            data:{
                'view':$(this).attr('data-tooltip'),
            },
            dataType: "html",
            cache: false,
            
       });
    }
});