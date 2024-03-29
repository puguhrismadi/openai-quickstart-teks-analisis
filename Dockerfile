FROM python:3.12.0b3-slim-bullseye
RUN pip install --no-cache-dir matplotlib pandas

RUN mkdir /code
COPY . /code
COPY requirements.txt /code
WORKDIR /code
ENV OPENAI_API_KEY=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

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
EXPOSE 5005
CMD ["flask", "run", "--host", "0.0.0.0"]
