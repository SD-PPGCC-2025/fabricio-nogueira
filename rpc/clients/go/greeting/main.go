package main

import (
	"fmt"
	"nogsantos/settings"
)

func main() {
	response, err := rpc.Call(
		"say_bye",
		[]interface{}{"Mrs. Maria"},
		map[string]interface{}{},
	)

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(response.Result)
	}
}
