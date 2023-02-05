FROM python:3.10-slim
RUN apt-get update && apt-get install -y git

WORKDIR /home/Otus
COPY requirements.txt /home/Otus/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

RUN git clone  --depth 1 --filter=blob:none --sparse https://github.com/Igorigorizh/OTUS-MS-23;
WORKDIR /home/Otus/OTUS-MS-23/

RUN git sparse-checkout set -- HW_2
WORKDIR /home/Otus/OTUS-MS-23/HW_2

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
