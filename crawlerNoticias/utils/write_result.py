from datetime import datetime

def write_result_to_txt(path,result,crawler_name="none"):
    filename = "spider_{}_{}.txt".format(crawler_name,datetime.now().strftime('%d-%m-%Y'))
    path_to_file = "{}/{}".format(path,filename)

    file = open(path_to_file,'w+')
    for counter,item in enumerate(result):
        print("{0}/{1}".format(counter+1,len(result)))
        file.write("\n#Item {}\n".format(counter))
        for key in item.keys():
            file.write("{}: \t{}\n".format(key,str(item[key])) )
    file.close()
