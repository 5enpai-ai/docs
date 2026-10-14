import html
SH="https://cdn.shopify.com/s/files/1/1012/2307/2042/files/"
DR="https://drive.google.com/file/d/%s/view"
R={ # key: (label, source, url)
"split":("hoshoku_split_stitched_v2","Drive",DR%"1X8DAomebEfiHe4EwtLmiBVYco_OMh8pf"),
"bunny":("hoshoku_bunny_red_v2","Drive",DR%"1UX-KFtjWbGxjeFpnxxPGQHUb5EowhgNK"),
"fox":("hoshoku_fox_blue_v2","Drive",DR%"12w37fXSaZA3yZWDq_lYU55sLdyDzR3mL"),
"yinyang":("hoshoku_yinyang","Drive",DR%"1ehRPaFzLJ2BU3DSbXZzy9Lqx5646cQyN"),
"logo":("hoshoku_main_logo","Drive",DR%"1TvJNrEQlcR6_HEMuiUpvhRrw2k_juzH2"),
"textlogo":("hoshoku_text_logo","Drive",DR%"1XBikBOY-pzfKBDBC6eQ2FnvzISuQBA6F"),
"ch1":("Chapter 1 Webtoon Panels","Canva","https://www.canva.com/d/RBPEj1XnALYi8tp"),
"letter":("Lettering & SFX Guide","Canva","https://www.canva.com/d/QIC0jn-TdYdHr96"),
"palette":("HOSHOKU Color Palette","Canva","https://www.canva.com/d/vTnnBYRkS7wRoz2"),
"hfup":("Your Higgsfield uploads","Higgsfield","https://higgsfield.ai"),
"hoshoku":("Hoshoku Shirt","Shopify",SH+"undr-hoshoku_shirt-hero.png"),
"seekreal":("Seek Reality tee","Shopify",SH+"hf_20261009_165807_02cf746e-d07a-4233-b9ac-98cb0e19d8c1.png"),
"seektruth":("Seek Truth tee","Shopify",SH+"hf_20261009_164240_77377e4d-1025-4001-bd56-b22d77823e3e.png"),
"seeku":("Seek Ü shirt","Shopify",SH+"undr-seek_u_shirt-hero.png"),
"shorts":("Seek Ü shorts","Shopify",SH+"undr-seek_u_shorts-hero.png"),
"box":("Box Logo tee","Shopify",SH+"hf_20261009_164239_a8a17498-65fa-4bbf-94ee-201bc73ec380.png"),
"voorhees":("Voorhees shirt","Shopify",SH+"hf_20261009_165807_500cef4a-7a0a-4675-a73c-59cb15fb5f68.png"),
"hon":("Hon shirt","Shopify",SH+"hf_20261009_163110_d8b8d1bc-807d-4ccf-91a7-b7a6b84219ce.png"),
"beanie2":("Beanie 2.0","Shopify",SH+"undr-beanie-2-product.png"),
"beanieog":("Beanie OG","Shopify",SH+"undr-beanie-og-product.png"),
}
H="HOSHOKU: a fully anthropomorphic rabbit-fox fusion character, 18, athletic muscular build, body split exactly 50/50 down the centre by a visible dark grey surgical-stitch seam (stitches also at shoulders, wrists, knees). Bunni half: pale lavender off-white fur, floppy rabbit ear with pink inner, red iris, black diamond-shaped mark under that eye. Renard half: orange-brown fur, pointed fox ear with black tip, cyan-blue iris, black X-shaped scar on that cheek, small fang. Real animal muzzle and skull, clawed paws with pads"
INK="rough dry-brush ink, cel-shaded, high detail"
# projects: (id, name, why, [steps])  step: (code, day, title, model, refs, uses_steps, image_prompt or None, ratio, video_prompt, goes_to)
P=[
("core","HOSHOKU core","The master reference. Everything with HOSHOKU in it depends on this, so it runs first.",[
("C1",1,"Master turnaround sheet","Nano Banana 2",["split","bunny","fox"],[],
"Use the attached images as the exact character reference. "+H+", wearing simple dark grey shorts. Character turnaround sheet: front, 3/4, side, back, plus 3 expression heads (Bunni-side sad, Renard-side cocky smirk, split). Plain off-white background, "+INK+".","16:9",
"Slow camera orbit around HOSHOKU standing still, fur shifting in wind, he blinks and the Renard side smirks. Plain background.","Reference for every later HOSHOKU card"),
("C2",1,"Hero portrait","Seedream 4.5",["split"],["C1"],
"Using the attached sheet as the exact design: waist-up portrait of HOSHOKU looking straight at camera, Bunni side melancholic, Renard side half-smiling, dark charcoal background with a faint crimson rim light. "+INK+".","4:5",
"Very slow push-in. The red eye blinks a little after the cyan eye, a breath moves his fur. Barely-there motion, loopable.","Profile pics, banners, website hero"),
("C3",2,"Yin-yang emblem in motion","Seedream 5.0 lite",["yinyang","logo"],["C1"],
"Clean redraw of the attached HOSHOKU yin-yang emblem, centered on charcoal, ink-brush texture, crimson and cyan accents only.","1:1",
"The emblem slowly rotates a half turn, ink bleeds outward and resolves back. Seamless loop.","Logo sting for videos, stream, site"),
]),
("manga","Manga: HOSHOKU Vol 1 \"Flashback\"","Promo for the Webtoon. Uses only canon beats: Broly, bookmark, the ODDITY meter, the storekeeper. Nason and Niko stay out until their designs are locked.",[
("M1",2,"Chapter 1 panels, animated","Wan 3.0 only",["ch1"],[],None,"9:16",
"Slow vertical pan down the panel with subtle parallax, ink lines shimmering, light dust. Keep the art exactly as is, only add camera motion.","Webtoon promo shorts. Do one per panel."),
("M2",2,"Key art: Broly + unseen HOSHOKU","Nano Banana Pro",["split","ch1"],["C1"],
"Vertical webtoon cover. Teenage boy Broly (match the attached Chapter 1 art) stands in a dark city street at night. Behind him looms a huge translucent "+H+", visible only to Broly. Title space at top. Black, charcoal and blood-crimson, "+INK+".","9:16",
"Slow push-in on Broly. The ghostly HOSHOKU behind him opens red and cyan eyes and leans down to whisper. No one else on the street reacts.","Webtoon cover, Chapter 2 teaser"),
("M3",3,"Bookmark: time rewind","Seedream 4.5",["ch1"],["M2"],
"Manga panel: Broly mid-gesture as the world freezes and runs backward, shattered glass suspended and reassembling, a cracked meter labelled ODDITY in the corner of his vision. Match the attached art style. Black and crimson, "+INK+".","9:16",
"Everything reverses in slow motion, glass flies back together, Broly clutches his head as the strain hits.","Power-explainer short"),
("M4",3,"The storekeeper","Seedream 4.5",["ch1"],["M2"],
"Manga splash: a menacing convenience-store storekeeper behind the counter, porcupine quills bristling from his back and arms, flickering fluorescent tube, shelves in shadow. Match the attached art style. "+INK+".","9:16",
"Quills slowly rise and rattle, the light flickers, he looks up at camera. Horror pacing.","Villain reveal short"),
("M5",4,"Chapter 2 trailer cut","Wan 3.0 only",[],["M1","M2","M3","M4"],None,"9:16",
"Use each finished clip above as a shot. Stitch them in CapCut: M2, then M3, then M4, then end on M2. Add red and blue lettering from the Lettering Guide.","Webtoon trailer, pinned post"),
]),
("vtuber","VTuber: HOSHOKU live","Stream package. Each piece uses the C1 sheet so the model stays on-design.",[
("V1",3,"Starting soon loop","Nano Banana 2",["split","beanie2"],["C1"],
H+", asleep slumped in a gaming chair in a dim bedroom streaming setup, warm desk lamp, rain on the window, beanie like the attached one on the desk. "+INK+".","16:9",
"Seamless loop: rain on the window, slow breathing, the fox ear twitches once. Camera locked.","OBS starting scene"),
("V2",4,"BRB: halves fight","Nano Banana 2",["split"],["C1"],
H+", at a desk, the Bunni side looking sadly at a snack, the Renard side grinning and reaching for it. "+INK+".","16:9",
"His own two hands fight over the snack, the Renard hand wins, the Bunni side pouts. Camera locked.","OBS BRB scene"),
("V3",4,"Alerts: follow / sub / raid","Nano Banana 2",["split"],["C1"],
"Chibi "+H+", jumping with arms up, plain charcoal background, centered. "+INK+".","1:1",
"He jumps and cheers, crimson sparks burst, lands with a Renard-side wink. 3 seconds.","Stream alerts. Make 3 variants."),
("V4",5,"Ending screen","Nano Banana 2",["split"],["C1","C3"],
H+", waving goodbye from a rooftop at night, city below, Bunni side sad, Renard side grinning. "+INK+".","16:9",
"He waves, turns away, the yin-yang emblem fades in over the sky. Camera pulls back.","OBS ending scene"),
]),
("brand","ÜNDR brand + website","The world the products live in. These get used on the site the longest.",[
("B1",1,"Hero tunnel loop","Seedream 4.5",["box"],[],
"Wet underground concrete tunnel at night, warm sodium lamps, faint graffiti, mist, at the far end a single clothing rack lit from above holding the attached shirt. No people. Black and charcoal with small crimson accents, anamorphic, film grain.","16:9",
"Very slow push-in toward the rack, mist drifting, one lamp flickers. No people, seamless loop feel.","Homepage hero (desktop). Rerun at 9:16 for mobile."),
("B2",2,"Beanie 2.0 product film","Kling O1",["beanie2"],[],
"The attached crochet beanie on a black plinth, studio rim light, extreme yarn detail, rabbit and fox ears, stitched seam. Black background.","1:1",
"Slow turntable rotation, focus pull across the stitches to the ears.","Beanie 2.0 product page ($75 priority item)"),
("B3",3,"HOSHOKU wears the drop","Nano Banana 2",["split","hoshoku","shorts"],["C1"],
H+", wearing the attached shirt and attached shorts, in an underground concrete stairwell, streetwear lookbook framing. Keep garment prints exact. "+INK+".","9:16",
"He walks down the stairs toward camera, stops, the Renard side smirks. Handheld.","Character Collection page, Reels"),
("B4",4,"Seek Reality / Seek Truth pair","GPT Image",["seekreal","seektruth"],[],
"Two people back to back in a dark concrete room, one in each attached shirt, single overhead bulb, editorial, black and white with crimson accent.","9:16",
"Camera slowly circles them, the bulb swings, they turn their heads to camera together.","Ü-002 collection banner"),
("B5",5,"Beanie OG origin film","Kling O1",["beanieog","logo"],["B2"],
"The attached OG beanie resting in an archival evidence box labelled FILE HOSHOKU-01, soft top light, dust, charcoal background.","1:1",
"Slow top-down push-in, a hand lifts the beanie out of the box, dust in the light.","Beanie OG page"),
]),
("social","Social: starter looks + posts","Volume content. Runs any time a slot is free.",[
("S1",1,"Devil Hunter fit","Nano Banana 2",["seektruth","box"],[],
"The attached shirt worn by a young man with messy silver-white hair, long open crimson leather duster, black cargo pants, combat boots, fingerless gloves, rain-soaked tunnel with sodium lamps. Dante cosplay energy, cocky half-smile. 35mm editorial, low angle. Keep the print exact.","9:16",
"Slow push-in. He flicks rain off his coat, swings it back to show the shirt, smirks at camera.","TikTok / Reels"),
("S2",1,"Assassin kid fit","Seedream 4.5",["seeku","shorts"],[],
"Slim young adult with spiky fluffy white hair and sharp blue eyes, Killua cosplay energy, wearing the attached shirt and shorts, skateboard under one foot, Tokyo back alley at night, flash photography. Keep prints exact.","9:16",
"He kicks the board up into his hand, blue lightning crackles along his arm, he looks bored and walks off.","TikTok / Reels"),
("S3",2,"Influencer mirror selfie","Nano Banana 2",["hoshoku","beanie2"],[],
"Phone mirror selfie, young streetwear creator wearing the attached shirt and beanie, bedroom studio with manga posters, candid UGC, slight grain.","9:16",
"They adjust the beanie ears, turn to show the shirt back, laugh at the phone.","TikTok / Reels"),
("S4",5,"Voorhees night walk","FLUX.2 Pro",["voorhees"],[],
"Someone in the attached shirt walking alone under a flickering streetlight at night, fog, Atlanta suburb, horror mood, 35mm flash.","9:16",
"They walk toward camera, the light cuts out and back on and they're suddenly closer.","TikTok / Reels"),
("S5",6,"Hon rooftop","Seedream 5.0 lite",["hon"],[],
"Close portrait of a person in the attached shirt on a rooftop at golden hour, city skyline, wind, calm, editorial streetwear.","9:16",
"Wind blows, they look from the skyline to camera, slow push-in.","Instagram"),
]),
]
DAYS={1:"Oct 14",2:"Oct 15",3:"Oct 16",4:"Oct 17",5:"Oct 18",6:"Oct 19",7:"Oct 20"}
e=html.escape
out=[]
# timeline
out.append('<section class="tl"><h2>Timeline</h2><p class="muted">Every card in order. Tap a code to jump to its card. Day 7 is for reruns in the other aspect ratio and anything that failed.</p>')
for d in range(1,8):
  items=[(s[0],s[2],p[1]) for p in P for s in p[3] if s[1]==d]
  out.append(f'<div class="day"><div class="dlab">Day {d}<span>{DAYS[d]}</span></div><div class="dits">'+("".join(f'<a href="#{c}" class="pill p-{c[0]}">{c} {e(t)}</a>' for c,t,_ in items) or '<span class="muted">Reruns, alt ratios, fixes</span>')+'</div></div>')
