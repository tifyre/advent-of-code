package utils

import (
	"fmt"
	"os"
	"strconv"
	"time"
)

func parseArgs(args []string) int {
	if len(args) > 1 {
		arg := os.Args[1]
		num, err := strconv.Atoi(arg)
		if err == nil {
			return num
		}
	}
	return 1
}

func timeIt(fn func() any, n int) string {
	startTime := time.Now()
	for i := 0; i < n; i++ {
		_ = fn()
	}
	duration := time.Since(startTime) / time.Duration(n)
	return fmt.Sprintf("%v", duration)
}

func Run(solutionOne func() interface{}, solutionTwo func() interface{}, args []string) {
	partOneSolution := solutionOne()
	partTwoSolution := solutionTwo()

	n := parseArgs(os.Args)
	partOneTime := timeIt(solutionOne, n)
	partTwoTime := timeIt(solutionTwo, n)

	fmt.Printf("Part one: %v, %v\n", partOneSolution, partOneTime)
	fmt.Printf("Part two: %v, %v\n", partTwoSolution, partTwoTime)
}
