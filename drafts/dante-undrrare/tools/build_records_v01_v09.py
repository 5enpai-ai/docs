"""Build data/videos/V01-V09 records from the local session's V01-V09 handoff.

The local Codex research session watched the footage; this script only encodes
its relayed findings. Re-running it overwrites every JSON file in data/videos/.
"""
import json, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "videos")
TAG = "You met me at a very Chinese time in my life."
CTA = "Get yours at childrenofkhan.com. Link in bio."
INSPECTED = "Verified by local Codex research session (reel downloaded, watched, transcribed and frame-sampled). This cloud session didn't view the media directly."
BASE = "/Volumes/lacie/watch-work/luca-dante/"
MISSING = ["music (UNVERIFIED)", "SFX (UNVERIFIED)", "tag and CTA line end times", "upload date"]

# (id, slug, url, caption, content_caption_note, duration, cuts, [(t, line)], tag_t, cta_t,
#  pivot_t, pivot_type, topic_group, setting, visual, secondary, hook_form, props)
V = [
 ("V01","gym-guys","https://www.instagram.com/reel/DdzNE-nlZy7/","Gym guys",None,22.83,[0.97,5.07,8.10,15.30,18.70],
  [(0,"She'll never find another Gymshark-wearing, white-Monster-drinking, Deftones-listening, mirror-selfie-taking guy who eats a plain chicken breast in his car and calls that a personality."),
   (8,"My supplier in Guangdong eats what his mom cooks, lifts boxes for a living, and has never once made that his entire personality.")],
  15,18,8,"supplier","social type","Wide futuristic silver home gym / living room",
  "Opens wide: Dante reclines on a silver couch at left, and a second gym-goer sits hunched by a weight bench/rack at right. Dante rises, crosses the room and handles exaggerated weights and equipment. The second figure stays atmospheric.",
  ["second gym-goer (atmospheric)"],"third-person stereotype list ('She'll never find another …')",["exaggerated weights / gym equipment"]),
 ("V02","star-wars-guys","https://www.instagram.com/reel/DdzGN_PjRVJ/","Star Wars guys",None,24.23,[5.90,10.83,17.17,20.10],
  [(0,"Star Wars fans are the strangest individuals."),
   (4,"They'll spend $400 on a lightsaber, have strong opinions about a movie from 1999, and explain what a midichlorian is to a girl who didn't ask."),
   (11,"My supplier makes the lightsabers in a factory in Dongguan. He's never seen the movie. He just knows that the purple one sells more.")],
  17,19,11,"supplier","fandom","Dark blue sci-fi / car set",
  "Dante holds a glowing purple lightsaber. Supporting figures stay background atmosphere. Hard cut to a white catalog/model end card.",
  ["supporting figures (background)"],"categorical verdict ('X fans are the strangest individuals')",["purple lightsaber"]),
 ("V03","british-bruv","https://www.instagram.com/reel/Ddy_VwgCrA4/","How'd you know I'm British bruv?",None,24.50,[5.83,12.90,17.17,20.37],
  [(0,"British girls will paint their face orange, call you bruv within 30 seconds of meeting you, and then ask, 'How did you know I'm British?'"),
   (5,"I don't know, sis. You've called every man in the room babe, said 'I'm not even drunk' while holding the wall, and have been planning a trip to Ibiza since January."),
   (13,"Seems cool being British. I wish I could be British, but I can't, because I'm Chinese.")],
  17,19,13,"identity","nationality","Bright white hallway",
  "A woman and a man in the background display an Essex-style flag. Wide and close framing alternate. Ends on a catalog end card.",
  ["woman and man with flag (background)"],"behavior list ending in a quoted question ('How did you know I'm British?')",["Essex-style flag"]),
 ("V04","dbz-guys","https://www.instagram.com/reel/Ddy4dP2ggJJ/","DBZ guys",None,26.80,[5.63,12.37,16.47,21.93],
  [(0,"Dragon Ball fans are the weirdest people."),
   (2,"They'll argue for hours about power levels and who Goku can solo, constantly saying stuff like, 'It's over 9,000.'"),
   (8,"Bro, the only thing over 9,000 is your weight."),
   (12,"My supplier's nephew in Guangzhou watches the same show and has never once scaled anybody. He just likes the yelling and the bright colors.")],
  18,20,12,"supplier","fandom","Fantasy city / sky scene with cloud",
  "Dante holds a Frieza-like figure/object and appears on a cloud. Then a product cutout and a model end card.",
  [],"categorical verdict ('X fans are the weirdest people')",["Frieza-like figure", "cloud"]),
 ("V05","slovak","https://www.instagram.com/reel/DdyxnNiDyix/","How did you know I'm Slovak??",None,25.90,[4.73,13.63,17.50,20.23],
  [(0,"Slovak guys will spend the whole night explaining they're not Czech, then ask, 'How did you know I'm Slovak?'"),
   (3,"I don't know, bro. Your grandma's soup has enough garlic to stop a heart, you can't stop drinking Kofola, and you got personally offended when I said Bratislava was near Vienna."),
   (14,"Seems cool being Slovak. I wish I could be Slovak, but I can't, because I'm Chinese.")],
  17,19,14,"identity","nationality","Snowy airport with a jet",
  "Dante gestures beside the aircraft, then enters the cockpit. Ends on a catalog end card.",
  [],"behavior list ending in a quoted question ('How did you know I'm Slovak?')",["aircraft / cockpit"]),
 ("V06","fnaf-lore","https://www.instagram.com/reel/DdyBfgGjEla/","elite ball knowledge","The published caption says 'elite ball knowledge', but the footage is about FNAF lore.",30.10,[5.57,13.07,23.83,27.73],
  [(0,"Why do FNAF lore kids know more about a fake pizza place than their own family?"),
   (5,"He's 14, has watched 40 hours of theory videos, and he can tell you which animatronic is possessed by which kid from a book he's never read."),
   (14,"He doesn't know his grandma's first name."),
   (17,"My supplier's daughter is nine and knows every animatronic too. She also knows her grandma's name. The grandma taught her.")],
  23,26,17,"supplier","fandom","Futuristic white room full of FNAF plushes",
  "Dante handles plushes. Ends on a catalog end card.",
  [],"rhetorical question about the group",["FNAF plushes"]),
 ("V07","goldmine-of-stuff","https://www.instagram.com/reel/Ddx6nlWlfCF/","goldmine of stuff",None,28.10,[8.40,11.60,19.60,19.73,24.60,25.73],
  [(0,"Chinese stationery stores are the best."),
   (2,"A whole store of pens, notebooks, and stickers, and every one of them is cuter than anything back home."),
   (8,"I went in for a pen and came out with a bag."),
   (11,"Look at this. I just got a notebook with a Pokémon on every page in the Chinese print, and the pen it came with has a Charizard on the cap. Amazing, right?")],
  21,24,11,"positive_china","china_positive","Outdoor / fantasy setting",
  "Dante reclines and shows off a notebook and pen. Positive discovery premise, not a mocking comparison. Ends on a catalog end card.",
  [],"positive categorical verdict ('Chinese stationery stores are the best')",["notebook", "Charizard pen"]),
 ("V08","hungry-games","https://www.instagram.com/reel/DdxfJ9dE9Cs/","hungry games",None,25.10,[4.47,9.63,12.30,22.70],
  [(0,"Hunger Games fans will put their three fingers up at a concert and act like it means something."),
   (4,"She's read all the books six times, has a Mockingjay pin from 2012, and thinks she'd survive the games, despite never once having been camping."),
   (11,"My supplier's cousin went to the movie in Guangzhou, said the girl with the bow was good, and went home. She didn't need to make it her whole personality.")],
  19,22,11,"supplier","fandom","Glossy futuristic room",
  "Dante is alone. Medium, wide and close framing changes. Ends on a catalog end card.",
  [],"behavior observation ('X fans will …')",[]),
 ("V09","frat-boys","https://www.instagram.com/reel/DdxKkH3Dz27/","frat boys",None,25.50,[2.73,11.80,19.17,22.80],
  [(0,"Frat boys are the most insufferable people."),
   (2,"He's 20, his shirt has Greek letters he can't pronounce, and he's called 11 strangers brother tonight."),
   (8,"By the end of the night, he's made eight girls uncomfortable and thrown up on the porch."),
   (11,"My supplier's got 200 guys on his floor from 11 provinces, and they call each other brother too. The difference is, they're respectful to the people around them.")],
  19,22,11,"supplier","social type","Futuristic lounge / party set",
  "Two men with cups appear behind Dante. Ends on a catalog end card.",
  ["two men with cups (background)"],"categorical verdict ('X are the most insufferable people')",["cups"]),
]