out.append('</section>')
out.append('<nav class="pn">'+"".join(f'<a href="#{p[0]}" class="pill p-{p[3][0][0][0]}">{e(p[1])}</a>' for p in P)+'</nav>')
for pid,name,why,steps in P:
  out.append(f'<section class="proj" id="{pid}"><h2>{e(name)}</h2><p class="muted">{e(why)}</p>')
  for c,d,t,m,refs,uses,ip,ar,vp,goes in steps:
    chips="".join(f'<a class="ref s-{R[k][1]}" href="{R[k][2]}" target="_blank" rel="noopener"><small>{R[k][1]}</small>{e(R[k][0])} ↗</a>' for k in refs)
    chips+="".join(f'<a class="ref s-step" href="#{u}"><small>Output</small>{u}</a>' for u in uses)
    img=(f'<div class="step"><div class="lab">1 · Image · <b>{m}</b> · {ar}</div><p class="pr" id="i{c}">{e(ip)}</p><button data-t="i{c}">Copy image prompt</button></div>' if ip else '')
    n="2" if ip else "1"
    start="start frame = best image from step 1" if ip else "start frame = the reference above"
    out.append(f'''<article class="job" id="{c}"><header><span class="tag p-{c[0]}">{c}</span><h3>{e(t)}</h3><span class="day-s">Day {d}</span><label class="done"><input type="checkbox" id="c{c}"> done</label></header>
<div class="refs">{chips or '<span class="muted">No reference needed</span>'}</div>{img}
<div class="step"><div class="lab">{n} · Video · <b>Wan 3.0</b> · {start}</div><p class="pr" id="v{c}">{e(vp)}</p><button data-t="v{c}">Copy video prompt</button></div>
<div class="goes">Goes to: {e(goes)}</div></article>''')
  out.append('</section>')
t=open('shell.html').read()
open('index.html','w').write(t.replace('%%CARDS%%',"\n".join(out)))
