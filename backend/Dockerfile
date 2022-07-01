FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY /api/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
COPY /api/ /backend/api/
CMD ["python3", "flask", "run"]