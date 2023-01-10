<?php

function wordPattern( string $pattern, string $str ) {

    $guide = [ 'a' => 0, 'b' => 1, 'c' => 2, 'd' => 3, 'e' => 4, 'f' => 5, 'g' => 6, 'h' => 7, 'i' => 8, 'j' => 9 ];
    $words = explode( ' ', $str );
    $count_word = array_count_values( $words );
    if ( count( $words ) != strlen( $pattern ) ) {
        return false;
    }

    $result = true;
    $unique_words = array_values( array_unique( $words ) );
    $arr = str_split( $pattern );

    for ( $i = 0; $i < strlen( $pattern );
    $i++ ) {
        if ( !isset( $guide[ $arr[ $i ] ] ) ) {
            $result = false;
            break;
        }

        if ( $words[ $i ] != $unique_words[ $guide[ $arr[ $i ] ] ] ) {
            $result = false;
            break;
        }
    }
    return $result;
}

dd( wordPattern( 'abba', 'hello world world hello' ) );

?>