FROM python AS model
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs
RUN git lfs install
RUN git clone https://huggingface.co/OFA-Sys/small-stable-diffusion-v0 /tmp/model
RUN rm -rf /tmp/model/.git

FROM python:3.10-slim

WORKDIR /stable-diffusion

COPY --from=model /tmp/model /stable-diffusion/model
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 -c "from diffusers import DiffusionPipeline; pipeline = DiffusionPipeline.from_pretrained(\"./model\")"

EXPOSE 80

CMD ["python3", "main.py"]