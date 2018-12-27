$(function(){
   $('#payBtn').click(function(){

       var order_id=$(this).attr('ga')
       $.getJSON('/pay/',{'order_id':order_id},function(data) {
           if(data['status']=='200'){
               alert(data['msg']);
               window.open('/mine/',target="_self");

           }

       })

   })
})