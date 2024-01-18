
FROM python:3.12
WORKDIR /app
RUN pip install Flask==2.0.1 Werkzeug==2.0.1 Jinja2==3.1.3 click==8.1.7 blinker==1.7.0 MarkupSafe==2.1.3
COPY . /app/

EXPOSE 5000

CMD ["python", "demo-app.py"]