os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    if f.endswith(".json"): os.remove(os.path.join(OUT, f))
for (vid,slug,url,cap,capnote,dur,cuts,lines,tag_t,cta_t,piv_t,piv_type,group,setting,visual,secondary,hook_form,props) in V:
    dlg=[{"t_start":t,"speaker":"Dante (on-screen speaker)","line":l} for t,l in lines]
    dlg.append({"t_start":tag_t,"speaker":"Dante","line":TAG,"delivery":"recurring tag"})
    dlg.append({"t_start":cta_t,"speaker":"Dante","line":CTA,"delivery":"CTA"})
    beats=[{"function":"hook","t_start":0}]
    esc=[t for t,_ in lines[1:] if t<piv_t]
    if esc: beats.append({"function":"escalation","t_start":esc[0],"lines":len(esc)})
    beats += [{"function":"pivot","t_start":piv_t,"type":piv_type},
              {"function":"tag","t_start":tag_t},
              {"function":"cta","t_start":cta_t}]
    rec={
     "id":vid,"url":url,"verification":"watched",
     "provenance":{"uploader":"@lucamaxiim","is_luca_original":True,"upload_date":None,"platform":"instagram",
                   "inspected_by":INSPECTED,"media_path":BASE+slug+"/" if vid=="V01" else BASE+" (reel folder name not in the handoff)"},
     "title_or_caption":cap,
     "content_vs_caption":capnote,
     "duration_s":dur,
     "characters":["Dante (Devil May Cry): white-haired, goggled older-game-model look, on-screen speaker"]+secondary,
     "setting":setting,
     "topic_group":group,
     "opening_hook":f"{hook_form}: \"{lines[0][1]}\"",
     "dialogue":dlg,
     "beats":beats,
     "pivot_type":piv_type,
     "final_line":CTA,
     "recurring_phrases":[{"text":TAG,"timestamps":[tag_t],"channel":"mixed","beat_function":"last joke line before the CTA, spoken while the same text is printed on Dante's crewneck"}],
     "product":{"item":"Red Children of Khan crewneck worn by Dante throughout","visible_text":TAG,
                "first_on_screen_s":0,"text_readable_s":[],"garment_visible_at_tag":True,
                "entry_into_joke":"Worn through the comedy. Semantically central at the spoken/printed tag. Then isolated on a white-background garment/model end card with www.childrenofkhan.com."},
     "props":props,
     "editing":{"cut_times_s":cuts,"shot_count":len(cuts)+1,"avg_shot_s":round(dur/(len(cuts)+1),2),
                "transitions":"Hard cut to a white-background catalog / model end card"},
     "visual_notes":visual,
     "render_characteristics":"Older-game-model (PS2 / early-3D) look",
     "voice":"One male voice presented as Dante's speech",
     "on_screen_text":"Bold white captions with dark outline/shadow throughout. www.childrenofkhan.com on the end card.",
     "sfx":[],"music":None,
     "ending_structure":"Recurring tag → hard cut to white-background garment/model end card → spoken CTA",
     "repeated_from_other_videos":["Dante model","red crewneck with the tag printed","tag line","CTA line","white catalog end card","caption style"],
     "missing_from_relay":MISSING,
     "notes":None}
    if vid=="V01":
        rec["notes"]="Speaker evidence: changing mouth/face animation on Dante; no separate narrator appears on screen."
    else:
        rec["missing_from_relay"]=MISSING+["verbatim tag and CTA wording for this reel: the handoff transcript says only 'recurring tag' / 'CTA', and the wording here comes from the packet's 9/9 constants (#6, #7)"]
    json.dump(rec,open(f"{OUT}/{vid}-{slug}.json","w"),indent=2,ensure_ascii=False)
print("written",len(V))
