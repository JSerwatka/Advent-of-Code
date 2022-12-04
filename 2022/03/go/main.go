package main

import (
	"bufio"
	"log"
	"os"
)

func main() {
	total := 0
	intersection := map[string]int{}

	file, err := os.Open("../input_test.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		solution_a(scanner.Text(), intersection)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	for _, value := range intersection {
		total += value
	}
	log.Println(total)
}