

Hiragana = (
    ('あ','い','う','え','お'),('か','き','く','け','こ'),
    ('さ','し','す','せ','そ'),('た','ち','つ','て','と'),
    ('な','に','ぬ','ね','の'),('は','ひ','ふ','へ','ほ'),
    ('ま','み','む','め','も'),('や','','ゆ','','よ'),
    ('ら','り','る','れ','ろ'),('わ','ゐ','','ゑ','を'),'ん')
Htakuon = (
    ('が','ぎ','ぐ','げ','ご'),('ざ','じ','ず','ぜ','ぞ'),('だ','ぢ','づ','で','ど'),
    ('ば','び','ぶ','べ','ぼ'),('ぱ','ぴ','ぷ','ぺ','ぽ')
)
Katakana = (
    ('ア','イ','ウ','エ','オ'),('カ','キ','ク','ケ','コ'),
    ('サ','シ','ス','セ','ソ'),('タ','チ','ツ','テ','ト'),
    ('ナ','ニ','ヌ','ネ','ノ'),('ハ','ヒ','フ','ヘ','ホ'),
    ('マ','ミ','ム','メ','モ'),('ヤ','','ユ','','ヨ'),
    ('ラ','リ','ル','レ','ロ'),('ワ','ヰ','','ヱ','ヲ'),'ン')
Ktakuon = (
    ('ガ','ギ','グ','ゲ','ゴ'),('ザ','ジ','ズ','ゼ','ゾ'),('ダ','ヂ','ヅ','デ','ド'),
    ('バ','ビ','ブ','ベ','ボ'),('パ','ピ','プ','ペ','ポ')
)

i = []
e = []
for x in range(0,10):
    i.append(Hiragana[x][1])
    e.append(Hiragana[x][3])
for y in range(0,5):
    i.append(Htakuon[y][1])
    e.append(Htakuon[y][3])
def verbEnd(kana, target):
    z = []
    z.append(Hiragana[0]);z.append(Hiragana[1]);z.append(Htakuon[0])
    z.append(Hiragana[2]);z.append(Hiragana[3]);z.append(Hiragana[4])
    z.append(Htakuon[3]); z.append(Hiragana[6]);z.append(Hiragana[8])
    for i in range(0,len(z)):
        if kana in z[i]:
            return z[i][target]

