$(document).ready(function(){
    var accunt = document.getElementById("accunt");
    var tip = document.getElementById("tip");

    accunt.addEventListener("blur", function(){
        inputstr = this.value;

        $.get("/checkusername/", {"username":inputstr}, function(data){
            tip.style.color = data["color"];
            tip.innerHTML = data["msg"];
            if (data.status == "fail"){
                $("[type='submit']").prop("disabled",true); // 禁用提交按钮
            }else{
                $("[type='submit']").prop("disabled",false); // 解禁提交按钮
            }
        })
    })

})