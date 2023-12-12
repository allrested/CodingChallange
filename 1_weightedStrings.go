package main

import (
	"encoding/json"
    "flag"
    "fmt"
    "strings"
)

func getSubstrings(s string) []string {
    substrings := []string{}
    for i := 0; i < len(s); i++ {
        for j := i + 1; j <= len(s); j++ {
            substring := s[i:j]
            if len(substring) == 1 || strings.Count(substring, string(substring[0])) == len(substring) {
                substrings = append(substrings, substring)
            }
        }
    }
    return substrings
}

func getWeight(s string) int {
    weight := 0
    for _, c := range s {
        weight += int(c - 'a' + 1)
    }
    return weight
}

func getWeights(substrings []string) map[string]int {
    weights := make(map[string]int)
    for _, s := range substrings {
        weights[s] = getWeight(s)
    }
    return weights
}

func getStatus(s string, queries []int) []string {
    status := []string{}

    substrings := getSubstrings(s)
    weights := getWeights(substrings)

    for _, q := range queries {
        found := false
        for _, w := range weights {
            if q == w {
                status = append(status, "Yes")
                found = true
                break
            }
        }
        if !found {
            status = append(status, "No")
        }
    }
    return status
}

func main() {
    var inputString string
	var queriesStr string

	flag.StringVar(&inputString, "input", "", "Input string")
	flag.StringVar(&queriesStr, "queries", "", "Comma-separated list of queries")

    flag.Parse()

	if inputString == "" || queriesStr == "" {
		fmt.Println("Usage: go run 1_weightedStrings.go -input=<inputString> -queries=<queries>")
		return
	}

	var queries []int
	if err := json.Unmarshal([]byte(queriesStr), &queries); err != nil {
		fmt.Println("Error parsing queries:", err)
		return
	}

    output := getStatus(inputString, queries)
    fmt.Println(output)
}
