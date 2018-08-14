$('#carousel-example-generic').carousel({
	interval : 3000,
 	pause : 'hover',
 	wrap : true,
});
$('#cycle').on('click', function () {
	$('#carousel-example-generic').carousel('cycle');
});

$('#pause').on('click', function () {
	$('#carousel-example-generic').carousel('pause');
});

$('#number').on('click', function () {
	$('#carousel-example-generic').carousel(2);
});

$('#prev').on('click', function () {
	$('#carousel-example-generic').carousel('prev');
});

$('#next').on('click', function () {
	$('#carousel-example-generic').carousel('next');
});
const ap = new APlayer({
	container: document.getElementById('aplayer'),
	mini: true,
	fixed: true,
	autoplay: true,
	theme: '#FADFA3',
	loop: 'all',
	preload: 'auto',
	volume: 0.7,
	mutex: true,
	listFolded: true,
	audio: [
		{
			name: 'Try',
	        artist: 'Asher Book',
	        url: 'static/music/g.mp3',
	        theme: '#505d6b',
            cover: 'static/img/try.jpg',
		}
	]
});