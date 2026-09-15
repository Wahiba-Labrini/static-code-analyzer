document.getElementById("fileInput").addEventListener("change",function(){
    const fileInput =   document.getElementById("fileInput");
    const file=fileInput.files[0];
    document.getElementById("fileDescription").textContent=file.name;
});

document.getElementById("analyzerbtn").addEventListener("click",function(){
    const fileInput=document.getElementById("fileInput");
    const file=fileInput.files[0];

    if(!file){
        alert("Please choose a python file first")
        return;
    }

    const formData=new FormData();
    formData.append("file",file);

    fetch("http://127.0.0.1:8000/analyzer",
    {
        method:"POST",
        body:formData

    })

    .then(response => response.json())
    .then(data => {
        console.log(data);
    })

    .catch(error => {
        console.error("Error:",error);
         
    });

});

