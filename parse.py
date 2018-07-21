import csv
import re

from bs4 import BeautifulSoup

maxms = 0.07
mvar = 100
var = 0
avg = 0
count = 0
mult = 2
csvfile = 'output.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["Sector","Event","Time in MS"])
    
    with open("workerpool_profile-35.html") as fp:
        parse = BeautifulSoup(fp, "html.parser")

        for rect in parse.find_all('rect'):
            
            text = str(rect.find('title').string)
            lines = text.splitlines()
            SectorMS = ""
            Sectornum = ""
            Sectorissue = ""
            for line in lines:
                ms = re.search('(.+?) ms$', line)
                ms2 = re.search('Long pause of (.+?) ms$', line)
                Sector = re.search(r"[^[]*\[([^]]*)\]", line)
                issue = re.search('\](.+?)$', line)


                if Sector:
                    Sectornum = Sector.group(1)

                if ms2:
                    SectorMS = ms2.group(1)
                    var = float(var) + float(SectorMS)
                    count = count +1
                else:
                    if ms:
                        SectorMS = ms.group(1)
                        var = float(var) + float(SectorMS)
                        count = count +1
                    
                if issue:
                    Sectorissue = issue.group(1)  
        avg = (var / count) * mult
        print(avg)            
        for rect in parse.find_all('rect'):
            
            text = str(rect.find('title').string)
            lines = text.splitlines()
            SectorMS = ""
            Sectornum = ""
            Sectorissue = ""
            for line in lines:
                ms = re.search('(.+?) ms$', line)
                ms2 = re.search('Long pause of (.+?) ms$', line)
                Sector = re.search(r"[^[]*\[([^]]*)\]", line)
                issue = re.search('\](.+?)$', line)


                if Sector:
                    Sectornum = Sector.group(1)

                if ms2:
                    SectorMS = ms2.group(1)
                    var = float(var) + float(SectorMS)
                    count = count +1
                else:
                    if ms:
                        SectorMS = ms.group(1)
                        var = float(var) + float(SectorMS)
                        count = count +1
                    
                if issue:
                    Sectorissue = issue.group(1)
            if float(SectorMS) >= maxms:
                writer.writerow([Sectornum,Sectorissue,SectorMS])



            #if mvar < 1:
            #    break
            #mvar = mvar - 1
