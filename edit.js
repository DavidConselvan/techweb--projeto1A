document.addEventListener("DOMContentLoaded", changeTheme = () => {
    const chosenTheme = localStorage.getItem("theme")
    
    const themeEdit = document.getElementById("ed-theme");
    if(chosenTheme.includes("/getit.css")){
        themeEdit.href = "/getit.css"
    } else{
        themeEdit.href = "/dark.css"
    }
    
})



