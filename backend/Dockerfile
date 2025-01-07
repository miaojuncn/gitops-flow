FROM registry.cn-hangzhou.aliyuncs.com/mj-mirror/python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .
RUN chmod +x start.sh

CMD [ "./start.sh" ]