package main

import (
	"bufio"
	"log"
	"os"
)

func main() {
    score := 0
    file, err := os.Open("../input.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        findScorePartTwo(scanner.Text(), &score)
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    println("Score is", score)
}