class Students:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths 
       

        # def calcpercentage(self):
        #     self.percentage = str((self.maths + self.chem + self.phy)/3) + "%"
        #issi kam ko krne ka ek better tarika ye h ki

    @property
    def percentage(self):
        return str((self.maths + self.chem + self.phy)/3) + "%"




stu1 = Students(98, 99, 97)
print(stu1.percentage)

#agar galtise phy marks 87 ke place pe 98 de diye to 
stu1.phy = 87
# print(stu1.phy) agar property use karenge to ye sare  extra method use krne ka NEED NHI HAI HM DIRECT ye use print(stu1.percentage) kar sakty hai 
# stu1.calcpercentage()
# print(stu1.percentage)  #ye percentage purane wale marks ke according hi dega agar property use nhi krenge to
#lekin hum property mrthod use kar liye hai to percentage as per updated marks ayega
print(stu1.percentage)