import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...
def GiveChange(cH, pP): 
    cH = float(cH)
    pP = float(pP)
    value = cH-pP
    if cH == pP: 
        print("ZERO")
    elif cH < pP: 
        print("ERROR")
    else: 
        CoinDictionary = {'PENNY': .01,'NICKEL': .05,'DIME': .10,'QUARTER': .25,'HALF DOLLAR': .50,'ONE': 1.00,'TWO': 2.00,'FIVE': 5.00,'TEN': 10.00,'TWENTY': 20.00,'FIFTY': 50.00,'ONE HUNDRED': 100.00}
        print(value)
        currentChangeList = []
        def CalculateChange(totalChangeNeeded, currentChangeValue, CoinDictionary):   
            # print(currentChangeList)    
            if currentChangeValue + CoinDictionary["ONE HUNDRED"] <= totalChangeNeeded: 
                currentChangeList.append("ONE HUNDRED")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["ONE HUNDRED"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["FIFTY"] <= totalChangeNeeded: 
                currentChangeList.append("FIFTY")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["FIFTY"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["TWENTY"] <= totalChangeNeeded: 
                currentChangeList.append("TWENTY")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["TWENTY"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["TEN"] <= totalChangeNeeded: 
                currentChangeList.append("TEN")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["TEN"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["FIVE"] <= totalChangeNeeded: 
                currentChangeList.append("FIVE")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["FIVE"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["TWO"] <= totalChangeNeeded: 
                currentChangeList.append("TWO")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["TWO"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["ONE"] <= totalChangeNeeded: 
                currentChangeList.append("ONE")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["ONE"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["HALF DOLLAR"] <= totalChangeNeeded: 
                currentChangeList.append("HALF DOLLAR")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["HALF DOLLAR"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["QUARTER"] <= totalChangeNeeded: 
                currentChangeList.append("QUARTER")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["QUARTER"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["DIME"] <= totalChangeNeeded: 
                currentChangeList.append("DIME")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["DIME"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["NICKEL"] <= totalChangeNeeded: 
                print("Nickle" , currentChangeList, currentChangeValue)
                currentChangeList.append("NICKLE")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["NICKEL"], CoinDictionary)
            elif currentChangeValue + CoinDictionary["PENNY"] <= totalChangeNeeded:
                currentChangeList.append("PENNY")
                return CalculateChange(totalChangeNeeded,currentChangeValue + CoinDictionary["PENNY"], CoinDictionary)
            else: 
                # print("Finished", currentChangeList, currentChangeValue)
                return

        CalculateChange(value, 0, CoinDictionary)
        print(sorted(currentChangeList))
        return sorted(currentChangeList)
        #calculateChange()    
        
    
for line in sys.stdin:
    # print(line, end="")
    pP, cH = line.split(";")
    GiveChange(cH, pP)