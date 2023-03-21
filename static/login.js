document.getElementById("photo1").addEventListener("click",function(){
    document.getElementById("photo1").style.border = "2px solid blue";
    document.getElementById("photo2").style.border = "none";
    document.getElementById("message").innerText = "Hii Doctor, How Can I help you";
})
document.getElementById("photo2").addEventListener("click",function(){
    document.getElementById("photo2").style.border = "2px solid blue";
    document.getElementById("photo1").style.border = "none";
    document.getElementById("message").innerText = "Hii , How can I help you";
})