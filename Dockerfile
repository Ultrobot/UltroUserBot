FROM erdembey/epicuserbot:latest 
RUN git clone https://github.com/UltroBot/UltroUserBot /root/UltroUserBot
WORKDIR /root/UltroUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
