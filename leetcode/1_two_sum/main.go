package main

import "fmt"

func twoSum(nums []int, target int) []int {
	var response []int

mainLoop:
	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums); j++ {
			if j == i {
				continue
			}

			if nums[i]+nums[j] == target {
				response = append(response, i)

				response = append(response, j)

				break mainLoop
			}
		}
	}

	return response
}

func main() {
	sliceOne := []int{2, 7, 11, 15}
	fmt.Println(twoSum(sliceOne, 9))
	fmt.Println("Hello World!")
}
