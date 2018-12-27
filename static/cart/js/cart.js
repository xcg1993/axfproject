$(function(){

    $("button.addShopping").click(function(){
        var goods_id=$(this).attr("ga");
        $.getJSON("/addtocart/",{"goods_id":goods_id},function(data){
           $('span#totalPrice').html(data['totalPrice']);
            if(data["status"]=="200"){
                document.getElementById(goods_id).innerHTML=data["cart_num"];
            }if(data["status"]=="900"){
                window.open("/login/",target="_self");
            }
        });
    });


    $('button.subShopping').click(function(){
      var goods_id=$(this).attr('ga');
      var $current_subttn=$(this)
      $.getJSON("/subtocart/",{"goods_id":goods_id},function(data){
          $('span#totalPrice').html(data['totalPrice']);
          if (data['status']=='200'){
              if (data['cart_num']==0){
                  $current_subttn.parents('li.menuList').css('display','none');
                  if($('span#totalPrice').html().trim()=='0'){
                    $('div#selectall').children('span').children('span').html('');
                  }
              }else{
                document.getElementById(goods_id).innerHTML=data['cart_num'];
                }
          }if(data["status"]=="900"){
                window.open("/login/",target="_self");
            }
         });
    });







    $("span.ischose").click(function(){
        var $outer_span = $(this);
        var cartid = $outer_span.parents("li.menuList").attr("cartid");
        $.getJSON("/changeselect/",{"cartid":cartid},function(data){
            // alert(data['totalPrice'])
            $('span#totalPrice').html(data['totalPrice']);

            if (data['ischoose']){
                $outer_span.children('span').html("√");
            }else{
                $outer_span.children('span').html("");
            }
            if(data['select_all_flag']){
                $('div#selectall').children('span').children('span').html('√')
            }else{
               $('div#selectall').children('span').children('span').html('')
            }
        });

    });

    $('div#selectall').click(function(){
        var $select_all=$(this).children('span').children('span')
        var is_select=$select_all.html().trim()==""?false:true;
        $.getJSON('/changeselectall/',{'hope_status':!is_select},function(data){
                $('span#totalPrice').html(data['totalPrice']);
                if(data['is_select']=='true'){
                    $('span.ischose').children('span').html('√')
                    $select_all.html('√')
                }else{
                    $('span.ischose').children('span').html('')
                    $select_all.html('')
                }

        })

    })

  $('span#ok').click(function(){
      $.getJSON('/makeorders/',function(data) {
          if(data['status']=='900'){
              window.open('/login/',target="_self")
          }
          if(data['status']=='200'){
              var orderid=data['orderid']
              window.open('/orderdetail/?order_id='+orderid,target="_self")
          }
          if(data['status']=='902'){
              alert('购物车中没有任何商品，请先添加')
          }
      })

  })
});