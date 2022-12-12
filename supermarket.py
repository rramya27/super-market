#supermarket
print("-----super market-----")
print(" ")
tot1=0
tot2=0
tot3=0
tot4=0
i=1
while(i<=5):
    i=i+1
    count1=0
    count2=0
    count3=0
    print(" 1.Vegies and fruits \n 2.Grocery \n 3.snacks ")
    choice=int(input("Enter the products:"))
    if(choice==1):
        print("1.Vegies \n 2.fruits")
        print(" ")
        vf=int(input("Enter the category:"))
        if(vf==1):
            print("VEGTABLES")
            print("1 onion 2 carrot 3 beetroot ")
            i=1
            while(i<=3):
                i=i+1
                veg=int(input("Enter the vegtables:"))
                print(" ")
                while(veg<=3):
                    if(veg==1):
                        print("***ONION-->RATE=50***")
                        kg=int(input("Enter the no of kg:"))
                        if(kg<=10):
                            count1=50*kg
                            print("The amount of onion:",count1)
                            print(" ")
                            if(count1>kg):
                                break
                    elif(veg==2):
                        print("***CARROT->RATE=70***")
                        kg=int(input("Enter the no of kg:"))
                        if(kg<=10):
                            count2=70*kg
                            print("Amount of carrot:",count2)
                            print(" ")
                            if(count2>kg):
                                break
                    elif(veg==3):
                        print("***beetroot->RATE=50***")
                        kg=int(input("Enter the no of kg:"))
                        if(kg<=10):
                            count3=50*kg
                            print("Amount od beetroot:",count3)
                            print(" ")
                            if(count3>kg):
                                break
                else:
                    print("None of the choice")
                    break
            tot1=count1+count2+count3
            print("--------------------------------")
            print("the total amount of vegies=",tot1)
            print("--------------------------------")
            
        elif(vf==2):
            print("FRUITS")
            print("1.APPLE 2.KIWI 3.GRAPS")
            print(" ")
            i=1
            while(i<=3):
                i=i+1
                fruits=int(input("Enter the fruits:"))
                print(" ")
                while(fruits<=3):
                    if(fruits==1):
                        print("***APPLE-->RATE=50***")
                        kg=int(input("Enter the no of kg:"))
                        if(kg<=10):
                            count1=50*kg
                            print("Amount of Apple:",count1)
                            print(" ")
                            if(count1>kg):
                                break
                    elif(fruits==2):
                        print("***KIWI-->RATE=250***")
                        kg=int(input("Enter the no of kg:"))
                        if(kg<=10):
                            count2=250*kg
                            print("Amount of kiwi:",count2)
                            print(" ")
                            if(count2>kg):
                                break
                    elif(fruits==3):
                        print("***GRAPS-->RATE=150***")
                        kg=int(input("Enter the no of kg:"))
                        if(kg<=10):
                            count3=150*kg
                            print("Amount of graps:",count3)
                            print(" ")
                            if(count3>kg):
                                break
                else:
                    print("none of the choice")
                    break
            tot2=count1+count2+count3
            print("--------------------------------")
            print("the total amount of fruits=",tot2)
            print("--------------------------------")
            
    elif(choice==2):
        print("GROCERY")
        print("1 Rice 2 Wheat 3 Grains")
        print(" ")
        i=1
        while(i<=3):
            i=i+1
            gro=int(input("Enter the choices:"))
            print(" ")
            while(gro<=3):
                if(gro==1):
                    print("***Rice--> RATE=500***")
                    pack=int(input("Enter the no of packs:"))
                    if(pack<=10):
                        count1=500*pack
                        print("Amount of Rice:",count1)
                        print(" ")
                        if(count1>pack):
                            break
                elif(gro==2):
                    print("***Wheat--> RATE=300***")
                    pack=int(input("Enter the no of packs:"))
                    if(pack<=10):
                        count2=300*pack
                        print("Amount of wheat:",count2)
                        print(" ")
                        if(count2>pack):
                            break
                elif(gro==3):
                    print("***Grains--> RATE=450***")
                    packs=int(input("Enter the no of packs:"))
                    if(packs<=10):
                        count3=450*packs
                        print("Amount of grains:",count3)
                        if(count3>packs):
                            break
            else:
                print("none of the choice")
                break
        tot3=count1+count2+count3
        print("--------------------------------")
        print("the total amount of grocery=",tot3)
        print("--------------------------------")
            
    elif(choice==3):
        print("SNACKS")
        print("1 BISCUITS 2 CHOCOLATES 3 ICE CREAMS")
        print(" ")
        i=1
        while(i<=3):
            i=i+1
            snacks=int(input("Enter the choices:"))
            print(" ")
            while(snacks<=3):
                if(snacks==1):
                    print("***BISCUITS--> RATE=10***")
                    packs=int(input("Enter the no of packs:"))
                    if(packs<=10):
                        count1=10*packs
                        print("Amount of biscuits:",count1)
                        print(" ")
                        if(count1>packs):
                            break
                elif(snacks==2):
                    print("***CHOCOLATS --> RATE=150***")
                    cho=int(input("Enter the no of chocos:"))
                    if(cho<=10):
                        count2=150*cho
                        print("Amount of chocolates:",count2)
                        print(" ")
                        if(count2>cho):
                            break
                elif(snacks==3):
                    print("***ICE CREAMS-->RATE=90***")
                    cream=int(input("Enter the cups of ice cream:"))
                    if(cream<=10):
                        count3=90*cream
                        print("The total amount:",count3)
                        print(" ")
                        if(count3>cream):
                            break
            else:
                print("None of the choice")
                break
        tot4=count1+count2+count3
        print("--------------------------------")
        print("the total amount of snacks=",tot4)
        print("--------------------------------")
    else:
        print("None of the chioce")
        break
        
total=tot1+tot2+tot3+tot4
print("==================================")
print("Totally you have purchased:",total)
print("==================================")
print("*****THANK YOU *****""\t *****VISIT AGAIN*****")
            
    


