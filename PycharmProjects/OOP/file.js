/**
 * Created by Dave on 2016/3/3.
 */
//文档中每个元素都是一个对象
//getElementById方法返回一个与那个有着给定id属性值的元素节点对应的对象
//alert(document.getElementById("purchases"));
//alert(document.getElementsByTagName("li").length);
//item = document.getElementsByTagName("li");
//for (var i =0; i <item.length; i++){
//    alert(typeof item[i]);
//}

//item = document.getElementsByTagName("*");
//for(i=0; i<item.length;i++){
//    alert(item[i]);
//}

//shopping = document.getElementById("purchases");
//item = shopping.getElementsByTagName("*");
//for(i=0; i<item.length;i++) {
//    alert(item[i]);
//}

//alert(document.getElementsByClassName("sale").length);

parse = document.getElementsByTagName("p");
for(var i = 0; i < parse.length; i++){
    text = parse[i].getAttribute("title");
    if(text != null){
        parse[i].setAttribute("title", "a list of goods");
        alert(parse[i].getAttribute("title"));
    }
}


