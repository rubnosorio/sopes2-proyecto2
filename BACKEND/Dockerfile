FROM ubuntu:18.04 
RUN apt update
RUN apt install python3 python3-pip sqlite3 nano -y
ADD . /webApp_RPA
WORKDIR /webApp_RPA
RUN pip3 install Flask
RUN pip3 install pymongo
RUN pip3 install pymongo[srv]
RUN pip3 install -U python-dotenv
RUN chmod 777 run.sh
CMD sh ./run.sh
EXPOSE 80
