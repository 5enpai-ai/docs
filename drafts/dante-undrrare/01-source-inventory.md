# 1. Source inventory

**Verified Dante videos watched: 0.**

Every entry below was found through web-search result titles and URLs only. None could be opened from this session: the video hosts are blocked by the environment's network policy. Per the brief, every video entry is marked **UNVERIFIABLE**, and nothing about its content is inferred from titles, captions, thumbnails or commentary.

## 1.1 Creator accounts (primary sources to crawl)

| Account | URL | Access |
| --- | --- | --- |
| Luca Maxim, YouTube Shorts | https://www.youtube.com/@Santeluca/shorts | Blocked |
| Same channel, by ID | https://www.youtube.com/channel/UCNmniAIIs77bbCO2Dfa24oQ/shorts | Blocked |
| Luca Maxim, TikTok | https://www.tiktok.com/@santeluca | Blocked |
| Luca Maxim, Instagram | https://www.instagram.com/lucamaxiim/ | Blocked |
| Children Of Khan, Facebook | https://www.facebook.com/childrenofkhan/ | Blocked |

## 1.2 Candidate video URLs

"Uploader" is what the URL itself shows. "Dante?" records whether the search-result title mentions Dante. That tells us nothing about what the video contains.

| ID | URL | Title as indexed | Uploader | Dante? | Status |
| --- | --- | --- | --- | --- | --- |
| C01 | https://www.youtube.com/shorts/Mc8L16lgYck | "you met me at a very chinese time in my life #dante #you_met_me_at_a_very_chinese_time_in_my_life" | Unknown: may be a repost | Yes | UNVERIFIABLE |
| C02 | https://www.youtube.com/shorts/Nnmaw-zPwfk | "a very Chinese time in my life 🪷" | Unknown: may be a repost | No | UNVERIFIABLE |
| C03 | https://www.tiktok.com/@santeluca/video/7537015957332577568 | "Enroll at Children of Khan" | @santeluca | No | UNVERIFIABLE |
| C04 | https://www.tiktok.com/@santeluca/video/7536551727663713568 | "Luca Maxim: The Final Boss of AI and Technology" | @santeluca | No | UNVERIFIABLE |
| C05 | https://www.tiktok.com/@santeluca/video/7405952105984396577 | "Children of Khan T-Shirt Review: Is It Legit?" | @santeluca | No | UNVERIFIABLE |
| C06 | https://www.facebook.com/childrenofkhan/videos/its-hard-being-luca-maxim/825186950122655/ | "it's hard being Luca Maxim." | Children Of Khan | No | UNVERIFIABLE |
| C07 | https://www.tiktok.com/@notjax/video/7686230833656565006 | "You met me at a very Chinese time of my life #chinese #lucamaxim #childrenofkhan #viral" | @notjax (third party, not Luca) | No | UNVERIFIABLE, and not a primary source |

The other @santeluca and YouTube Shorts URLs surfaced by search are listed in [`tools/seed-urls.txt`](tools/seed-urls.txt). Their titles don't indicate Dante; they're kept only so the crawler checks them.

## 1.3 Secondhand leads (not evidence)

Search-engine summaries and third-party pages made the claims below. I couldn't open any of the underlying pages, so these claims are **not used anywhere in the analysis**. They're recorded only so that Phase 1 knows what to confirm or reject.

| Lead | Where it appeared | Verification needed |
| --- | --- | --- |
| Children Of Khan is Luca Maxim's apparel brand, and it appears at the end of his Shorts with a link | Search summary of the Wikitubia page (blocked) | Watch the endings |
| The brand's ads are AI-generated "PS2-style" videos | Search summaries | Watch and describe the render style |
| The line "You met me at a very Chinese time in my life" is associated with the Dante character | Search summaries, KYM page title, X posts by @Naexthaniel and via `x.com/i/status/2099110220572070277` | Confirm the exact wording and who says it, plus where and how often |
| The phrase appears on a Children Of Khan shirt | Search summary only | Confirm on screen and on the store |
| The phrase parodies the *Fight Club* (1999) line "You met me at a very strange time in my life." | KYM summary. The *Fight Club* line itself is a known quote. | Confirm the videos play off it and aren't simply using it |
| Other recurring Luca characters: Yakub, Selim Kerimov, Skebob | Search summary of Wikitubia | Only relevant if they appear in Dante videos |

## 1.4 What Phase 1 will capture per video

Each watched video becomes one record matching [`schema/video-record.schema.json`](schema/video-record.schema.json). A record carries every field from the brief, plus:

- a `provenance` block (who uploaded it, and whether it's an original or a repost)
- per-line timestamps for dialogue
- a `verification` field: `watched`, `partial` or `UNVERIFIABLE`

A video only counts toward the frequency tallies in Phase 2 if its `verification` is `watched` **and** it's a Luca Maxim original.
