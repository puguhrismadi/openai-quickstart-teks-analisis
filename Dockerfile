FROM python:3.10
ADD app.py .
RUN pip install -r requirements.txt .
CMD [ "flask",'run' ]