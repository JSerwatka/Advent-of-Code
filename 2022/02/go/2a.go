package main

import (
	"strings"
)

var winningRules = map[string]int{
	"AX": 3,
	"AY": 6,
	"AZ": 0,
	"BX": 0,
	"BY": 3,
	"BZ": 6,
	"CX": 6,
	"CY": 0,
	"CZ": 3,
}

var shapeRules = map[string]int{
	"X": 1,
	"Y": 2,
	"Z": 3,
}

func findScorePartOne(line string, score *int) {
	lineWithoutSpaces := strings.ReplaceAll(line, " ", "")
    *score += winningRules[lineWithoutSpaces]
    *score += shapeRules[string(lineWithoutSpaces[1])]
}