$(document).ready(function(){

$(function(){

    if($(".form_check").attr("required")){
        $(".form_check").attr("oninvalid", "this.setCustomValidity('Campo obrigatório')");
        $(".form_check").attr("oninput", "setCustomValidity('')");
    }

});

$(function(){

    $("#submit_new_patient").click(function(){

        $("#cpf_alert").attr("hidden", "true");

        var ok = 1;
        if($("#patient_cpf").val().length > 11 || $("#patient_cpf").val().length < 11){
            $("#cpf_alert").removeAttr("hidden");
            ok = 0;
        }

        if(ok == 1){
            $("#form_new_patient").submit();
        }

    });

});

});