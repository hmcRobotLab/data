result = "cd "
for j in xrange(3):
    result += "%i_"%j
    for k in xrange(7):
        result += "%i_1"%k
        tmp = " && mkdir new && mv 0.png new/0.png"
        for i in xrange(1,12):
            tmp += " && mv %i.png new/%i.png" % (i, 12-i)
        tmp += " && rm *.png && mv new/* ./ && rmdir new"
        result += tmp
        if k != 6:
            result += " && cd ../%i_"%j
    result += " && cd ../"

print result
