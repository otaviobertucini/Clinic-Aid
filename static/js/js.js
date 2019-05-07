$(document).ready(function(){

//    $( "#formularioValidation" ).validate({
//        debug: true,
//        rules:{
//            select_doctor:{
//                required: true
//            },
//            select_date:{
//                date: true,
//                required: true
//            }
//        }
//
//    });

function isDate(date){
    alert("aaaaa");
}

$(function(){
    $("button").click(function(){
        isDate("aaa");
        alert("asdnashd");
    });
});

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