class Verb:
    verb = ''
    group = 0
    def __init__(self, v):
        self.verb = v
        if v == 'くる' or v == 'する': self.group = 3
        elif (v[-1] == Hiragana[8][2]) and (v[-2] in e or v[-2] in i): self.group = 2
        else: self.group = 1
    def masu(self):
        ms =''
        if self.group == 3:
            if self.verb == 'くる': ms = 'き'
            elif self.verb == 'する': ms = 'し'
        elif self.group == 2: ms = self.verb.replace(self.verb[-1],'')
        else: ms = self.verb.replace(self.verb[-1],verbEnd(self.verb[-1],1))
        return ms
    def te(self):
        te = ''
        soku = [Hiragana[0][2], Hiragana[3][2], Hiragana[8][2]]
        hatsu = [Hiragana[4][2], Htakuon[3][2], Hiragana[6][2]]
        if self.group == 3:
            if self.verb == 'くる': te = 'きて'
            elif self.verb == 'する': te = 'して'
        elif self.group == 2: te = self.verb.replace('る','て')
        else:
            if self.verb[-1] == Hiragana[1][2]:
                if self.verb == 'いく':
                    te = self.verb.replace(self.verb[-1],'って')
                else: te = self.verb.replace(self.verb[-1],'いて')
            elif self.verb[-1] == Htakuon[0][2]: te = self.verb.replace(self.verb[-1],'いで')
            elif self.verb[-1] in soku: te = self.verb.replace(self.verb[-1],'って')
            elif self.verb[-1] in hatsu: te = self.verb.replace(self.verb[-1],'んで')
            else: te = self.verb.replace(self.verb[-1],'して')
        return te
    def ed(self):
        ta = ''
        soku = [Hiragana[0][2], Hiragana[3][2], Hiragana[8][2]]
        hatsu = [Hiragana[4][2], Htakuon[3][2], Hiragana[6][2]]
        if self.group == 3:
            if self.verb == 'くる': ta = 'きた'
            elif self.verb == 'する': ta = 'した'
        elif self.group == 2: ta = self.verb.replace('る','た')
        else:
            if self.verb[-1] == Hiragana[1][2]:
                if self.verb == 'いく':
                    ta = self.verb.replace(self.verb[-1],'った')
                else: ta = self.verb.replace(self.verb[-1],'いた')
            elif self.verb[-1] == Htakuon[0][2]: ta = self.verb.replace(self.verb[-1],'いだ')
            elif self.verb[-1] in soku: ta = self.verb.replace(self.verb[-1],'った')
            elif self.verb[-1] in hatsu: ta = self.verb.replace(self.verb[-1],'んだ')
            else: ta = self.verb.replace(self.verb[-1],'した')
        return ta
    def no(self):
        inverse = ''
        if self.group == 3:
            if self.verb == 'くる': inverse = 'こ'
            elif self.verb == 'する': inverse = 'し'
        elif self.group == 2:
            inverse = self.verb.replace(self.verb[-1],'')
        else:
            inverse = self.verb.replace(self.verb[-1],verbEnd(self.verb[-1],0))
        return inverse
    def can(self):
        could = ''
        if self.group == 3:
            if self.verb == 'くる': could = 'こられる'
            elif self.verb == 'する': could = 'できる'
        elif self.group == 2: could = self.verb.replace(self.verb[-1],'られる')
        else:
            could = self.verb.replace(self.verb[-1], verbEnd(self.verb[-1],3)+'る')
        return could
    def should(self):
        shd = ''
        if self.group == 3:
            if self.verb == 'くる': shd = 'こい'
            elif self.verb == 'する':
                both = ['しろ','せよ']
                #shd = both[Random(len(both))]
        elif self.group == 2:
            shd = self.verb.replace(self.verb[-1],Hiragana[8][4])
        else:
            shd = self.verb.replace(self.verb[-1],verbEnd(self.verb[-1],3))
        return shd
    def weather(self, idx):
        if idx == 0: return self.verb + Hiragana[3][4]
        elif idx == 1: return self.verb.replace(self.verb[-1],verbEnd(self.verb[-1],3)+'ば')
        elif idx == 2: return self.ed() + Hiragana[8][0]
        elif idx == 3: return self.verb + 'なら'
    def lets(self):
        lts = ''
        if self.group == 3:
            if self.verb == 'くる': lts = 'こよう'
            elif self.verb == 'する': lts = 'しよう'
        elif self.group == 2: lts = self.verb.replace(self.verb[-1], 'よう')
        else: lts = self.verb.replace(self.verb[-1], verbEnd(self.verb[-1],4)+'う')
        return lts
    def dont(self):
        return self.verb+'な'
    def passive(self):
        psv = ''
        if self.group == 3:
            if self.verb == 'くる': psv = 'こられる'
            elif self.verb == 'する': psv = 'される'
        elif self.group == 2: psv = self.verb.replace(self.verb[-1], 'られる')
        else: psv = self.verb.replace(self.verb[-1], verbEnd(self.verb[-1],0)+'れる')
        return psv
    def active(self):
        atv = ''
        if self.group == 3:
            if self.verb == 'くる': atv = 'こらせる'
            elif self.verb == 'する': atv = 'させる'
        elif self.group == 2: atv = self.verb.replace(self.verb[-1], 'させる')
        else: atv = self.verb.replace(self.verb[-1], verbEnd(self.verb[-1],0)+'せる')
        return atv
class IAdj:
    adj = ''
    def __init__(self,a):
        self.adj = a
        if self.adj == 'いい':
            self.adj = 'よい'
    def ed(self):
        e = self.adj.replace(self.adj[-1], 'かった')
        return e
    def ku(self):
        e = self.adj.replace(self.adj[-1],Hiragana[1][2])
        return e
    def kute(self):
        e = self.adj.replace(self.adj[-1],'くて')
        return e
    def verber(self):
        v = self.adj.replace(self.adj[-1], 'がる')
        return v
    def too(self):
        e = self.adj.replace(self.adj[-1], 'すぎる')
        return e
    def weather(self,idx):
        ifarray = []
        ifarray[0] = self.adj + Hiragana[3][4]
        ifarray[1] = self.adj.replace(self.adj[-1],'ければ')
        ifarray[2] = self.ed(self.adj) + Hiragana[8][0]
        ifarray[3] = self.adj + 'なら'
        return ifarray[idx]
    def noun(self):
        if self.adj == 'さむい': n = self.adj.replace(self.adj[-1], Hiragana[1][3])
        else: n = self.adj.replace(self.adj[-1], Hiragana[2][0])
        return n
class NAdj:
    adj = ''
    def __init__(self,a):
        self.adj = a
        print(self.adj)

def addon(data,k,r,m=''):
    data.append({
        'kanji':k,
        'read':r,
        'mean':m
    })

write = Verb('かく')
print(write.active())
for x in range(0,4):
    print(write.weather(x))

heavy = IAdj('おもい')
print(heavy.ed())
print(heavy.kute())