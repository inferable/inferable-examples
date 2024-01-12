FROM python AS model
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs
RUN git lfs install
RUN git clone https://huggingface.co/OFA-Sys/small-stable-diffusion-v0 /tmp/model
RUN rm -rf /tmp/model/.git

FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && \
    apt-get -y install curl bash tar wget gpg sed

#install cuda
RUN curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

RUN sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list

RUN apt-get update
# Install deps including python and nvidia-container-toolkit
RUN apt-get install -y git python3 python3-pip --fix-missing nvidia-container-toolkit


RUN distribution=$(. /etc/os-release;echo $ID$VERSION_ID | sed -e 's/\.//g') && cd /tmp && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb 
RUN apt-get update 
RUN apt-get -y install cuda-drivers

WORKDIR /diffusion

COPY --from=model /tmp/model /diffusion/model
COPY ./requirements.txt /diffusion/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /diffusion/requirements.txt

COPY . .

CMD tail -f /dev/null