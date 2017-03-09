<?php

require_once 'sql.php';

$nodeId = MySql::select('o',"
	SELECT * FROM `random-check-nodes` WHERE status LIKE 'todo' LIMIT 1",
$name, $id)[0];

echo $nodeId->nodeId;