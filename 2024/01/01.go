package main

import (
	utils "advent_of_code/utils"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func parse() ([]int, []int) {
	input, err := os.ReadFile("2024/01/input.txt")
	if err != nil {
		panic(err)
	}

	lefts, rights := []int{}, []int{}
	lines := strings.Split(string(input), "\n")
	for _, line := range lines {
		parts := strings.Fields(line)
		left, _ := strconv.Atoi(parts[0])
		right, _ := strconv.Atoi(parts[1])
		lefts = append(lefts, left)
		rights = append(rights, right)
	}
	sort.Ints(lefts)
	sort.Ints(rights)
	return lefts, rights
}

func count(slice []int, value int) int {
	count := 0
	for i := 0; i < len(slice); i++ {
		if slice[i] == value {
			count++
		}
	}
	return count
}

func partOne() any {
	lefts, rights := parse()
	result := 0
	for i := 0; i < len(lefts); i++ {
		result += int(math.Abs(float64(lefts[i]) - float64(rights[i])))
	}
	return result
}

func partTwo() any {
	lefts, rights := parse()
	result := 0
	for i := 0; i < len(lefts); i++ {
		result += lefts[i] * count(rights, lefts[i])
	}
	return result
}

func main() {
	utils.Run(partOne, partTwo, os.Args)
}
