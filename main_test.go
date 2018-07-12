package main_test

import (
    "testing"
    "github.com/stretchr/testify/assert"
    . "github.com/reaandrew/dashtat"
)

func TestCreateApp(t *testing.T){
    app := CreateApp()

    assert.Equal(t, app.Name, AppName)
    assert.Equal(t, app.Usage, AppUsage)
}
