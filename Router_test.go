package main_test

import (
    "net/http"
    "net/http/httptest"
    "testing"
    "github.com/stretchr/testify/assert"
    . "github.com/reaandrew/dashtat"
)

func TestRoutePing(t *testing.T){
  r := GetRouter()
  req, _ := http.NewRequest("GET", "/ping", nil)

  testHTTPResponse(t, r, req, func(w *httptest.ResponseRecorder) bool {
    assert.Equal(t, w.Code, http.StatusOK)

    //p, err := ioutil.ReadAll(w.Body)
    //assert.Nil(t, err)

    return true
  })
}
