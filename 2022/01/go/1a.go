package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func ona_a() {
	readFile, err := os.Open("../input.txt")
	total := 0
	highestTotal := 0

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		currentLine := fileScanner.Text()
		if currentLine == "" {
			if total > highestTotal {
				highestTotal = total
			}
			total = 0
		} else {
			currentLineValue, _ := strconv.Atoi(currentLine)
			total += currentLineValue
		}
	}

	readFile.Close()
	fmt.Println(highestTotal)
}
