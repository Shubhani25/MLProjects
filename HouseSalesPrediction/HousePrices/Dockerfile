FROM windows10

MAINTAINER Shubhani Mulay "shubhani.mulay25@gmail.com"

RUN pip install python3
    python3 -m pip install --upagrade pip

ADD ./requirements.txt /
RUN python3 -m pip install -r requirements.txt

ADD ./prediction.py /
ADD ./ server.py /
ADD ./ kc_house_data.csv /
CMD [ "python3", "-u", "./server.py" ]
