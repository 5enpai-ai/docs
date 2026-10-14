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
J=[
("D1","Day 1 · Hero drops","Devil Hunter fit","Nano Banana 2",["seektruth","box"],
"Photo of the attached shirt worn by a stylish young man with messy silver-white hair, long open crimson leather duster coat over the shirt so the graphic is fully visible, black cargo pants, combat boots, fingerless gloves. Standing in a rain-soaked underground concrete tunnel lit by red neon and sodium lamps. Devil May Cry Dante cosplay energy, cocky half-smile. Fashion editorial, 35mm, low angle, film grain. Keep the shirt print exactly as in the reference.","9:16",
"Low-angle slow push-in. He flicks rain off his coat, swings the coat back with one arm so the shirt graphic shows, then smirks at camera. Red neon flicker, rain falling, coat moving in wind. Cinematic, 35mm film grain."),
("D2","Day 1 · Hero drops","Assassin kid fit","Seedream 4.5",["seeku","shorts"],
"Fashion editorial of a slim teen-looking young adult with spiky fluffy white hair and sharp blue eyes, Killua Zoldyck cosplay energy, wearing the attached shirt and attached shorts, oversized, hands in pockets, skateboard under one foot. Neon-lit Tokyo back alley at night, faint blue electricity crackling around one hand. Shot on 35mm, flash photography, streetwear lookbook. Keep both garment prints exactly as referenced.","9:16",
"He kicks the skateboard up into his hand, blue lightning crackles briefly along his arm, he looks at camera bored and walks off. Handheld camera, flash-photo look, light motion blur."),
("D3","Day 1 · Hero drops","Influencer selfie series","Nano Banana 2",["hoshoku","beanie2"],
"Phone selfie in a mirror, young streetwear influencer wearing the attached shirt and attached beanie, messy dorm-studio room with anime posters, ring light reflection, iPhone in hand covering part of face, candid casual pose. Realistic UGC style, slight grain, warm practical light.","9:16",
"Mirror selfie. They tilt their head, adjust the beanie ears, do a quick turn to show the back of the shirt, then hold the phone closer and laugh. Handheld phone footage, natural light."),
("W1","Website","Hero tunnel loop","Seedream 4.5",["box"],
"Wide shot of a wet underground concrete tunnel at night, flickering sodium lights, faint graffiti, mist, at the far end a single clothing rack lit from above holding the attached shirt. No people. Cinematic, anamorphic, film grain, moody.","16:9",
"Very slow push-in down the tunnel toward the rack, mist drifting, one light flickering. Locked horizon, no people, seamless loop feel."),
("W2","Website","Floating drop teaser","GPT Image",["seekreal"],
"The attached oversized shirt floating in a black void, perfectly flat-lit front, hard rim light on the edges, dust particles, high contrast. Product hero shot, centered.","16:9",
"The shirt slowly rotates in mid-air, fabric rippling slightly, dust drifting through the rim light. Slow motion, black background."),
("W3","Website","Beanie macro","Kling O1",["beanieog"],
"Extreme macro of the attached crochet beanie, rabbit and fox ears, yarn texture sharp, shallow depth of field, soft window light, dark background.","1:1",
"Slow macro dolly across the crochet stitches toward the ears, focus pull, soft light shifts."),
("V1","VTuber stream","Starting soon","Nano Banana 2",["beanie2"],
"Anime illustration: a cream bunny girl asleep curled against a rust-orange fox boy's tail on a couch in a cozy neon-lit room, he is reading a manga, both wear beanies like the attached one, rain on the window, purple and orange lighting. 2D anime cel-shaded.","16:9",
"Gentle loop: rain streaks on window, she breathes slowly in her sleep, his tail twitches, he turns a page. Camera locked. Anime style."),
("V2","VTuber stream","BRB","Nano Banana 2",[],
"Anime illustration: cream bunny girl sneaking snacks from a shelf on tiptoe while a rust-orange fox boy watches from a gaming chair, unimpressed. Neon streamer room. 2D anime cel-shaded.","16:9",
"She grabs a snack and freezes when she notices him watching. He slowly raises an eyebrow. Camera locked, anime style."),
("V3","VTuber stream","Alert: new follower","Nano Banana 2",[],
"Anime chibi illustration of a cream bunny girl jumping with arms up and a rust-orange fox boy doing a slow clap, confetti, plain dark background, centered.","1:1",
"She jumps and cheers, confetti bursts, he gives a slow unimpressed clap. 3 seconds."),
("S1","Social","Voorhees night walk","FLUX.2 Pro",["voorhees"],
"Street photo of someone wearing the attached shirt walking alone under a flickering streetlight at night, hockey-mask horror mood, fog, Atlanta suburb, 35mm flash.","9:16",
"They walk toward camera, streetlight flickers off and back on and they're suddenly closer. Handheld, horror pacing."),
("S2","Social","Hon portrait","Seedream 5.0 lite",["hon"],
"Close portrait of a person wearing the attached shirt sitting on a rooftop at golden hour, city skyline, wind in hair, calm expression, editorial streetwear.","9:16",
"Wind blows, they look from the skyline to camera, slow push-in, golden light flare."),
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
