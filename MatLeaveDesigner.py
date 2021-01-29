Germany = [1,0,14,"Germany"]
BAEI = [.6,600,8,"Brookings-AEI compromise proposal"]
Canada = [.55,428,16,"Canada",52,11.5]
Denmark = [1,698,18,"Denmark",13,120/13]
Ireland = [-1,290,26,"Ireland",52]
Italy = [.8,0,21.7,"Italy"]
Australia = [-1,534,18,"Australia",40,8.25,115000]
Austria = [1,0,16,"Austria"]
Bulgaria = [.9,401,58.6,"Bulgaria",52]
Chile = [1,0,18,"Chile",24]
CostaRica = [1,0,17.3,"Costa Rica",12]
Croatia = [1,0,30,"Croatia",52]
Czech = [.7,424,28,"Czech Republic",52]
Estonia = [1,0,20,"Estonia"]
France = [1,519.2,16,"France, first or second child"]
France2 = [1,519.2,24,"France, third or subsequent child"]
Hungary = [.7,0,24,"Hungary",52]
Israel = [1,453,15,"Israel",40]
Japan = [.67,0,14,"Japan",0,40]
Latvia = [.8,0,16,"Latvia",52]
Lithuania = [1,0,18,"Lithunia",52]
Luxembourg = [1,1041.5,20,"Luxembourg",24]
Mexico = [1,0,12,"Mexico",30]
Netherlands = [1,1263,16,"Netherlands"]
NZ = [1,383,18,"New Zealand",26,10]
Romania = [.85,0,18,"Romania",4]
Slovak = [.75,2080,34,"Slovakia",270/5] #based off US national average wage
Slovenia = [1,2080,15,"Slovenia"] #based off US national average wage
Spain = [1,1132,16,"Spain",180/5]
Switzerland = [.8,1100,16,"Switzerland",9*4]
Turkey = [.66,0,16,"Turkey",90/5]
#Iceland = [.8,1003,26,"Iceland"]
#DC = [.9,1000,8,"District of Columbia"]
California = [.55,1067,6,"California"]
NJ = [.66,524,6,"New Jersey"]
NY = [.67,1450.17*.66,12,"New York"]
RI = [.6,752,4,"Rhode Island"]
simple_countries = [Germany,BAEI,Canada,Denmark,Ireland,Italy,Australia,Austria,Bulgaria, 
                    Chile,CostaRica,Croatia,Czech,Estonia,France,France2,Hungary,Israel,
                    Japan,Latvia,Lithuania,Luxembourg,Mexico,Netherlands,NZ,Romania,Slovak,
                    Slovenia,Spain,Switzerland,Turkey,California,NJ,NY,RI]
def designer(countries):
    print("Welcome to the Maternity Leave Designer")
    e = float(input("Enter the number of weeks you have continuously worked (does not have to be for the same employer): "))
    f = float(input("Enter your average number of hours per week: "))
    a = int(input("Enter 1 if you are salaried or 2 if you are hourly: "))
    if a == 1:
        b = float(input("Enter your annual salary: "))
        b = round(b/52,2)
    elif a == 2:
        b = float(input("Enter your hourly wage: "))
        c = float(input("Enter how many hours you work per week: "))
        if c <= 40:
            b = round(b*c,2)
        else:
            d = c-40
            b = round(b*c+d*b*1.5,2)
    print("Your weekly wage is: $",b)
    print("Please select from the maternity leave frameworks below.")
    list_c = []
    for i in countries:
        n = i[3]
        list_c.append(n)
    print(list_c)
    c = input("Which country would you like to run? ")
    d = list_c.index(c)
    d = countries[d]
    name = d[3]
    length = len(d)
    weeks_worked = -1
    hours_worked = -1
    if length == 5:
        weeks_worked = d[4]
    elif length == 6:
        weeks_worked = d[4]
        hours_worked = d[5]
    elif length == 7:
        weeks_worked = d[4]
        hours_worked = d[5]
    results = set_point(d,b)
    x = results[0]
    y = results[1]
    z = results[2]
    pct = int(y/b*100)
    error = False
    if name == "Australia":
        if b*52 >= 115000:
            error = True
    if weeks_worked > -1:
        if e < weeks_worked:
            error = True
    if hours_worked > -1:
        if f < hours_worked:
            error = True
    print("In {}, your weekly benefit would be ${}, {}% of your weekly wage. You would qualify for {} weeks of maternity leave, for a total benefit of ${}.".format(name,y,pct,x,z))
    if error == True:
        print("However, due to weeks worked or minimum hours requirements, you may not be eligible to collect leave in this country.")
    return
def set_point(country,wage):
    pct = country[0]
    max = country[1]
    weeks = country[2]
    if max == 0:
        weekly_ben = pct*wage
    else:
        weekly_ben = min(pct*wage,max)
    if pct < 0:
        weekly_ben = max
    max_ben = weeks*weekly_ben
    results = [weeks,weekly_ben,max_ben]
    return results
designer(simple_countries)
