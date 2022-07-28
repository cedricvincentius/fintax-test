FROM fnndsc/ubuntu-python3:18.04

COPY . /app
WORKDIR /app

# RUN pip install -r requirements.txt
# RUN cp -r -f timezone/Asia/Jakarta /etc/localtime && echo "Asia/Jakarta" > /etc/timezone && date

ENTRYPOINT ["python"]
CMD ["main.py" ]