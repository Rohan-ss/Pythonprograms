package main

import "fmt"

type books struct {
	 tittle string
	 author string
	 name string
	 cost int
}
func main() {
	var book1 books
	var book2 books

	book1.tittle = "You can win"
	book1.author = "shiv kheda"
	book1.name = "You can win"
	book1.cost = 200

	book2.tittle = "The secret"
	book2.author = "Bob jodge"
	book2.name = "The secret"
	book2.cost = 500

	printbook(book1)
	fmt.Print("------------------\n")
	printbook(book2)

}
func printbook(book books){
	fmt.Printf("Tiitle of the book %s \n",book.tittle)
	fmt.Printf("Tiitle of the book %s \n",book.author)
	fmt.Printf("Tiitle of the book %s \n",book.name)
	fmt.Printf("Tiitle of the book %d \n",book.cost)

}
