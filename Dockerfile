FROM python:3.10
COPY . .
RUN pip install fastapi uvicorn
RUN pip install fastapi uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
