from datetime import datetime, timedelta

def eklenme_tarihi():
    eklenme_tarihi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return eklenme_tarihi

def iade_tarihi():
    iade_tarihi = (datetime.now() + timedelta(weeks=2)).strftime("%Y-%m-%d %H:%M:%S")
    return iade_tarihi

        

