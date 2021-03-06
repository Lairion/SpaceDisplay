$(document).ready(function($){
	$( ".navbutton" ).click(function() {
		$(".statusBar").text("");
		$title = $(this).attr("data-tooltip");
		$(".statusBar").append("<span class='spanBar'>"+$title+"</span>");
        $.ajax({
            type: "GET",
            url: "/shipdisplay/crew/",
            data:{
                'view':$(this).attr('data-tooltip'),
            },
            dataType: "html",
            success: function(response){
                location.reload();
            }
       });

	});
	$("[data-tooltip]").mousemove(function (eventObject) {

        $data_tooltip = $(this).attr("data-tooltip");
        
        $("#tooltip").text($data_tooltip)
                     .css({ 
                         "top" : eventObject.pageY + 5,
                        "left" : eventObject.pageX + 5
                     })
                     .show();

    }).mouseout(function () {

        $("#tooltip").hide()
                     .text("")
                     .css({
                         "top" : 0,
                        "left" : 0
                     });
    });
});