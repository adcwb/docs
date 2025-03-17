

### 调用golang转化时区时报错

>Golang Error: missing Location in call to Time.In
>
>```go
>location, _ := time.LoadLocation("Europe/Amsterdam")
>
>name, offset := time.Now().In(location).Zone()
>
>log.Println("name: "+name, "offset: "+strconv.Itoa(offset))
>
>
>panic: time: missing Location in call to Time.In
>
>goroutine 1 [running]:
>time.Time.In(...)
>        /usr/local/go/src/time/time.go:1146
>main.main()
>        /app/main.go:16 +0x1c5
>```



异常原因

>LoadLocation returns the Location with the given name.
>
>If the name is "" or "UTC", LoadLocation returns UTC. If the name is "Local", LoadLocation returns Local.
>
>Otherwise, the name is taken to be a location name corresponding to a file in the IANA Time Zone database, such as "America/New_York".
>
>LoadLocation looks for the IANA Time Zone database in the following locations in order:
>
>- the directory or uncompressed zip file named by the ZONEINFO environment variable
>- on a Unix system, the system standard installation location
>- $GOROOT/lib/time/zoneinfo.zip
>- the time/tzdata package, if it was imported



解决

解决方案是在 Docker 构建步骤中添加时区信息。

Go 运行时会检查几个位置以获取时区信息。您可以在[Golang LoadLocation 文档](https://pkg.go.dev/time@go1.22.0#LoadLocation)中阅读有关确切行为的更多信息 。基本上，有 4 个位置按顺序进行检查：

- ZONEINFO 环境变量指定的目录或未压缩的 zip 文件
- 在 Unix 系统上，系统标准安装位置
- $GOROOT/lib/time/zoneinfo.zip
- time/tzdata 包（如果已导入）



示例

```dockerfile
# Build stage
FROM golang:1.22 as builder

# Install musl-dev and gcc for Alpine compatibility
RUN apt-get update && apt-get install -y musl-dev musl-tools gcc

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy go.mod and go.sum files
COPY go.mod go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source code into the container
COPY . .

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o application .

## Final stage
FROM alpine:latest as final

## Install necessary packages, e.g. ca-certificates, if your application needs it
RUN apk --no-cache add ca-certificates

WORKDIR /app

## Copy the pre-built binary file from the previous stage
COPY --from=builder /app/application /app/application
COPY --from=builder /usr/local/go/lib/time/zoneinfo.zip /
ENV ZONEINFO=/zoneinfo.zip

CMD ["/app/application"]

```



证书错误

>
>
>busybox:latest 