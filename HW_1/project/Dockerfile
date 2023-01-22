FROM python:3.10-slim-buster
RUN apt-get update && apt-get install -y cifs-utils git

WORKDIR /home/OTUS-MS-23/HW_1/
COPY requirements.txt /home/OTUS-MS-23/HW_1/requirements.txt
RUN pip3 install -r requirements.txt

ARG otus_bld_ver="unknown"
RUN echo "otus build ver is ${otus_bld_ver}"
RUN git clone https://github.com/Igorigorizh/OTUS-MS-23.git
WORKDIR /home/OTUS-MS-23/HW_1/
ENV PYTHONPATH="$PYTHONPATH:./project"