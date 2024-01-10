# Stable Diffusion

This is a very simple Stable Diffusion container to be used via the `docker-cmd` interface of Inferable.

```
docker build . --tag=diff
docker run -d diff
python3 main.py --sentence='a big blimp'
```

To run it via Inferable issue a HTTP POST request:
```bash
curl -X POST -L -v http://docker-cmd.inferable.co/diff?cmd=python3%20main.py%20--sentence=%22a%20big%20blimp%22
```