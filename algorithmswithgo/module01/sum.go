package module01

import "fmt"

// Sum will sum up all of the numbers passed
// in and return the result
func Sum(numbers []int) int {
	fmt.Println(numbers)
	if len(numbers) == 0 || numbers == nil {
		return 0
	}
	var sum int
	for _, i := range numbers {
		sum += i
	}
	return sum
}

func SumRec(numbers []int) int {
	fmt.Println(numbers)
	if len(numbers) == 0 || numbers == nil {
		return 0
	}

	// using recusion
	return numbers[0] + Sum(numbers[1:])
}
