function addEvent(el, type, handler) {
	if (el.attachEvent) el.attachEvent('on'+type, handler); else el.addEventListener(type, handler);
}

function postAjax(url, data, success) {
	var params = typeof data == 'string' ? data : Object.keys(data).map(
		function(k){ return encodeURIComponent(k) + '=' + encodeURIComponent(data[k]) }
	).join('&');

	var xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");
	xhr.open('POST', url);
	xhr.onreadystatechange = function() {
		if (xhr.readyState>3 && xhr.status==200) { success(xhr.responseText); }
	};
	xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);
	return xhr;
}

// example request with data object
// postAjax('http://foo.bar/', { p1: 1, p2: 'Hello World' }, function(data){ console.log(data); });

App = {
	init: function() {
		// [].forEach.call(document.querySelectorAll('#run'), function(item, i) {
		// 	addEvent(item, 'click', function() {
		// 		run();
		// 	});
		// });
	}
}

var run = function () {
	// postAjax('run.php', 'r=1', function(data){
	// 	// console.log(data);
	// });
}

var fetchNextArticleId = function () {
	postAjax('fetchNextArticleId2.php', 'r=1', function(data){
		prompt('', 'http://random.local/de/node/'+data+'/edit');
	});
}

var setNextArticleId404 = function () {
	postAjax('setNextArticleId404.php', 'r=1', function(data){
	});
}
var setNextNodeIdDone = function () {
	postAjax('setNextNodeIdDone.php', 'r=1', function(data){
	});
}

var setNextArticleIdError = function () {
	postAjax('setNextArticleIdError.php', 'r=1', function(data){
	});
}
var setNextNodeIdError = function () {
	postAjax('setNextNodeIdError.php', 'r=1', function(data){
	});
}

var decideWhatToDo = function (val) {
	if (val == 'Edit Random Item') {
		setNextNodeIdDone();
	} else {
		setNextNodeIdError();
	}
}

window.onload = function () {
	// JSON.parse(jsonString);
	App.init();
}