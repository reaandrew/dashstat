package main

import (
	"log"
	"os"
	"strconv"
	"time"

	"github.com/urfave/cli"
    "github.com/gin-gonic/gin"
)

var (
    token string
    org string
)

func GetRouter() (r *gin.Engine) {
	r = gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
    return
}

func run(){
    r := GetRouter()
	r.Run()
}

func CreateApp() (app *cli.App){
	app = cli.NewApp()
	app.CustomAppHelpTemplate = AppHelpText
	app.Name = "dashtat"
	app.Usage = "Some Dashboard Views Server"
	app.Version = Version

	compileTime, _ := strconv.ParseInt(BuildTime, 10, 64)
	app.Compiled = time.Unix(compileTime, 0)
	app.Copyright = "Andrew Rea & Associates Limited 2018"
	app.Author = "Andrew Rea <email@andrewrea.co.uk>"

	app.Flags = []cli.Flag{
		cli.StringFlag{
			Name:        "github-token, t",
			Usage:       "Github Token",
			Destination: &token,
		},
		cli.StringFlag{
			Name:        "org, o",
			Usage:       "The github organisation",
			Destination: &org,
		},
	}

	app.Action = func(c *cli.Context) error {
		run()
		return nil
	}
    return
}

func main() {
    app := CreateApp()
	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}

