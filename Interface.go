package main

import "fmt"
import "math"



type Shape interface {
	area() float64
}
type Circle struct {
	x,y,radius float64
}

func (circle Circle) area() float64{
	return math.Pi * circle.radius * circle.radius
}
func getarea(shape Shape) float64 {
	return shape.area()
}
func main(){
	circle := Circle{x:0,y:0,radius : 3}
	fmt.Printf("Area of circle is %f",getarea(circle))
}