<?php
if( isset($_POST['tag_name']) && $_POST['tag_name'] !== '' && $_POST['tag_name'] !== 'Search tags') {
    $_POST['tag_name'] = urldecode($_POST['tag_name']);
    echo '<script type="text/javascript">this.stored_tag_name = "';
    echo $_POST['tag_name'] . '";';
    echo '</script>'; 
}
//echo "post tag name is: " . $_POST['tag_name'];

include('main.html');

?>
