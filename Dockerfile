FROM python:2.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./check_safety.py" ]
