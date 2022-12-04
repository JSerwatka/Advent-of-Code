package main

import (
	"strings"
)

func createHalves(rucksack string) (string, string) {
	var half_len int = len(rucksack) / 2
	return rucksack[:half_len], rucksack[half_len:]
}

func findIntersection(firstHalf string, secondHalf string, intersection map[string]int) {
	for _, letter := range firstHalf {
		letter_str := string(letter)

		if strings.Contains(secondHalf, letter_str) {
			if _, exists := intersection[letter_str]; !exists {
				intersection[letter_str] = calculateItemPriority(letter_str)
			}
		}
	}
}

func calculateItemPriority(letter string) int {
	letter_rune := []rune(letter)[0]
	if strings.ToLower(letter) == letter {
		return  int(letter_rune - 'a') + 1
	}
	return int(letter_rune - 'A') + 27
}

func solution_a(rucksack string, intersection map[string]int){

	first_half, second_half := createHalves(rucksack)
	findIntersection(first_half, second_half, intersection)
}