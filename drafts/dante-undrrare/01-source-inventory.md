# 1. Source inventory

**Verified Dante videos: 1** (V01, inspected by the local Codex session).

This cloud session still can't reach any video host. Footage is inspected by the local research session through the user's logged-in Instagram browser. Media and analysis live on the user's machine under `/Volumes/lacie/watch-work/luca-dante/<reel>/`, and structured records get relayed here into [`data/videos/`](data/videos/). Media is never stored in this repo.

A candidate is only upgraded from **UNVERIFIABLE** once its footage and audio have actually been inspected. Nothing about a video's content is inferred from titles, captions, thumbnails or commentary.

## 1.1 Creator accounts (primary sources to crawl)

| Account | URL | Access |
| --- | --- | --- |
| Luca Maxim, YouTube Shorts | https://www.youtube.com/@Santeluca/shorts | Blocked |
| Same channel, by ID | https://www.youtube.com/channel/UCNmniAIIs77bbCO2Dfa24oQ/shorts | Blocked |
| Luca Maxim, TikTok | https://www.tiktok.com/@santeluca | Blocked |
| Luca Maxim, Instagram (**where the Dante videos are**, per the user) | https://www.instagram.com/lucamaxiim/ | Accessible only through the local session |
| Children Of Khan, Facebook | https://www.facebook.com/childrenofkhan/ | Blocked |

## 1.2 Verified videos

| ID | URL | Caption | Duration | Inspected by | Media | Record |
| --- | --- | --- | --- | --- | --- | --- |
| V01 | https://www.instagram.com/lucamaxiim/reel/DdzNE-nlZy7/ | "Gym guys" | 22.83 s | Local Codex session (relayed) | `/Volumes/lacie/watch-work/luca-dante/gym-guys/` | [`data/videos/V01-gym-guys.json`](data/videos/V01-gym-guys.json) |

## 1.3 Candidate video URLs (still unverified)

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

## 1.4 Secondhand leads

Search-engine summaries and third-party pages made the claims below. A lead only counts as confirmed for a video that was actually inspected. Frequency across the format is still open.

| Lead | Where it appeared | Status |
| --- | --- | --- |
| Children Of Khan is Luca Maxim's apparel brand, and it appears at the end of his Shorts with a link | Search summary of the Wikitubia page (blocked) | **Seen in V01**: it ends with "Get yours at childrenofkhan.com. Link in bio." |
| The brand's ads are AI-generated "PS2-style" videos | Search summaries | **Seen in V01**: PS2 / early-2000s game aesthetic |
| The line "You met me at a very Chinese time in my life" is associated with the Dante character | Search summaries, KYM page title, X posts by @Naexthaniel and via `x.com/i/status/2099110220572070277` | **Seen in V01**: spoken verbatim as the tag |
| The phrase appears on a Children Of Khan shirt | Search summary only | **Seen in V01**: the red crewneck carries the phrase. The exact print still needs transcribing. |
| The phrase parodies the *Fight Club* (1999) line "You met me at a very strange time in my life." | KYM summary. The *Fight Club* line itself is a known quote. | Confirm the videos play off it and aren't simply using it |
| Other recurring Luca characters: Yakub, Selim Kerimov, Skebob | Search summary of Wikitubia | Only relevant if they appear in Dante videos |

## 1.5 What Phase 1 will capture per video

Each watched video becomes one record matching [`schema/video-record.schema.json`](schema/video-record.schema.json). A record carries every field from the brief, plus:

- a `provenance` block (who uploaded it, and whether it's an original or a repost)
- per-line timestamps for dialogue
- a `verification` field: `watched`, `partial` or `UNVERIFIABLE`
- `inspected_by` and `media_path`, so every claim can be traced back to footage

A video only counts toward the frequency tallies in Phase 2 if its `verification` is `watched` **and** it's a Luca Maxim original.
