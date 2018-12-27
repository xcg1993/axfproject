$(function(){
    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")

    typediv.style.display = "none"
    sortdiv.style.display = "none"


    alltypebtn.addEventListener("click", function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)
    showsortbtn.addEventListener("click", function(){
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)
    typediv.addEventListener("click", function(){
        typediv.style.display = "none"
    },false)
    sortdiv.addEventListener("click", function(){
        sortdiv.style.display = "none"
    },false)


    var $addShopping = $(".addShopping");
    $addShopping.bind("click",function(){
        var goods_id = $(this).attr("ga");  //获取点击按钮所在行的商品ID
        $.getJSON("/addtocart/",{"goods_id":goods_id},function(data){
            if(data["status"]=="900"){
                window.open("/login/",target="_self");
            }else if(data["status"]=="200"){
                document.getElementById(goods_id).innerHTML=data["cart_num"];
            }
        });
    });


    var $subShopping = $(".subShopping");
    $subShopping.bind("click",function(){
        var goods_id = $(this).attr("ga");
        $.getJSON("/subtocart/",{"goods_id":goods_id},function(data){
            if(data["status"]=="900"){
                window.open("/login/",target="_self");
            }else if(data["status"]=="200"){
                document.getElementById(goods_id).innerHTML=data["cart_num"];
            }else if(data["status"]=="901"){
                alert(data["msg"]);
            }
        });
    });
})