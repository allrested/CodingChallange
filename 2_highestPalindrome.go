package main

import (
	"flag"
	"fmt"
)

func makePalindrome(num string, k int) string {
	if k < 0 {
		return "-1"
	}

	// If the given string is already a palindrome, no need for replacements
	if isPalindrome(num) {
		return num
	}

	// Convert the string to a rune slice to allow modifications
	runes := []rune(num)

	// Call the recursive function to perform replacements
	makePalindromeRecursive(runes, 0, len(runes)-1, k)

	return string(runes)
}

func makePalindromeRecursive(runes []rune, start, end, k int) {
	// Base case: if we have traversed the entire string or used up all replacements, return
	if start >= end || k == 0 {
		return
	}

	// If the characters at the current positions are different, replace the smaller one with the larger one
	if runes[start] != runes[end] {
		if runes[start] < runes[end] {
			runes[start] = runes[end]
		} else {
			runes[end] = runes[start]
		}
		k-- // Reduce the number of replacements available
	}

	// Recursively process the next pair of characters
	makePalindromeRecursive(runes, start+1, end-1, k)
}

func isPalindrome(num string) bool {
	return num == getReverse(num)
}

func getReverse(num string) string {
	if len(num) == 0 {
		return ""
	}
	return string(num[len(num)-1]) + getReverse(num[:len(num)-1])
}

func main() {
	var inputString string
	var k int

	flag.StringVar(&inputString, "input", "", "Input string")
	flag.IntVar(&k, "k", -1, "Integer maximum character replacement")

	flag.Parse()

	if inputString == "" || k == -1 {
		fmt.Println("Usage: go run 2_highestPalindrome.go -input=<inputString> -k=<inputInteger>")
		return
	}

	result := makePalindrome(inputString, k)
	fmt.Println(result)
}