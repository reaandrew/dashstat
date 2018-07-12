package main_test

import (
    "os"
    "testing"
    "github.com/gin-gonic/gin"
    "github.com/stretchr/testify/assert"
    . "github.com/reaandrew/dashtat"
)

func TestMain(m *testing.M) {
  //Set Gin to Test Mode
  gin.SetMode(gin.TestMode)

  // Run the other tests
  os.Exit(m.Run())
}

func TestCreateApp(t *testing.T){
    app := CreateApp()

    assert.Equal(t, app.Name, AppName)
    assert.Equal(t, app.Usage, AppUsage)
}
