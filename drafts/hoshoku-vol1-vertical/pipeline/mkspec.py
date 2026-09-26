import json
C={'3a':[0,355,1856,2304],'3b':[0,547,1792,2400],'3c':[0,0,1149,2400],'3e':[0,650,1536,2533],'4a':[175,0,1688,2304],
   '6a':[0,330,1792,2297],'10c':[33,91,1764,2316],'11a':[84,0,1779,2304],'14d':[0,555,1856,2304],'5c':[0,0,1856,1940]}
BONE=[245,240,232]; RED=[196,20,20]
def P(k,letters=(),**kw):
    d={'type':'panel','img':f'gen/v_{k}.png','letters':list(letters)}
    if k in C: d['crop']=C[k]
    d.update(kw); return d
G=lambda h:{'type':'gap','h':h}
pilot=json.load(open('spec_pilot.json'))
spec=pilot[:-1]  # drop trailing gap
spec+= [G(260),
 P('3a',[{'k':'caption','head':'BOOTCAMP // DAY 8','body':"Lights out. My head didn't get the memo.",'x':0.05,'y':0.04,'maxw':430},
         {'k':'broly','t':'Can’t… slow down…','x':0.66,'y':0.33,'tx':0.34,'ty':0.42,'maxw':220,'size':28}]), G(120),
 P('3b',[{'k':'caption','head':'02:13 AM // COURTYARD','body':'Needed air. Any air.','x':0.05,'y':0.05,'maxw':420}]), G(70),
 P('3c',[{'k':'thought','t':'(Just… breathe.)','x':0.7,'y':0.1,'tx':0.52,'ty':0.2,'maxw':190,'size':28}]), G(70),
 P('3d',[{'k':'broly','t':'…I’m gonna—','x':0.74,'y':0.9,'tx':0.52,'ty':0.7,'maxw':220,'size':30}]), G(70),
 P('3e',[{'k':'shout','t':'Whoa! Easy—','x':0.3,'y':0.1,'tx':1.0,'ty':0.3,'size':34,'maxw':220}]), G(200),
 P('4a',[{'k':'caption','head':'PRE-BLACKOUT','body':'Last thing I remember clearly.','x':0.04,'y':0.04,'maxw':400},
         {'k':'sfx','t':'TSS','x':0.4,'y':0.36,'size':70,'big':False,'rot':-12},
         {'k':'other','t':'Hold still.','x':0.3,'y':0.86,'tx':1.0,'ty':0.97,'maxw':200,'size':30}]), G(70),
 P('4b',[{'k':'ambient','t':'beep…','x':0.6,'y':0.18,'size':34},{'k':'ambient','t':'drip…','x':0.12,'y':0.58,'size':30},{'k':'ambient','t':'drip…','x':0.62,'y':0.8,'size':30}]), G(70),
 P('4c',[{'k':'ambient','t':'drip…','x':0.1,'y':0.2,'size':28,'alpha':110},{'k':'ambient','t':'drip…','x':0.6,'y':0.35,'size':26,'alpha':90},
         {'k':'ambient','t':'drip…','x':0.2,'y':0.55,'size':24,'alpha':70},{'k':'ambient','t':'drip…','x':0.65,'y':0.72,'size':22,'alpha':50}]),
 {'type':'black','h':1100,'letters':[{'k':'ambient','t':'· · · · · ·','x':0.38,'y':0.48,'size':34,'alpha':220}]},
 P('5b',[{'k':'caption','head':'DAY: UNKNOWN // LOCATION: UNKNOWN','body':'Me: …also unknown.','x':0.04,'y':0.04,'maxw':440},
         {'k':'ambient','t':'ngh…','x':0.08,'y':0.72,'size':52,'alpha':200}]), G(70),
 P('5c',[{'k':'broly','t':'Where… am I…?','x':0.76,'y':0.8,'tx':0.56,'ty':0.62,'maxw':200,'size':30}]), G(200),
 P('6a',[{'k':'caption','head':'MILITARY MEDICAL WING','body':'Too clean. Too quiet.','x':0.05,'y':0.04,'maxw':420}]), G(70),
 P('6b'), G(70), P('6c'), G(70), P('6d'), G(70), P('6e'), G(200),
 P('7a'), {'type':'gap','h':900}, P('7d'), G(200),
 P('8a'), G(70), P('8b'), G(70), P('8c'), G(70), P('8d'), G(70), P('8e'), G(70),
 P('9a'), G(70), P('9b'), G(70), P('9c'), G(70), P('9d'), G(70), P('9e'), G(160),
 P('10a'), G(70), P('10b'), G(70), P('10c'), G(70), P('10d'), G(160),
 P('11a'), G(70), P('11b'), G(70), P('11c'), G(0), P('12'), G(200),
 {'type':'endcard','lines':[['END OF CH. 1','mono',RED],['FLASHBACK','marker',BONE]]}, G(300),
 {'type':'card','kind':'open','lines':[['HOSHOKU','logo',BONE],['VOL. 1 — FLASHBACK','mono',RED],['CH. 2','marker',BONE]]}, G(120),
 P('13a'), G(70), P('13b'), G(70), P('13c'), G(70), P('13d'), G(70), P('13e'), G(200),
 P('14a'), G(70),
 P('14b',[{'k':'num','t':'#007','x':0.38,'y':0.08,'size':80}]), G(70),
 P('14c',[{'k':'num','t':'#614','x':0.62,'y':0.3,'size':70}]), G(70),
 P('14d',[{'k':'num','t':'#389','x':0.4,'y':0.03,'size':70,'col':[235,235,240]}]), G(260),
 {'type':'endcard','lines':[['TO BE CONTINUED','mono',RED]]}]
json.dump(spec,open('spec_full.json','w'),indent=1)
print(len(spec))
