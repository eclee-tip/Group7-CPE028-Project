FROM python
RUN pip install flask
RUN pip install firebase
RUN pip install python-jwt
RUN pip install gcloud
RUN pip install sseclient
RUN pip install pycrypto
RUN pip install requests-toolbelt
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  main.py /home/myapp/
EXPOSE 5000
CMD python3 /home/myapp/main.py
