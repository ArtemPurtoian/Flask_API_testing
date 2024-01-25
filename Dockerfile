FROM python

WORKDIR /Flask_API_testing

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

 CMD ["pytest"]