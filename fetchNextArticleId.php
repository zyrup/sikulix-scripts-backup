<?php

require_once 'sql.php';

$articleId = MySql::select('o',"
	SELECT * FROM `random-check-deleted-products` WHERE status LIKE 'todo' LIMIT 1",
$name, $id)[0];

echo $articleId->articleId . ' random';