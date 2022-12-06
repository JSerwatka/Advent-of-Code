package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func findTop3Calories() []int {
	readFile, err := os.Open("../input.txt")
	singleElfTotal := 0
	totalSlice := []int{}

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		currentLine := fileScanner.Text()
		if currentLine == "" {
			totalSlice = append(totalSlice, singleElfTotal)
			singleElfTotal = 0
		} else {
			currentLineValue, _ := strconv.Atoi(currentLine)
			singleElfTotal += currentLineValue
		}
	}

	readFile.Close()
	sort.Slice(totalSlice, func(i int, j int) bool { return totalSlice[i] > totalSlice[j] })
	return totalSlice[:3]
}

func one_b() {
	top3CaloriesSum := 0
	totalArray := findTop3Calories()

	for _, value := range totalArray {
		top3CaloriesSum += value
	}

	fmt.Println(top3CaloriesSum) // 200158
}
