win.show()

 workdir = " "

 def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endwith(ext)
            result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def ShowFilenamesList():
    extensions = ['.jpg','.jpeg','.png','.gif','.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)

    Im_files.clear()
    for filename in filenames:
        Iw_files.addItem(filename)

btn_dir.clicked.connect(ShowFilenamesList)

class ImageProcessar():
    def __init__(self)
    self.image = None
    self.dir = None 
    self.filename = None
    self.save_dir = 'Modifield/'

    def loadImage(self, filename):
        '''під час завантаження запам'ятовуємо шлях та ім'я файлу'''
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)

    def saveImage(self):
        '''зберігає копію файла у підпапці'''
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exicts(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname =os.path.join(path, self.filename)
