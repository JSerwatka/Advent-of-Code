package main

import (
	"strings"
)

var choosingRoles = map[string]string{
    "AX": "C",
    "AY": "A",
    "AZ": "B",
    "BX": "A",
    "BY": "B",
    "BZ": "C",
    "CX": "B",
    "CY": "C",
    "CZ": "A",
}

var scoreRules = map[string]int{
	"X": 0,
	"Y": 3,
	"Z": 6,
}

var shapeRulesTwo = map[string]int{
	"A": 1,
	"B": 2,
	"C": 3,
}


func findScorePartTwo(line string, score *int) {
	lineWithoutSpaces := strings.ReplaceAll(line, " ", "")
    chosenSchape := choosingRoles[lineWithoutSpaces]
    *score += shapeRulesTwo[chosenSchape]
    *score += scoreRules[string(lineWithoutSpaces[1])]
}