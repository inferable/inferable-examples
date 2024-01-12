# Stable Diffusion

This is a very simple Stable Diffusion container to be used via the `docker-cmd` interface of Inferable.

```
docker build . --tag=diff
docker run -d diff
docker run ghcr.io/inferable/stable-diffusion:main
python3 main.py --sentence='a big blimp'
```

To run it via Inferable issue a HTTP POST request:
```bash
curl -X POST -o response.txt -L -v http://docker-cmd.inferable.farm:8080/diff?cmd=python3%20main.py%20--sentence=cat
curl -X POST -o response.txt -L -v http://docker-cmd.inferable.farm:8080/ghcr.io/inferable/stable-diffusion:main?cmd=python3%20main.py%20--sentence=cat
```

Note that the response will be of type `text/plain` and the body will include the container's stdout output and a base64 encodec image.