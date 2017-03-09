<?php

require_once 'sql.php';

MySql::update(
"UPDATE `random-check-deleted-products` SET status = 'error'
	WHERE id IN (
		SELECT id FROM (
		SELECT id FROM `random-check-deleted-products`
		WHERE status LIKE 'todo'
		LIMIT %i
	) tmp
);", 1);
