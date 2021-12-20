FROM python
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install flask_login
RUN pip install flask_wtf
RUN pip install flask_bootstrap
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  main.py /home/myapp/
COPY  api.py /home/myapp/
COPY  Users.sqlite /home/myapp/
EXPOSE 5000
CMD python3 /home/myapp/main.py
