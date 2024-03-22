import csv
fp = open("answers.csv","w+")
writer = csv.writer(fp)
ans=["A","B","B","C","B","C","A","B","C","A"]
writer.writerows(ans)
fp.close()
