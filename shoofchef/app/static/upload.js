Dropzone.autoDiscover = false;
$(".dropzone").dropzone({
	dictDefaultMessage: "ضع الملفات هنا لتحميلها",
	accept: function(file, done){
		done();
	},
	success: function(file, response){
		var new_image = $('<img src="./static/files/' + response.image + '">').hide();
		$('.images').prepend(new_image);
		new_image.fadeIn(999);
	}
});