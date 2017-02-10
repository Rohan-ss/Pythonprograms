package main

import (
	"fmt"
)
func main(){
	var a int =10
	var ip * int
	ip = &a
	fmt.Println("Variable %d",a)
	fmt.Printf("Address of variable %x \n",&a)
	fmt.Printf("Address store in ip variable %x \n",ip)
	fmt.Printf("Value of *ip variable %d \n",*ip)
}