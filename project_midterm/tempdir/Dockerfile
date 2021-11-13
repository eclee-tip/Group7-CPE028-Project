FROM python
RUN pip install flask
RUN pip install flask_bootstrap
RUN pip install flask_wtf
RUN pip install flask_sqlalchemy
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  main.py /home/myapp/
EXPOSE 5000
CMD python3 /home/myapp/main.py
