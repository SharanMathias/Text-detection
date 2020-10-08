# Text-Detection
<p> It is a small experimental project which has been created using python.The purpose of my project is to provide text detection on image as well as pdf. Currently it consist of three language detection i.e Hindi, Kannada and English.</p>
<ol>
  <b> Steps to use this project:</b>
  <li>Install python from <a href="https://www.python.org/downloads/">here</a></li>
  <li>Open the terminal and go to this project where it is located.</li>
  <li>
  <b>Installing Pip</b>(Pip is required in order to install additonal packages like tesseract,etc)
    <ol>
      <li>Download <a href="https://bootstrap.pypa.io/get-pip.py">get-pip.py</a> to a folder on your computer.</li>
<li>Open a command prompt and navigate to the folder containing get-pip.py.</li>
<li>Run the following command:</li>
<li>python get-pip.py</li>
<li>Pip is now installed!</li>
    </ol>
  </li>
  <li><b>Installing Packages:</b>
    <ul>
      <b>Pil</b>
      <li>python3 -m pip install --upgrade pip</li>
      <li>python3 -m pip install --upgrade Pillow</li>
    </ul>
     <ul>
       <b>Pdf2Image</b>
      <li>pip install pdf2image</li>
    </ul>
    <ul>
      <b>Pytesseract</b>
      <li>pip install pytesseract</li>
    </ul>
    <ul>
      <b>Tesseract OCR</b>
   <li><b>Windows</b><br>
        &nbsp;&nbsp;Follow the instructions from <a href="https://github.com/tesseract-ocr/tesseract/wiki#windows">here</a></li>
    <li><b>Linux</b><br>
      &nbsp;&nbsp;sudo apt install tesseract-ocr<br>
&nbsp;&nbsp;sudo apt install libtesseract-dev</li>
    </ul>
    </li>
  <li>Then copy all the files from traindata to 
  <ul>
    <li><b>For Windows:</b>C:\Program Files\Tesseract-OCR</li>
    <li><b>For Linux:</b>/usr/share/tesseract-ocr/4.00/tessdata</li>
</ul>
  </li>
  <li>Then type:<b>python3 image.py</b> in your terminal</li>
</ol>
