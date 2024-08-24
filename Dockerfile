FROM python:3.9

WORKDIR /server

COPY requirements.txt /server

ARG LIBRARY="-i https://pypi.tuna.tsinghua.edu.cn/simple"

RUN pip install -r requirements.txt ${LIBRARY}

COPY . /server

ARG PORT=8000

ENV PORT=${PORT} WORKERS=4

EXPOSE ${PORT}

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT --workers $WORKERS"]