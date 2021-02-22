  
/*--This JS is taken from the link below and if an embedded Mailchimp form--*/
/*--https://mailchimp.com/help/add-a-signup-form-to-your-website/--*/

function($) {
    window.fnames = new Array(); 
    window.ftypes = new Array();
    fnames[6]='TITLE';
    ftypes[6]='text';
    fnames[1]='FNAME';
    ftypes[1]='text';
    fnames[2]='SNAME';
    ftypes[2]='text';
    fnames[8]='KNAME';
    ftypes[8]='text';
    fnames[3]='ADDRESS';
    ftypes[3]='address';
    fnames[0]='EMAIL';
    ftypes[0]='email';
    fnames[7]='MOBILE';
    ftypes[7]='phone';
    fnames[4]='PHONE';
    ftypes[4]='phone';
    fnames[5]='DOB';
    ftypes[5]='date';
    fnames[9]='DJP';
    ftypes[9]='date';
    fnames[10]='DRP';
    ftypes[10]='date';
    fnames[11]='PRN';
    ftypes[11]='number';
    fnames[12]='PENSION';
    ftypes[12]='number';
    fnames[13]='SHIST';
    ftypes[13]='text';
    fnames[14]='KINNAME';
    ftypes[14]='text';
    fnames[16]='RELATION';
    ftypes[16]='text';
    fnames[19]='KINEMAIL';
    ftypes[19]='text';
    fnames[18]='KINTEL';
    ftypes[18]='phone';
    fnames[17]='KINADDRESS';
    ftypes[17]='text';
} (jQuery);

var $mcj = jQuery.noConflict(true);