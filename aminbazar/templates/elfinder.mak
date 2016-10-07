<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>elFinder 2.0</title>

		<!-- <link rel="stylesheet" type="text/css" href="${tg.url('/lib/jquery-ui/css/ui-lightness/jquery-ui-1.10.4.min.css')}">
		<script src="${tg.url('/lib/jquery-ui/js/jquery-1.10.2.js')}"></script>
		<script src="${tg.url('/lib/jquery-ui/js/jquery-ui-1.10.4.min.js')}"></script> -->

		<link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.23/themes/smoothness/jquery-ui.css">
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
		<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.23/jquery-ui.min.js"></script>

		<link rel="stylesheet" type="text/css" href="${tg.url('/contrib/elfinder/css/elfinder.min.css')}">
		<link rel="stylesheet" type="text/css" href="${tg.url('/contrib/elfinder/css/theme.css')}" >
		<script src="${tg.url('/contrib/tiny_mce/tiny_mce_popup.js')}"></script>
		<script src="${tg.url('/contrib/elfinder/js/elfinder.min.js')}"></script>
		<script src="${tg.url('/contrib/elfinder/js/i18n/elfinder.ru.js')}"></script>
		<script type="text/javascript" charset="utf-8">
			var FileBrowserDialogue = {
				init : function() {
					// Here goes your code for setting your custom things onLoad.
				},
				mySubmit : function(URL) {
					var win = tinyMCEPopup.getWindowArg('window');

					// pass selected file path to TinyMCE
					win.document.getElementById(tinyMCEPopup.getWindowArg('input')).value = URL;

					// are we an image browser?
					if ( typeof (win.ImageDialog) != 'undefined') {
						// update image dimensions
						if (win.ImageDialog.getImageData) {
							win.ImageDialog.getImageData();
						}
						// update preview if necessary
						if (win.ImageDialog.showPreviewImage) {
							win.ImageDialog.showPreviewImage(URL);
						}
					}

					// close popup window
					tinyMCEPopup.close();
				}
			}

			tinyMCEPopup.onInit.add(FileBrowserDialogue.init, FileBrowserDialogue);

			$().ready(function() {
				var elf = $('#elfinder').elfinder({
					// set your elFinder options here
					url : '/elfinderphp/connector.php', // connector URL
					getFileCallback : function(file) {// editor callback
						FileBrowserDialogue.mySubmit(file.url);
						// pass selected file path to TinyMCE
					}
				}).elfinder('instance');
			});

		</script>
	</head>
	<body>

		<!-- Element where elFinder will be created (REQUIRED) -->
		<div id="elfinder"></div>

	</body>
</html>
