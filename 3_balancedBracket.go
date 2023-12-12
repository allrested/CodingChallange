package main

import (
	"flag"
	"fmt"
)

func isBalanced(s string) string {
	stack := make([]rune, 0)

	bracketPairs := map[rune]rune{
		'}': '{',
		']': '[',
		')': '(',
	}

	for _, char := range s {
		if isOpeningBracket(char) {
			stack = append(stack, char)
		} else if isClosingBracket(char) {
			if len(stack) == 0 || stack[len(stack)-1] != bracketPairs[char] {
				return "NO"
			}
			stack = stack[:len(stack)-1]
		}
	}

	if len(stack) == 0 {
		return "YES"
	}

	return "NO"
}

func isOpeningBracket(char rune) bool {
	return char == '{' || char == '[' || char == '('
}

func isClosingBracket(char rune) bool {
	return char == '}' || char == ']' || char == ')'
}

func main() {
	var inputString string

	flag.StringVar(&inputString, "input", "", "Input string")
	flag.Parse()

	if inputString == "" {
		fmt.Println("Usage: go run 3_balancedBracket.go -input=<inputString>")
		return
	}

	result := isBalanced(inputString)
	fmt.Println(result)
}