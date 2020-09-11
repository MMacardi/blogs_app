// let btn = document.getElementById("theme-button");
// let link = document.getElementById("theme-link");

// btn.addEventListener("click", function () { ChangeTheme(); });

// function ChangeTheme()
// {
//     let lightTheme = "{% static 'assets/main.css' %}";
//     let darkTheme = "{% static 'assets/dark.css' %}";

//     let currTheme = link.getAttribute("href");
//     let theme = "";

//     if(currTheme == lightTheme)
//     {
//    	 currTheme = darkTheme;
//         theme = "dark";
//         $(btn).html("☀️")
//     }
//     else
//     {    
//    	 currTheme = lightTheme;
//         theme = "light";
//         $(btn).html("🌙")
//     }

//     link.setAttribute("href", currTheme);

// }

// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}

// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-dark');
    } else {
        setTheme('theme-light');
    }
})();