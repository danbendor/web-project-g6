

var x =document.getElementById("lop");
var count =0;


function createorderproduct(){


    count = count + 1;
    var x =document.getElementById("numproduct").value;

    if(count == x)
    {
        window.location.replace("orderManagement.html")
    }
    else
    {
        document.getElementById("quantity").value  = "";
        document.getElementById("product1").value  = "";
        document.getElementById("Size").value  = "";
        document.getElementById("cloth").value  = "";
        document.getElementById("Price").value  = "";
        document.getElementById("subject").value  = "";
        document.getElementById("lop").innerHTML = " enter deatils for product "  + (count+1);
}
}