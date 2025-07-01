package rpc

import (
	"encoding/json"
	"net"
)

type RPCRequest struct {
	Func   string        `json:"func"`
	Args   []interface{} `json:"args"`
	Kwargs map[string]interface{} `json:"kwargs"`
}

type RPCResponse struct {
	Result interface{} `json:"result"`
	Error  string      `json:"error"`
}

func Call(
		function string,
		args []interface{},
		kwargs map[string]interface{},
	) (*RPCResponse, error) {

	conn, err := net.Dial("tcp", "127.0.0.1:5000")
	if err != nil {
		return nil, err
	}
	defer conn.Close()

	request := RPCRequest{
		Func:   function,
		Args:   args,
		Kwargs: kwargs,
	}

	reqData, err := json.Marshal(request)
	if err != nil {
		return nil, err
	}

	_, err = conn.Write(reqData)
	if err != nil {
		return nil, err
	}

	buffer := make([]byte, 4096)
	n, err := conn.Read(buffer)
	if err != nil {
		return nil, err
	}

	var response RPCResponse
	err = json.Unmarshal(buffer[:n], &response)
	if err != nil {
		return nil, err
	}

	return &response, nil
}
