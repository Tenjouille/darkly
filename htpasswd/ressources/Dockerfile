FROM ubuntu

RUN apt-get update && apt-get upgrade -y
RUN apt install git -y && apt install hashcat -y
RUN git clone https://github.com/00xBAD/kali-wordlists.git

CMD ["hashcat", "-m", "0", "437394baff5aa33daa618be47b75cb49", "kali-wordlists/rockyou.txt.gz"]