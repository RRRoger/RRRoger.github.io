# Golang笔记

## 1. `:=`

`:=`只能用在函数体里面, 不能作为全局变量

## 2. 声明多个变量 | 常量

```go
var x, y int = 100, 200
```

## 3. iota

> `iota`用于常量递增声明, 每一行加一

## 4. 小写字母开头的函数为私有函数

## 5. import

> import 导入 

```go
import (
	"Project1/lib"
	"Project1/lib2"
)

import (
	p1 "Project1/lib"
	p2 "Project1/lib2"
)

// 点不要轻易使用; . 是引入包里的所有东西, 不需要再去用lib2去点
import (
	p1 "Project1/lib"
	. "Project1/lib2"
)
```

## 6. 指针

```go
package main

import "fmt"

func main()  {
	var a ,b int = 10, 20
	fmt.Println("a =", a, "b =", b)
	exchangeAB(&a, &b)
	fmt.Println("a =", a, "b =", b)

	var x ,y int = 10, 20
	fmt.Println("x =", x, "y =", y)
	x, y = exchangeXY(x, y)
	fmt.Println("x =", x, "y =", y)
}

//使用指针； 这种方式不需要另外开辟内存
func exchangeAB(a, b *int) {

	fmt.Println(&*a)
	fmt.Println(&*b)

	var tmp = 0
	tmp = *a
	*a = *b
	*b = tmp
}

//不使用指针， 直接值传递， 最后再赋值
func exchangeXY(a, b int) (int, int){
	var tmp = 0
	tmp = a
	a = b
	b = tmp
	return a, b
}
```

## 7. defer: 函数最后运行

```go
package main

import "fmt"

func main(){

	// 最后执行，比return还后
	// 使用堆栈模式，先进后出，所以hahaha2先执行
	defer fmt.Println("hahaha1")
	defer fmt.Println("hahaha2")

	fmt.Println("100000")
}
```

```go
# 特殊测试

func main(){

  a := 1
  defer fmt.Println("a =", a)
  a += 1
  return a
}

# 这里打印 "a = 1"
```

## 8. 数组定义

```go
package main

import "fmt"

func main()  {
	fmt.Println(".....")

	// 固定长度
	var a [10]int
	for i:=0; i<len(a); i++{
		fmt.Println("a", a[i])
		fmt.Println("i", a[i])
	}

	// 使用range来遍历
	for _, value := range a{
		fmt.Println(value)
	}

	fmt.Println("........................")

  // 动态数组
	myArray := []int {1, 2, 3, 4}
	modifyArr(myArray)
	fmt.Println("myArray=", myArray)

}

func modifyArr(arr []int){
	arr[0] = 11111
}
```

## 9. 数组长度,容量

> 当数组长度等于容量的时候
>
> 继续追加元素
>
> 数组会新开辟一个等于当前长度的容量 即 cap(Array) = len(Array) * 2

```go
package main

import "fmt"

func main()  {
	//fmt.Println()
	// cap 容量, 容量要满的话, 继续开辟一倍的容量

	numbers := make([]int, 5)

	fmt.Printf("numbers %v len is %d, cap " +
		"is %d \n", numbers, len(numbers), cap(numbers))
	numbers = append(numbers, 1)
	fmt.Printf("numbers %v len is %d, cap " +
		"is %d \n", numbers, len(numbers), cap(numbers))

	// test defer
	defer fmt.Println("defer: numbers is ", numbers)

	numbers = append(numbers, 1)
	numbers = append(numbers, 1)
	numbers = append(numbers, 1)
	numbers = append(numbers, 1)
	numbers = append(numbers, 1)
	fmt.Printf("numbers %v len is %d, cap " +
		"is %d \n", numbers, len(numbers), cap(numbers))

	/*
		切片同python
	*/
}

```

## 10. map

> 1. 关键点: `map[string]string`
>
> 2. 如果使用函数操作, 是地址传递而不是值传递
>
> 3. cap(map) 有如下报错; "cap: 要获取map的容量，可以用len函数"
>
>    `invalid argument m (type map[string]int) for cap`

```go
package main

import "fmt"

func main() {
	var myMap1 map[string]string
	if myMap1 == nil {
		fmt.Println("myMap is null")
	}

	myMap1 = make(map[string]string, 5)

	myMap1["one"] = "java"
	myMap1["two"] = "c++"
	myMap1["three"] = "python"

	fmt.Println(myMap1)
	printMap(myMap1)

	// 删除一个key
	delete(myMap1, "two")
	printMap(myMap1)

	myMap1["for"] = "golang"
	myMap1["one"] = "c#"

	printMap(myMap1)
}

func printMap(mymap map[string]string)  {
	fmt.Println("........................")
	fmt.Println("len is", len(mymap))
	//fmt.Println("cap is", cap(mymap))
	for k, v := range mymap{
		fmt.Println(k, v)
	}
}
```

