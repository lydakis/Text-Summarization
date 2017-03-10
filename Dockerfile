FROM tensorflow/tensorflow
RUN apt-get update -qq && apt-get install -y \
  libmagickwand-dev \
  tesseract-ocr \
  tesseract-ocr-ell \
  ghostscript \
  git \
  vim
RUN pip install --upgrade pip
RUN pip install \
  wand \
  pyocr 
RUN mkdir /project
WORKDIR /project
RUN wget http://nemertes.lis.upatras.gr/jspui/bitstream/10889/10077/6/Lydakis%28ele%29.pdf
RUN wget http://nemertes.lis.upatras.gr/jspui/bitstream/10889/2639/8/Publication_Georgiou-Papadatou%5b2007%5d.pdf
RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/ell.traineddata
RUN git clone https://github.com/euske/pdfminer.git
RUN cd pdfminer && python setup.py install
