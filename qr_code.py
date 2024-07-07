import pyqrcode
url="https://drive.google.com/file/d/1Z3UI-0zN17qs8su3XtBalhIh1WLV1Ta4/view?usp=sharing"
img=pyqrcode.create(url)
img.svg("arshin.svg",scale=10)