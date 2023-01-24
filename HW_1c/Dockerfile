FROM python:3.10-slim-buster
RUN apt-get update && apt-get install -y cifs-utils git

WORKDIR /home/Otus
COPY requirements.txt /home/Otus/requirements.txt
RUN pip3 install -r requirements.txt

ARG otus_bld_ver="unknown"
RUN echo "otus build ver is ${otus_bld_ver}"
RUN git clone  --depth 1 --filter=blob:none --sparse https://github.com/Igorigorizh/OTUS-MS-23;
WORKDIR /home/Otus/OTUS-MS-23/
git sparse-checkout set -- HW_1c
WORKDIR /home/Otus/OTUS-MS-23/HW_1c
ENV PYTHONPATH="$PYTHONPATH:./app"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]