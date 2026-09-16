document.getElementById("fileInput").addEventListener("change",function(){
    const fileInput =   document.getElementById("fileInput");
    const file=fileInput.files[0];
    document.getElementById("fileDescription").textContent=file.name;
});

document.getElementById("analyzerbtn").addEventListener("click",function(){
    const fileInput=document.getElementById("fileInput");
    const file=fileInput.files[0];
    
    if (!file) {
        alert("Please upload a file first.");
        return;
    }

    if(!file.name.endsWith(".py")){
        alert("Please upload a Python (.py) file only")
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
        console.log("DATA SUCESSFLY RECEUIVED",data)
        const  res=document.getElementById("results");
        const resultsTitle=document.getElementById("resultsTitle");
        resultsTitle.style.display="block";

        let resHtml=`<h3>${data.filename}</h3>`;

        if(data.total_issue==0){
            resHtml +=` <div class="success-message"> ✅ No security issues found !</div>`;
        }else{
            let scoreColor;
            if(data.score>=70) scoreColor ="linear-gradient(135deg,#2cecc71,#27ae60)";
            else if(data.score>=40) scoreColor ="linear-gradient(135deg,#f4a261,#e67e22)"
            else scoreColor ="linear-gradient(135deg,#e63946,#c0392b)"
            resHtml+=`<div class="score-circle" style="background:${scoreColor}">${data.score}/100</div>`
            resHtml+=`<p>Total issues: ${data.total_issue}</p>`;

            data.issue.forEach(issue => {
                resHtml+=`<div class="issue-card">
                        <span class="info-box box-line">Line ${issue.line}</span> 
                        <span class="info-box box-rule"> ${issue.rule_id} </span> 
                        <span class="info-box box-severity">${issue.severity}</span>
                        <span class="info-box box-message">${issue.message}</span>
                </div>`; 
            });
        }
        res.innerHTML=resHtml;
    })

    .catch(error => {
        console.error("Error:",error);
         
    });

});








