def strrr(x: str) -> list:
    liste = []
    temp = ""
    for i in x:
        if (i != ','):
            temp += i
        else:
            liste.append(temp if str.isnumeric(temp.replace(".","0"))==False else float(temp))
            temp = ""
    return liste


if __name__ == "__main__":
    print(strrr("<0,6.0,critical/other existing credit,radio/tv,1169.0,no known savings,>=7,4.0,male single,none,4.0,real estate,67.0,none,own,2.0,skilled,1.0,yes,yes,good"))
    print(strrr("0<=X<200,48.0,existing paid,radio/tv,5951.0,<100,1<=X<4,2.0,none,2.0,real estate,22.0,none,own,1.0,skilled,1.0,none,yes,female,div/dep/mar"))
    print(strrr("no checking,12.0,existing paid,radio/tv,3059.0,>=1000,4<=X<7,2.0,none,4.0,real estate,61.0,none,own,1.0,unskilled resident,1.0,none,yes,male,div/sep,good"))
    print(strrr("0<=X<200,30.0,critical/other existing credit,new car,5234.0,<100,unemployed,4.0,none,2.0,car,28.0,none,own,2.0,high qualif/self emp/mgmt,1.0,none,yes,male,mar/wid,bad"))
    print(str.isnumeric("123.32"))

"""

['<0', '6.0', 'critical/other existing credit', 'radio/tv', '1169.0', 'no known savings', '>=7', '4.0', 'none', '4.0', 'real estate', '67.0', 'none', 'own', '2.0', 'skilled', '1.0', 'yes', 'yes','male',single']



no checking,12.0,existing paid,radio/tv,3059.0,>=1000,4<=X<7,2.0,none,4.0,real estate,61.0,none,own,1.0,unskilled resident,1.0,none,yes,male,div/sep,good
0<=X<200,30.0,critical/other existing credit,new car,5234.0,<100,unemployed,4.0,none,2.0,car,28.0,none,own,2.0,high qualif/self emp/mgmt,1.0,none,yes,male,mar/wid,bad

"""