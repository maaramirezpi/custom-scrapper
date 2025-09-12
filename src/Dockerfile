FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --upgrade

COPY . .

RUN apt-get update
RUN mkdir -p /var/lib/apt/lists/partial
RUN apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1 libglx-mesa0
RUN apt -y --force-yes install libu2f-udev fonts-liberation libasound2  libatk-bridge2.0-0 libatk1.0-0  libatspi2.0-0  libcairo2 libcups2 libdrm2 libgbm1 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 libxcomposite1 libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 xdg-utils
RUN apt -y --force-yes install wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt install -f


# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "python", "anon-scrapper.py" ]