$(document).ready(function(){
	var $theatreAreaCodes = $("#choose_theatre");
	var $movieContainer = $("#movie_container");
	var $loader = $("#loader");
	var $advancedSearch = $('#asds');

	$movieContainer.load('/movies/'+1033+' ul', function(){
		$loader.hide();
	});

	$theatreAreaCodes.on('change', function(evt){
		var url = '/movies/'+$(this).val()+" ul";
		$movieContainer.children().remove();
		$loader.show();
		$movieContainer.load(url, function(){
			$loader.hide();
		});
	});
});
