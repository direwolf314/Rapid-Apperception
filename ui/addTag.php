<?php

$keyword = urldecode($_POST["keyword"]);
$tag = urldecode($_POST["tag"]);
$extension = urldecode($_POST["extension"]);
$project = urldecode($_POST["project"]);

chdir("tagger");

echo "Adding tag...";
$command = "/usr/bin/python add_keyword.py " . $extension . " " . $keyword . " " . $tag;
$command = escapeshellcmd($command) . ' 2>&1';
$output = exec($command, $blah);

echo "Re-parsing project";
$command = "/usr/bin/python run.py " . $project;
$command = escapeshellcmd($command) . ' 2>&1';
$output = exec($command, $blah);

echo "Tagger finished!";

?>
