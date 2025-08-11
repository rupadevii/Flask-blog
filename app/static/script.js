const toggleBtn = document.getElementById("theme-toggle")

function setThemeIcon(theme){
    toggleBtn.textContent = theme === 'dark' ? "🌙":"🌞";
}

function toggleTheme(){
    document.body.classList.toggle('dark-mode');
    const theme = document.body.classList.contains("dark-mode") ? "dark" : "light";
    localStorage.setItem("theme", theme);
    setThemeIcon(theme);
}

// window.onload = function (){
//     const savedTheme = localStorage.getItem("theme");
//     if( savedTheme === "dark"){
//         document.body.classList.add("dark-mode");
//     }else{
//         document.body.classList.remove("dark-mode")
//     }
//     setThemeIcon(savedTheme || "light");

//     toggleBtn.addEventListener("click", toggleTheme)
// }

window.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");
    if( savedTheme === "dark"){
        document.body.classList.add("dark-mode");
    }else{
        document.body.classList.remove("dark-mode")
    }
    setThemeIcon(savedTheme || "light");

    toggleBtn.addEventListener("click", toggleTheme)
})

setTimeout(function() {
    let alert = document.querySelector(".alert");
    if (alert) alert.style.display = "none";
  }, 3000); // hides after 3 seconds

