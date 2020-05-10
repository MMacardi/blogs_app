$(function(){
    if(jQuery('body > main > div > div.col-md-8 > #profile:nth-child(3)').length){
        //if(jQuery('body > main > div > div.col-md-8 > #profile:nth-child(4)').length){
        //if(jQuery('body > main > div > div.col-md-8 > #profile:nth-child(5)').length){
        jQuery('body > main > div > div.col-md-8 > #profile:nth-child(5)').remove();
        //};
        jQuery('body > main > div > div.col-md-8 > #profile:nth-child(4)').remove();
    }

    else{
        // pass
    };
    if(jQuery("body > main > div > div.col-md-8 > h2#posts_by:nth-child(3)").length){
        //if(jQuery('body > main > div > div.col-md-8 > #profile:nth-child(4)').length){
        //if(jQuery('body > main > div > div.col-md-8 > #profile:nth-child(5)').length){};
        jQuery("body > main > div > div.col-md-8 > #posts_by:nth-child(6)").remove();
        jQuery("body > main > div > div.col-md-8 > #posts_by:nth-child(8)").remove();
        jQuery("body > main > div > div.col-md-8 > title:nth-child(5)").remove();
        jQuery("body > main > div > div.col-md-8 > title:nth-child(6)").remove();
    }

    else{
        // pass
    };
});
// console.log(jQuery('body > main > div > div.col-md-8 > div:nth-child(2)').length);

// document.querySelector("body > main > div > div.col-md-8 > div:nth-child(5)");
// document.querySelector("body > main > div > div.col-md-8 > div:nth-child(4)");
// document.querySelector("body > main > div > div.col-md-8 > div:nth-child(3)");
// document.querySelector("body > main > div > div.col-md-8 > h2:nth-child(6)");
// document.querySelector("body > main > div > div.col-md-8 > h2:nth-child(3)")
// document.querySelector("body > main > div > div.col-md-8 > h2:nth-child(6)")
// document.querySelector("body > main > div > div.col-md-8 > h2:nth-child(8)")