<?php
// tiny class for mysqli

// $ip = MySql::select('o','
// SELECT ip FROM users AS WHERE name LIKE %s AND id = %i',
// $name, $id)[0]->ip;

// MySql::update('
// 'INSERT INTO users (id,name) VALUES (null, %s)',
// $name);

class MySql {
	private static $mysqli;

	public static function connect () {
		self::$mysqli = mysqli_connect ('localhost', 'root', 'root', 'sikulix-temp');
		if (!self::$mysqli) { die ('Could not connect'); }
	}

	public static function select ($type, $q) {
		$args = array_slice (func_get_args (), 2);
		$stmt = self::binding($q, $args);
		$result = $stmt->get_result();
		$arr = array();
		if ($type == 'o') {
			while ($note = $result->fetch_object()) {
				$arr[] = $note;
			}
		} else if ($type == 'a') {
			while ($note = $result->fetch_assoc()) {
				$arr[] = $note;
			}
		}
		return $arr;
	}

	public static function update ($q) {
		$args = array_slice (func_get_args (), 1);
		self::binding($q, $args);
	}

	private static function binding ($q, $args) {
		preg_match_all("/%i|%s/", $q, $m);
		$q = preg_replace("/%i|%s/", '?', $q);
		$stmt = self::$mysqli->prepare($q);
		$m = $m[0];
		$p = "";
		$arr = array();
		foreach ($m as $k => $v) {
			$arg = $args[$k];
			if ($v == '%i') {
				$p .= 'i';
			} else if ($v == '%s') {
				$p .= 's';
			}
		}

		$arr[] = $p;
		foreach ($args as $k => $arg) {
			$arr[] = &$args[$k];
		}

		@call_user_func_array(array($stmt, 'bind_param'), $arr);
		$stmt->execute();
		return $stmt;
	}

}

MySql::connect();

?>