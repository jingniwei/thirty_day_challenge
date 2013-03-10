start= 6*60*60+52*60 # TIME IN SECONDS 
run = 8*60+15 + 3*(7*60 + 12) + 8*60+15
endtime = start+run
endhour= endtime/3600
endmin= (endtime%3600)/60
endsec= (endtime%3600)%60

print (str(endhour)+":" + str(endmin) + ":" + str(endsec))
