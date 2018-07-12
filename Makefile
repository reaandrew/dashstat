AUTHOR_NAME:='Andrew Rea'
AUTHOR_EMAIL:='emailandrewrea.co.uk'

.PHONY: build
build:
	go build -o dist/dashtat -ldflags "-X main.BuildTime=`date +%s` \
			-X main.CommitHash=`git rev-parse HEAD` \
			-X main.Version=`cat VERSION`"

.PHONY: test
test:
	go test -cover
