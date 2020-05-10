const titleInput = document.querySelector('input[name=article_title]');
const slugInput = document.querySelector('input[name=slug]');
const textInput = document.querySelector('textarea[name=article_text]');

const slugify = val => {
    return val.toString().toLowerCase().trim()
      .replace(/&/g, '-and-')                 // replace & with '-and-'
      .replace(/[\s\W-]+/g, '-');              // replace spaces, non word characters and dashes with single dash
      //.replace(/?/g, ' ')
};

titleInput.addEventListener('keyup', () => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});


$(function() {
    /*jQuery(titleInput).on('keyup', function(){
        const val = jQuery(titleInput).val();
        jQuery(slugInput).html(slugify(val));
    }); <-- not working*/     
    jQuery(titleInput).on('keyup', () => {
        const val = jQuery(titleInput).val();
        jQuery(textInput).html(val); // .html uses only for one value in the row
    });

});















