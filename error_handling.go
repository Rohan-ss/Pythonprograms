package main

import "math"
import "fmt"
import "errors"

func Sqrt(value float64) (float64, error) {
	if(value < 0) {
		return 0,errors.New("Negative number")
	}
	return math.Sqrt(value),nil
}
func main() {
	result,arr := Sqrt(-1)
	if (arr != nil) {
		fmt.Println(arr)
	} else {
	fmt.Println(result)
	}

	result1,arr1 := Sqrt(9)
	if (arr1 != nil) {
		fmt.Println(arr1)
	} else {
		fmt.Println(result1)
	}
}
