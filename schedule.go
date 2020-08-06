package main

import (
    "log"
    "net/http"
    "os"
    "fmt"
  "strings"
  "net/url"
  "math/rand"
  "time"
  "encoding/json"
  "github.com/jasonlvhit/gocron"
)

func main() {
  fmt.Println("running schedule")

    s := gocron.NewScheduler()
    //s.Every(1).Week().Do(task)
    s.Every(1).Day().At("19:30:59").Do(taskStop)
    s.Every(1).Day().At("6:30:59").Do(taskStop)
    s.Every(10).Second().Do(taskTest)
    <- s.Start()
}

func taskTest() {
    fmt.Println("I am running task.")
    t := time.Now()
    fmt.Println(t)
}

func taskStop() {

  url := "http://0.0.0.0:5000/api/OIC/stop"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))

}

func taskStart() {

  url := "http://0.0.0.0:5000/api/OIC/stop"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))

}