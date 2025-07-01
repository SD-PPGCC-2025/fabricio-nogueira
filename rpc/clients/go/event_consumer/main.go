package main

import (
	"fmt"
	"time"
	"nogsantos/settings"
)

func main() {
	for {
		response, err := rpc.Call(
			"queue_get",
			[]interface{}{},
			map[string]interface{}{},
		)

		if err != nil {
			fmt.Printf("Erro na chamada RPC: %v\n", err)
			time.Sleep(1 * time.Second)
			continue
		}

		if response.Result != nil {
			fmt.Println(response.Result)
		}

		time.Sleep(1 * time.Second)
	}
}
