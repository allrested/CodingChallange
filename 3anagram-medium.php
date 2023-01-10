<?php

function anagram( $a, $b ) {

    $aChars = count_chars( $a, 1 );
    $bChars = count_chars( $b, 1 );

    return $aChars === $bChars;
}

dd( anagram( 'anagram', 'nagaram' ) );

?>