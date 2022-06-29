#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="konrad.bachusz"

WORKDIR /usr/app/src

COPY requirements.txt ./
RUN pip install -r requirements.txt


#to COPY the remote file at working directory in container
COPY app.py ./
COPY utils.py ./

EXPOSE 8501

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "streamlit", "run", "app.py"]