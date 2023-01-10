<?php

function sumArray( $arr, $t ) {

    $result = [];

    foreach ( $arr as $i => $n ) {
        $diff = $t - $n;
        if ( in_array( $diff, $arr ) ) {
            $result = [ $i, array_search( $diff, $arr ) ];
            break;
        }
    }

    return $result;
}

dd( sumArray( [ 2, 7, 11, 15 ], 17 ) );

?>