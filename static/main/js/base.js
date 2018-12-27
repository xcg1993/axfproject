$(document).ready(function(){
    // document.documentElement返回html dom中的root 节点 即<html>
    // innerWidth是window对象的只读属性,声明了窗口的文档显示区的宽度，以像素(px)为计量单位
    document.documentElement.style.fontSize = innerWidth / 10 + "px";
})