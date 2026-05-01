FROM python:3.10
RUN pip install pdm
COPY . /app
RUN pdm install
CMD ["pdm", "run", "start"]
