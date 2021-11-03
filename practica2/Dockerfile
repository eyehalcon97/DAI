# Dockerfile
FROM python:3.9-alpine

WORKDIR /app  
# directorio dentro del contenedor para el código
COPY . /app
RUN pip install -r requirements.txt
        
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development        
        
CMD ["flask", "run"]