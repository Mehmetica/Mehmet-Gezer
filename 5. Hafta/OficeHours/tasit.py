class Tasit:
    toplam_tasit_sayisi=0


    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        Tasit.toplam_tasit_sayisi+=1
        
    def tanit(self):
        print(f"marka: {self.marka}, model: {self.model}")
    

tasit1=Tasit("mercedes","c200")
tasit2=Tasit("audi","q7")

print(f"toplam tasit sayisi: {tasit1.toplam_tasit_sayisi}")