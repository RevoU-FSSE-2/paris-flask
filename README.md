## how to build and run in docker

### BUILD
```bash
docker build -t flask-revou:latest .
```

### RUN
```bash
docker run -p 5000:8000 -it --rm --name flask-api flask-revou:latest
```