package main

import (
	"fmt"
	"time"
	"math/rand"
	"nogsantos/settings"
)

func main() {
	for {
		response, err := rpc.Call(
			"update_counter",
			[]interface{}{},
			map[string]interface{}{},
		)
		if err != nil {
			fmt.Println(err)
		} else {
			fmt.Println(response)
		}

		r := rand.Intn(10)
		time.Sleep(time.Duration(r) * time.Second)
	}
}
