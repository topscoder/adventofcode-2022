<?php

$source_file = "example.txt";

$content = file_get_contents($source_file);
$content = explode("\n", $content);

function is_cd($line) {
    return substr($line, 0, 4) == "$ cd";
}

function cd_to($line) {
    return substr($line, 5, strlen($line));
}

function is_dir_entry($line) {
    return substr($line, 0, 4) == "dir ";
}

function is_file_entry($line) {
    preg_match("/^([0-9]+) (.*?)$/", $line, $matches);

    if (count($matches) == 0) {
        return false;
    }

    return array('name' => $matches[2], 'size' => $matches[1]);
}

$structure = array();

$level = 0;
$pointer = &$structure[0];
$level_pointer = array();

foreach($content as $line) {

    if (is_cd($line)) {
        $cd_to = cd_to($line);
        if ( $cd_to == ".." ) {
            // Point to parent directory
            $level--;
            $pointer =& $level_pointer[$level];
        } else {
            $level++;
            $dirname = cd_to($line);
            $key = isset($pointer['dirs']) ? count($pointer['dirs']) + 1 : 0;
            $pointer['dirs'][$key] = array(
                'type' => 'directory',
                'name' => $dirname,
                'level' => $level,
            );

            $pointer = &$pointer['dirs'][$key];

            $level_pointer[$level] =& $pointer['dirs'][$key];
        }
    }

    if (($file_els = is_file_entry($line)) !== false) {
        $pointer['files'][] = array_merge(
            array(
                'type' => 'file',
                'level' => $level,
            ),
            $file_els,
        );
    }

    if (($dir = is_dir_entry($line)) !== false) {
        $pointer['dirs'][] = array(
            'type' => 'directory',
            'name' => $dir,
            'level' => $level,
        );
    }
}

$level = 0;

foreach($structure as $key => $value) {
    process_dirstructure($structure[$key], $level);
}

function process_dirstructure(&$structure, &$level) {
    if (isset($structure['dirs']) && count($structure['dirs']) > 0) {
        $level++;
        foreach ($structure['dirs'] as $dirnum => $dirval) {
            if (isset($dirval['type']) && $dirval['type'] == 'directory') {
                echo sprintf("%s- %s (dir)\n", str_repeat(" ", $level), $dirval['name']);
                process_dirstructure($dirval, $level);
            }
        }
    }
}