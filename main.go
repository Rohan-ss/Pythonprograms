package main

import "fmt"

func main() {
	var x float64 =20.02
	y := 15
	z := 25
	f,g := "Rohan","Dhiraj"
	fmt.Println(x)
	fmt.Println(y)
	fmt.Printf("x is a type of %T",x)
	fmt.Printf("Y is a type of %T",y)
	fmt.Print("\n------------------------------\n\n")

	var a,b,c = 3,4,"foo"

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Printf("a is a type of %T \n",a)
	fmt.Printf("b is a type of %T \n",b)
	fmt.Printf("c is a type of %T \n",c)

	var res int
	res = max(y,z)
	fmt.Println("max number is\t",res)
	fmt.Println(swap(f,g))
}

func swap(x,y string) (string,string) {
	return y,x
}


func max(num1, num2 int) int {
	var result int

	if (num1 > num2) {
		result = num1
	} else {
		result = num2
	}
	return result
}