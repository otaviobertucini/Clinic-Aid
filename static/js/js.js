$(document).ready(function(){

$(function(){

    if($(".form_check").attr("required")){
        $(".form_check").attr("oninvalid", "this.setCustomValidity('Campo obrigatório')");
        $(".form_check").attr("oninput", "setCustomValidity('')");
    }

});

//$("#doc_selection").validate({
//    debug: true,
//    rules:{
//        select_doctor:{
//            required: true
//        },
//        select_date:{
//            required: true
//        }
//    },
//    messages:{
//        select_date:{
//            accept: "Campo obrigatório!"
//        }
//    }
//});

//function isDate(date){
//    alert("aaaaa");
//}
//
//$(function(){
//    $("button").click(function(){
//        isDate("aaa");
//    });
//});

//    $(function() {
//
//        $('#submit_doc_selection').bind('click', function(){
//
//            var txtVal =  $('#select_date').val();
//
//            if(isDate(txtVal))
//                alert('Valid Date');
//            else
//                alert('Invalid Date');
//        });
//
//    });


});