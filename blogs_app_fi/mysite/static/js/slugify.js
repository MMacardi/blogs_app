let titleInput = document.querySelector('input[name=article_title]');//('#id_article_title');
let slugInput = document.querySelector('input[name=slug]');//('#id_slug');
let textInput = document.querySelector("textarea[name=article_text]");//('#id_article_text');

const slugify = val => {
    return val.toString().toLowerCase().trim()
      .replace(/&/g, '-and-')                 // replace & with '-and-'
      // .replace(/[а-яА-ЯЁё]-/g, '-')
      .replace(/[\s\!\`\~\@\"\№\;\:\?\,\#\$\%\^\&\*\(\)\_\+\{\|\}\:\"\?\>\<\\,\.\/\;\[\]\-\=\㋛\ソ\ッ\ヅ\ツ\ゾ\シ\ジ\ｯ\ﾂ\ｼ\ﾝ\〴\☺\☻\☹\☜\☞\☝\☟\✍\☺\☹\☻\😁\😂\😃\😆\😇\😈\😉\😊\😋\😌\😍\😎\😏\😐\😒\🚤\😓\😔\😖\😘\😚\😜\😝\😞\😠\😡\😢\😣\😤\😥\😨\😩\😪\😫\😭\😰\🌏\🍀\😱\😲\😳\😵\😶\😷\😸\😹\😺\😻\😼\😽\😾\😿\🙀\🙅\🙆\🙇\🙈\🙉\🙊\🙋\🙌\🙍\🙎\✋\✋\🐲\👀\🐝\💢\☘\✌\∞\©\🐾\💋\👣\🚗\☠\🚀\🚃\🚄\🚅\🚇\🚉\🚌\🚏\🚑\🚒\🚓\🚕\😄\😅\🚙\🚚\🚢]/g, '-')
      .replace(/[\а\А]/g, 'a')
      .replace(/[\б\Б]/g, 'b')
      .replace(/[\в\В]/g, 'v')
      .replace(/[\г\Г]/g, 'g')
      .replace(/[\д\Д]/g, 'd')
      .replace(/[\е\Е]/g, 'e')
      .replace(/[\ё\Ё]/g, 'e')
      .replace(/[\ж\Ж]/g, 'zh')
      .replace(/[\з\З]/g, 'z')
      .replace(/[\и\И]/g, 'i')
      .replace(/[\й\Й]/g, 'i')
      .replace(/[\к\К]/g, 'k')
      .replace(/[\л\Л]/g, 'l')
      .replace(/[\м\М]/g, 'm')
      .replace(/[\н\Н]/g, 'n')
      .replace(/[\о\О]/g, 'o')
      .replace(/[\п\П]/g, 'p')
      .replace(/[\р\Р]/g, 'r')
      .replace(/[\с\С]/g, 's')
      .replace(/[\т\Т]/g, 't')
      .replace(/[\у\У]/g, 'u')
      .replace(/[\ф\Ф]/g, 'f')
      .replace(/[\х\Х]/g, 'kh')
      .replace(/[\ц\Ц]/g, 'ts')
      .replace(/[\ч\Ч]/g, 'ch')
      .replace(/[\ш\Ш]/g, 'sh')
      .replace(/[\щ\Щ]/g, 'shch')
      .replace(/[\ъ\Ъ]/g, 'ie')
      .replace(/[\ы\Ы]/g, 'y')
      .replace(/[\ь\Ь]/g, '')
      .replace(/[\э\Э]/g, 'e')
      .replace(/[\ю\Ю]/g, 'iu')
      .replace(/[\я\Я]/g, 'ia');
                         
       
                           
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
    $(titleInput).on('keyup', () => {
        const val = jQuery(titleInput).val();
        // $(slugInput).html(slugify(val)) 
        $(textInput).html(val); // .html uses only for one value in the row
    });

});















