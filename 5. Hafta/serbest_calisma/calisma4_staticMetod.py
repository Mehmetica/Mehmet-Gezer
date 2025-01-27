#genel bir metoddur, class ile bir instance olusturmadan direk sinif ismi ile cagirabiliriz. duzenleme amacli bir metoddur

class Math:
    @staticmethod
    def add5(x):
        return x+5
    
    @staticmethod
    def add10(x):
        return x+10
    
    def pr():
        print("Run")


print(Math.add5(3))

Math.pr()