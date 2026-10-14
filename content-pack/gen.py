import html,json
B="https://cdn.shopify.com/s/files/1/1012/2307/2042/files/"
P={"hoshoku":("Ü-002 Hoshoku Shirt","undr-hoshoku_shirt-hero.png"),
"seekreal":("Seek Reality Oversized","hf_20261009_165807_02cf746e-d07a-4233-b9ac-98cb0e19d8c1.png"),
"seektruth":("Seek Truth Oversized","hf_20261009_164240_77377e4d-1025-4001-bd56-b22d77823e3e.png"),
"seeku":("Seek Ü Shirt","undr-seek_u_shirt-hero.png"),
"shorts":("Seek Ü Shorts","undr-seek_u_shorts-hero.png"),
"box":("Ü-000 Box Logo","hf_20261009_164239_a8a17498-65fa-4bbf-94ee-201bc73ec380.png"),
"voorhees":("Voorhees Shirt","hf_20261009_165807_500cef4a-7a0a-4675-a73c-59cb15fb5f68.png"),
"hon":("Hon Shirt","hf_20261009_163110_d8b8d1bc-807d-4ccf-91a7-b7a6b84219ce.png"),
"beanie2":("Hoshoku Beanie 2.0","undr-beanie-2-product.png"),
"beanieog":("Hoshoku Beanie OG","undr-beanie-og-product.png")}
# (id, group, title, image model, refs, image prompt, ratio, video prompt)
H="HOSHOKU: a fully anthropomorphic rabbit-fox fusion character, 18 years old, athletic muscular build, body split exactly 50/50 down the centre by a visible dark grey surgical-stitch seam (stitches also at shoulders, wrists, knees). Left half Bunni: pale lavender off-white fur (#D0D6EB), floppy rabbit ear with pink inner, red iris (#B83282), black diamond-shaped mark under that eye. Right half Renard: orange-brown fur (#C96A36), pointed fox ear with black tip, cyan-blue iris (#3BBED1), black X-shaped scar on that cheek, small fang on that side. Real animal muzzle and skull, clawed paws with pads, not a human face"
INK="rough dry-brush ink, cel-shaded, high detail"
J=[
("H0","Start here · Canon","HOSHOKU master sheet (make this first)","Nano Banana 2",["beanieog"],
H+", wearing simple dark grey shorts. Character turnaround sheet: front, 3/4, side, back, plus 3 expression heads (Bunni-side sad, Renard-side cocky smirk, split half-and-half). Plain off-white background, "+INK+".","16:9",
"Slow camera orbit around HOSHOKU standing still, fur moving slightly in wind, he blinks and the Renard side smirks. Plain background, "+INK+" anime style."),
("M1","Manga · HOSHOKU Vol 1 Flashback","Webtoon cover / key art","Nano Banana Pro",[],
"Vertical webtoon cover. A teenage boy, Broly, stands in a dark city street at night, and behind him looms the huge translucent figure of "+H+", visible only to Broly. Title space at top. Black, charcoal and blood-crimson palette, "+INK+".","9:16",
"Slow push-in on Broly. The ghostly HOSHOKU behind him slowly opens his eyes, red and cyan glints, and leans down to whisper. Dust drifts. No one else on the street reacts."),
("M2","Manga · HOSHOKU Vol 1 Flashback","Bookmark: time rewind","Seedream 4.5",[],
"Manga panel: Broly mid-gesture as the world around him freezes and runs backward, shattered glass suspended and reassembling, clock-hand motifs, a cracked meter labelled ODDITY glowing in the corner of his vision. Black and crimson, "+INK+".","9:16",
"Everything in the scene reverses in slow motion, glass pieces flying back together, Broly clutches his head as the strain hits. Camera locked, anime style."),
("M3","Manga · HOSHOKU Vol 1 Flashback","The storekeeper","Seedream 4.5",[],
"Manga splash: a menacing convenience-store storekeeper behind the counter, porcupine quills bristling out of his back and arms, flickering fluorescent tube light, shelves in shadow. Horror tension, black and crimson, "+INK+".","9:16",
"His quills slowly rise and rattle, the fluorescent light flickers, he looks up at camera. Slow push-in, horror pacing."),
("M4","Manga · HOSHOKU Vol 1 Flashback","Chapter 1 promo clip","Wan 3.0 only",[],
"Skip the image step: use your real Chapter 1 panels as start frames.",
"9:16","Slow vertical pan down the panel with a subtle parallax, ink lines shimmering, light dust. Keep the art exactly as is, only add camera motion."),
("V1","VTuber · HOSHOKU live","Starting soon loop","Nano Banana 2",["beanie2"],
H+", asleep slumped in a gaming chair in a dim bedroom streaming setup, warm desk lamp, rain on the window, beanie like the attached one on the desk. "+INK+".","16:9",
"Seamless loop: rain on the window, slow breathing, the fox ear twitches once. Camera locked."),
("V2","VTuber · HOSHOKU live","BRB: split argument","Nano Banana 2",[],
H+", sitting at a desk, the Bunni side looking sad at a snack, the Renard side grinning and reaching for it. "+INK+".","16:9",
"His own two hands fight over the snack, the Renard hand wins, the Bunni side pouts. Camera locked, comedic timing."),
("V3","VTuber · HOSHOKU live","Alerts: follow / sub / raid","Nano Banana 2",[],
"Chibi version of "+H+", jumping with arms up, plain dark charcoal background, centered. "+INK+".","1:1",
"He jumps and cheers, crimson sparks burst, lands with a Renard-side wink. 3 seconds."),
("B1","Brand · ÜNDR world","Hero tunnel loop","Seedream 4.5",["box"],
"Wet underground concrete tunnel at night, warm sodium lamps, faint graffiti, mist, at the far end one clothing rack lit from above holding the attached shirt. No people. Black and charcoal with small crimson accents, anamorphic, film grain.","16:9",
"Very slow push-in toward the rack, mist drifting, one lamp flickers. No people, seamless loop feel."),
("B2","Brand · ÜNDR world","Beanie 2.0 product film","Kling O1",["beanie2"],
"The attached crochet beanie on a black plinth, studio rim light, extreme detail of the yarn, rabbit and fox ears, stitched seam. Black background.","1:1",
"Slow turntable rotation, focus pull across the stitches to the ears. Soft light sweep."),
("B3","Brand · ÜNDR world","HOSHOKU wears the drop","Nano Banana 2",["hoshoku","shorts"],
H+", wearing the attached shirt and attached shorts, posing in an underground concrete stairwell, streetwear lookbook framing. Keep the garment prints exact. "+INK+".","9:16",
"He walks down the stairs toward camera, stops, the Renard side smirks. Handheld, cinematic."),
("B4","Brand · ÜNDR world","Seek Reality / Seek Truth pair","GPT Image",["seekreal","seektruth"],
"Two people back to back in a dark concrete room, one wearing each attached shirt, single overhead bulb, editorial, black and white with crimson accent.","9:16",
"Camera slowly circles them, bulb swings gently, they turn their heads toward camera at the same time."),
("S1","Starter looks · social","Devil Hunter fit","Nano Banana 2",["seektruth","box"],
"Photo of the attached shirt worn by a young man with messy silver-white hair, long open crimson leather duster coat, black cargo pants, combat boots, fingerless gloves, rain-soaked underground tunnel with sodium lamps. Devil May Cry Dante cosplay energy, cocky half-smile. Fashion editorial, 35mm, low angle. Keep the shirt print exact.","9:16",
"Slow push-in. He flicks rain off his coat, swings it back to show the shirt graphic, then smirks at camera. Rain, coat moving in wind, film grain."),
("S2","Starter looks · social","Assassin kid fit","Seedream 4.5",["seeku","shorts"],
"Fashion editorial of a slim young adult with spiky fluffy white hair and sharp blue eyes, Killua cosplay energy, wearing the attached shirt and attached shorts, hands in pockets, skateboard under one foot, Tokyo back alley at night, flash photography. Keep both prints exact.","9:16",
"He kicks the skateboard up into his hand, blue lightning crackles along his arm, he looks at camera bored and walks off. Handheld, flash-photo look."),
("S3","Starter looks · social","Influencer mirror selfie","Nano Banana 2",["hoshoku","beanie2"],
"Phone mirror selfie, young streetwear creator wearing the attached shirt and attached beanie, bedroom studio with manga posters, candid, realistic UGC, slight grain.","9:16",
"They adjust the beanie ears, turn to show the shirt back, laugh at the phone. Handheld phone footage."),
("S4","Starter looks · social","Voorhees night walk","FLUX.2 Pro",["voorhees"],
"Street photo of someone in the attached shirt walking alone under a flickering streetlight at night, fog, Atlanta suburb, horror mood, 35mm flash.","9:16",
"They walk toward camera, the light cuts out and back on and they're suddenly closer. Handheld, horror pacing."),
]
cards=[]
for g in dict.fromkeys(j[1] for j in J):
  cards.append(f'<h2>{g}</h2>')
  for i,gr,t,m,refs,ip,ar,vp in J:
    if gr!=g: continue
    r="".join(f'<a class="ref" href="{B}{P[k][1]}" target="_blank" rel="noopener">{html.escape(P[k][0])} ↗</a>' for k in refs) or '<span class="muted">No product image. Add your Bunni/Renard model art if you have it.</span>'
    cards.append(f'''<article class="job" id="{i}"><header><span class="tag">{i}</span><h3>{html.escape(t)}</h3><label class="done"><input type="checkbox" id="c{i}"> done</label></header>
<div class="step"><div class="lab">1 · Image · <b>{m}</b> · {ar}</div><div class="refs">{r}</div>
<p class="pr" id="i{i}">{html.escape(ip)}</p><button data-t="i{i}">Copy image prompt</button></div>
<div class="step"><div class="lab">2 · Video · <b>Wan 3.0</b> · start frame = best result above</div>
<p class="pr" id="v{i}">{html.escape(vp)}</p><button data-t="v{i}">Copy video prompt</button></div></article>''')
tpl=open('/home/user/docs/content-pack/shell.html').read()
open('/home/user/docs/content-pack/index.html','w').write(tpl.replace('%%CARDS%%',"\n".join(cards)))
