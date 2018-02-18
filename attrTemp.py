import maya.cmds as mc

class AttrTemp(object):
    def __init__(self):
        self.tx = 0
        self.ty = 0
        self.tz = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.sx = 1
        self.sy = 1
        self.sz = 1
        self.r = 0.7
        self.g = 0.7
        self.b = 0.9


    #input
    def world(self, *args):
        self.r = 0.7
        self.g = 0.7
        self.b = 0.9

    def local(self, *args):
        self.r = 0.9
        self.g = 0.7
        self.b = 0.7

    def getT(self, *args):
        self.tx= mc.getAttr('.tx')
        self.ty = mc.getAttr('.ty')
        self.tz = mc.getAttr('.tz')
        mc.floatField('ftx', value=self.tx, edit=True, enable=True)
        mc.floatField('fty', value=self.ty, edit=True, enable=True)
        mc.floatField('ftz', value=self.tz, edit=True, enable=True)

    def getR(self, *args):
        self.rx = mc.getAttr('.rx')
        self.ry = mc.getAttr('.ry')
        self.rz = mc.getAttr('.rz')
        mc.floatField('frx', value=self.rx, edit=True, enable=True)
        mc.floatField('fry', value=self.ry, edit=True, enable=True)
        mc.floatField('frz', value=self.rz, edit=True, enable=True)

    def getO(self, *args):
        self.rx = mc.getAttr('.jointOrientX')
        self.ry = mc.getAttr('.jointOrientY')
        self.rz = mc.getAttr('.jointOrientZ')
        mc.floatField('frx', value=self.rx, edit=True, enable=True)
        mc.floatField('fry', value=self.ry, edit=True, enable=True)
        mc.floatField('frz', value=self.rz, edit=True, enable=True)

    def getS(self, *args):
        self.sx = mc.getAttr('.sx')
        self.sy = mc.getAttr('.sy')
        self.sz = mc.getAttr('.sz')
        mc.floatField('fsx', value=self.sx, edit=True, enable=True)
        mc.floatField('fsy', value=self.sy, edit=True, enable=True)
        mc.floatField('fsz', value=self.sz, edit=True, enable=True)

    def getReset(self, *args):
        self.tx = 0
        self.ty = 0
        self.tz = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.sx = 1
        self.sy = 1
        self.sz = 1
        mc.floatField('ftx', value=self.tx, edit=True, enable=True)
        mc.floatField('fty', value=self.ty, edit=True, enable=True)
        mc.floatField('ftz', value=self.tz, edit=True, enable=True)
        mc.floatField('frx', value=self.rx, edit=True, enable=True)
        mc.floatField('fry', value=self.ry, edit=True, enable=True)
        mc.floatField('frz', value=self.rz, edit=True, enable=True)
        mc.floatField('fsx', value=self.sx, edit=True, enable=True)
        mc.floatField('fsy', value=self.sy, edit=True, enable=True)
        mc.floatField('fsz', value=self.sz, edit=True, enable=True)

    def setAll(self, *args):
        self.setT()
        self.setR()
        self.setS()

    def setT(self, *args):
        self.tx = float(mc.floatField('ftx', q=True, value=True))
        self.ty = float(mc.floatField('fty', q=True, value=True))
        self.tz = float(mc.floatField('ftz', q=True, value=True))
        mc.setAttr('.tx', self.tx)
        mc.setAttr('.ty', self.ty)
        mc.setAttr('.tz', self.tz)

    def setR(self, *args):
        self.rx = float(mc.floatField('frx', q=True, value=True))
        self.ry = float(mc.floatField('fry', q=True, value=True))
        self.rz = float(mc.floatField('frz', q=True, value=True))
        mc.setAttr('.rx', self.rx)
        mc.setAttr('.ry', self.ry)
        mc.setAttr('.rz', self.rz)

    def setO(self, *args):
        self.rx = float(mc.floatField('frx', q=True, value=True))
        self.ry = float(mc.floatField('fry', q=True, value=True))
        self.rz = float(mc.floatField('frz', q=True, value=True))
        mc.setAttr('.jointOrientX', self.rx)
        mc.setAttr('.jointOrientY', self.ry)
        mc.setAttr('.jointOrientZ', self.rz)

    def setS(self, *args):
        self.sx = float(mc.floatField('fsx', q=True, value=True))
        self.sy = float(mc.floatField('fsy', q=True, value=True))
        self.sz = float(mc.floatField('fsz', q=True, value=True))
        mc.setAttr('.sx', self.sx)
        mc.setAttr('.sy', self.sy)
        mc.setAttr('.sz', self.sz)

    def setZero(self, *args):
        mc.setAttr('.tx', 0)
        mc.setAttr('.ty', 0)
        mc.setAttr('.tz', 0)
        mc.setAttr('.rx', 0)
        mc.setAttr('.ry', 0)
        mc.setAttr('.rz', 0)
        mc.setAttr('.sx', 1)
        mc.setAttr('.sy', 1)
        mc.setAttr('.sz', 1)

    def ui(self):
        win = mc.window(title='attrTemp', widthHeight=(390,270))
        form = mc.formLayout()

        #text
        inText = mc.text(l='inPut', h=(30))
        outText = mc.text(l='outPut', h=(30))

        #button
        world = mc.button(l='world', w=(70), h=(70), c=self.world, bgc=(0.9,0.5,0.5))
        inO = mc.button(l='orient', w=(70), h=(70), c=self.getO, bgc=(0.6,0.6,0.6))
        local = mc.button(l='local', w=(70), h=(70), c=self.local, bgc=(0.5,0.5,0.9))
        inT = mc.button(l='translate', w=(70), h=(70), c=self.getT, bgc=(self.r,self.g,self.b))
        inR = mc.button(l='rotate', w=(70), h=(70), c=self.getR, bgc=(self.r,self.g,self.b))
        inS = mc.button(l='scale', w=(70), h=(70), c=self.getS, bgc=(self.r,self.g,self.b))
        outAll = mc.button(l='all', w=(70), h=(70), c=self.setAll)
        outO = mc.button(l='orient', w=(70), h=(70), c=self.setO, bgc=(0.6,0.6,0.6))
        outZero = mc.button(l='Zero', w=(70), h=(70), c=self.setZero, bgc=(0.9,0.9,0.9))
        outT = mc.button(l='translate', w=(70), h=(70), c=self.setT)
        outR = mc.button(l='rotate', w=(70), h=(70), c=self.setR)
        outS = mc.button(l='scale', w=(70), h=(70), c=self.setS)
        resetButton = mc.button(l='reset', w=(70), h=(30), c=self.getReset, bgc=(0.9,0.9,0.9))

        #Field
        fieldTX = mc.floatField('ftx', w=(70), h=(20), value=self.tx)
        fieldTY = mc.floatField('fty', w=(70), h=(20), value=self.ty)
        fieldTZ = mc.floatField('ftz', w=(70), h=(20), value=self.tz)
        fieldRX = mc.floatField('frx', w=(70), h=(20), value=self.rx)
        fieldRY = mc.floatField('fry', w=(70), h=(20), value=self.ry)
        fieldRZ = mc.floatField('frz', w=(70), h=(20), value=self.rz)
        fieldSX = mc.floatField('fsx', w=(70), h=(20), value=self.sx)
        fieldSY = mc.floatField('fsy', w=(70), h=(20), value=self.sy)
        fieldSZ = mc.floatField('fsz', w=(70), h=(20), value=self.sz)


        #inPut layout
        mc.formLayout(form, edit=True, attachForm=[
            (inText,'top',5),(inText,'left',70),
            (world,'top',40),(world,'left',10),
            (inO,'top',115),(inO,'left',10),
            (local,'top',190),(local,'left',10),
            (inT,'top',40),(inT,'left',85),
            (inR,'top',115),(inR,'left',85),
            (inS,'top',190),(inS,'left',85)
        ])
        #field layout
        mc.formLayout(form, edit=True, attachForm=[
            (fieldTX,'top',40),(fieldTX,'left',160),
            (fieldTY,'top',65),(fieldTY,'left',160),
            (fieldTZ,'top',90),(fieldTZ,'left',160),
            (fieldRX,'top',115),(fieldRX,'left',160),
            (fieldRY,'top',140),(fieldRY,'left',160),
            (fieldRZ,'top',165),(fieldRZ,'left',160),
            (fieldSX,'top',190),(fieldSX,'left',160),
            (fieldSY,'top',215),(fieldSY,'left',160),
            (fieldSZ,'top',240),(fieldSZ,'left',160),
        ])
        #outPut layout
        mc.formLayout(form, edit=True, attachForm=[
            (outText,'top',5),(outText,'left',290),
            (outAll,'top',40),(outAll,'left',310),
            (outO,'top',115),(outO,'left',310),
            (outZero,'top',190),(outZero,'left',310),
            (outT,'top',40),(outT,'left',235),
            (outR,'top',115),(outR,'left',235),
            (outS,'top',190),(outS,'left',235)
        ])
        #resetButton layout
        mc.formLayout(form, edit=True, attachForm=[(resetButton,'top',5),(resetButton,'left',160)])
        mc.showWindow(win)

a = AttrTemp()
a.ui()
