package main

import "fmt"

// ListNode Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1, l2 *ListNode) *ListNode {
	result := ListNode{}
	var carry int = 0
	var nextNode *ListNode
	var started bool

	for {
		var currentL1Node int
		var currentL2Node int

		if l1 != nil {
			currentL1Node = l1.Val
			l1 = l1.Next
		}

		if l2 != nil {
			currentL2Node = l2.Val
			l2 = l2.Next
		}

		sum := currentL1Node + currentL2Node + carry

		if sum > 9 {
			carry = 1
			sum = sum - 10
		} else {
			carry = 0
		}

		if result.Val == 0 && result.Next == nil && !started {
			result.Val = sum
			nextNode = &result
			started = true

			continue
		}

		if carry == 0 && sum == 0 && l1 == nil && l2 == nil {
			break
		}

		nextNode.Next = &ListNode{
			Val: sum,
		}

		nextNode = nextNode.Next

		if l1 == nil && l2 == nil && carry == 0 {
			break
		}
	}

	return &result
}

func main() {
	l1 := ListNode{
		Val: 2,
		Next: &ListNode{
			Val: 4,
			Next: &ListNode{
				Val:  3,
				Next: nil,
			},
		},
	}

	l2 := ListNode{
		Val: 5,
		Next: &ListNode{
			Val: 6,
			Next: &ListNode{
				Val:  4,
				Next: nil,
			},
		},
	}

	l3 := ListNode{
		Val: 0,
	}

	l4 := ListNode{
		Val: 0,
	}

	l5 := ListNode{
		Val: 9,
		Next: &ListNode{
			Val: 9,
			Next: &ListNode{
				Val: 9,
				Next: &ListNode{
					Val: 9,
					Next: &ListNode{
						Val: 9,
						Next: &ListNode{
							Val: 9,
							Next: &ListNode{
								Val: 9,
							},
						},
					},
				},
			},
		},
	}

	l6 := ListNode{
		Val: 9,
		Next: &ListNode{
			Val: 9,
			Next: &ListNode{
				Val: 9,
				Next: &ListNode{
					Val: 9,
				},
			},
		},
	}

	result := addTwoNumbers(&l1, &l2)
	fmt.Println(result)

	result2 := addTwoNumbers(&l3, &l4)
	fmt.Println(result2)

	result3 := addTwoNumbers(&l5, &l6)
	fmt.Println(result3)

	fmt.Println("==================")
	temp := result3
	for {
		fmt.Println(temp.Val)

		temp = temp.Next

		if temp == nil {
			break
		}
	}
	fmt.Println("==================")

	fmt.Println("Hello " + "World!")
}
