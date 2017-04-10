FROM tensorflow/tensorflow
RUN apt-get update -qq && apt-get install -y \
  libmagickwand-dev \
  tesseract-ocr \
  tesseract-ocr-ell \
  ghostscript \
  git \
  vim \
  wget
RUN pip install --upgrade pip
RUN pip install \
  wand \
  pyocr
RUN mkdir /project
WORKDIR /project
RUN git clone https://github.com/euske/pdfminer.git
RUN cd pdfminer && python setup.py install
