<?php

require_once 'sql.php';

MySql::update(
"UPDATE `random-check-nodes` SET status = 'done'
	WHERE id IN (
		SELECT id FROM (
		SELECT id FROM `random-check-nodes`
		WHERE status LIKE 'todo'
		LIMIT %i
	) tmp
);", 1);
