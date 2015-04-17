<?php

$project = urldecode($_POST["project"]);

chdir("tagger");

echo "Re-parsing project";
$command = "/usr/bin/python run.py " . $project;
$command = escapeshellcmd($command) . ' 2>&1';
$output = exec($command, $blah);

echo "Tagger finished!";

?>
