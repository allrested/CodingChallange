<?php

function charExist( $arr ) {

    $charCounts = array_map(function ($string) {
        $counts = array_count_values(str_split($string));
        ksort($counts);
        return $counts;
    }, $arr);
    
    $result = array_reduce($charCounts, function ($result, $counts) {
        if (!$result) {
            return $counts;
        }
        return array_intersect_assoc($result, $counts);
    }, null);

    return count($result);
}

dd( charExist( [ 'abcdde', 'baccd', 'eeabg' ] ) );

?>