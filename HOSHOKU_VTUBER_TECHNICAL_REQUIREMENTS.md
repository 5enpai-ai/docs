# HOSHOKU VTuber — technical pipeline requirements

Companion to `HOSHOKU_VTUBER_STATE.md`, `HOSHOKU_VTUBER_DRIVE_REFERENCE_AUDIT.md`, and `HOSHOKU_VTUBER_VISUAL_VERIFICATION.md`.

This is general technical/domain research into what the 2D and 3D VTuber pipelines require — it does not depend on seeing any HOSHOKU image, and nothing here commits to a 2D or 3D path. No software was installed, no accounts were created, and no credits were spent to produce it.

<Note>
**2D and 3D are separate production tracks with separate source-asset requirements.** They can share the same visual design (the confirmed HOSHOKU identity, once verified), but a single image is not automatically usable for both. Plan for two distinct deliverables, not one asset that does everything.
</Note>

---

## 2D track: artwork → Live2D → VTube Studio → OBS

**Pipeline:** HOSHOKU artwork → layer separation → Live2D Cubism → VTube Studio → face tracking → mouth/lip-sync → OBS

### What the source artwork must be

- A single, flat, front-facing illustration at rest — not a photo, not a posed scene, not a multi-panel sheet. Live2D "cuts" one image into movable parts; it does not composite from multiple references.
- Painted (or paintable) in **layers that anticipate separation**: head, each eye, eyebrows, mouth, and any independently-moving element (ears, hair strands, accessories) need to exist as parts that can be isolated — either because the source file already has them on separate layers, or because they can be cleanly cut out of a flat image in Photoshop/Clip Studio/GIMP afterward.
- High resolution (Live2D's own guidance: at least 2000–4000px on the long edge for a bust-up model) since parts get warped and deformed during rigging.
- A neutral, symmetrical-as-possible rest pose. Asymmetry (like a one-sided seam or a single floppy ear) is fine as *design*, but the rigger needs to know it's intentional, not a posing artifact.

### Layer separation

- Manual or semi-automated (some tools, e.g. Clip Studio's "auto-select" or Photoshop's subject-select tooling, can assist, but a stitched-puppet character with a center seam is exactly the kind of asymmetric, texture-heavy subject that benefits from manual layer work).
- Minimum layer set for a talking VTuber bust: base head/body, left eye (open + closed states), right eye (open + closed), eyebrows, mouth (see viseme set below), and any parts that should independently sway or blink.
- HOSHOKU-specific complication, flagged but not resolved here: the center seam crosses the face. Standard Live2D face rigs assume a roughly bilateral face where left/right deform together. A seam that visually divides the face into two different characters (different fur colors, different eye colors) may need the rig built as two coordinated half-faces rather than one symmetric face — this is a rigging decision, not a generation decision, and it's a strong reason the mouth-at-the-seam question (still open, see the visual verification queue) matters before any layered artwork is finalized.

### Live2D Cubism

- Cubism Editor (Adobe/Live2D Inc.) is the authoring tool. Free tier exists but caps project complexity; a paid tier (Pro) is typically needed for a full commercial-grade rig with physics (hair/ear sway) and advanced deformers.
- Output is a `.moc3` model file plus its texture atlas — this is what VTube Studio (and other Live2D-compatible runtimes) load.
- Minimum facial controls for expressive real-time tracking: `ParamAngleX/Y/Z` (head turn/tilt), `ParamEyeLOpen`/`ParamEyeROpen` (independent eye blink — useful here since the two halves may blink differently), `ParamEyeBallX/Y` (eye look direction), `ParamBrowLY/RY` or similar, `ParamMouthOpenY` (mouth open amount), and ideally `ParamMouthForm` (mouth shape, for viseme approximation).

### VTube Studio + face tracking

- VTube Studio (desktop, iOS via its own app, or webcam-based on desktop) reads a webcam or phone-based face tracker (ARKit blendshapes on iOS, or its own webcam tracker on desktop) and maps tracked expressions to the model's Cubism parameters above.
- Mouth/lip-sync in VTube Studio is typically **audio-driven** (mic input volume mapped to `ParamMouthOpenY`) rather than true viseme-matched phoneme detection, unless a plugin or the tracker's own mouth-shape detection is used. This matters for the mouth-shape sheet question: a full A/I/U/E/O viseme set is *nice to have* for hand-animated cutscenes or pre-rendered content, but the live VTube Studio pipeline mostly needs open/closed + a couple of shape variants, not a full phoneme set.
- Output goes to OBS via VTube Studio's built-in window capture or its transparent-background virtual camera / NDI/Spout output.

### What Live2D/VTube Studio can automate vs. what's manual

| Step | Automated | Manual |
| --- | --- | --- |
| Layer separation | Partial (selection assist tools) | Yes, mostly manual for a complex character |
| Rigging (deformers, physics) | Partial (Cubism has auto-rigging aids for simple parts) | Yes, expression/mouth rigging is hand-done |
| Face tracking → parameter mapping | Yes (VTube Studio handles this once params exist) | N/A |
| Mouth/lip-sync | Yes (audio-volume-driven, automatic) | Only if a custom viseme system is wanted |

---

## 3D track: model → rig → VRM → VSeeFace/Warudo → OBS

**Pipeline:** HOSHOKU model → humanoid rig → facial blendshapes → VRM → VSeeFace/Warudo → face/mouth tracking → OBS

### What the source reference/model must be

- For **Meshy image-to-3D**: one or more clean, well-lit reference images of the subject, ideally from multiple angles (front/side/back or front/3-quarter) for better geometric accuracy — Meshy explicitly supports both single-image and multi-image-to-3D, with multi-image producing more accurate geometry. This is exactly the gap the "no back view found anywhere" finding in the Drive audit points at.
- A turnaround sheet (once one exists/is confirmed) is therefore *more valuable for 3D than a single portrait*, because it feeds multi-image reconstruction directly.

### Required file formats

- **GLB** — the standard interchange format for a rigged, textured 3D asset; what Meshy exports and what most modern pipelines (including Blender, Unity, and glTF-based tools) consume directly.
- **VRM** (`.vrm`, itself a profile of glTF/GLB) — the format VTuber runtimes (VSeeFace, Warudo, VRChat, etc.) actually load. A plain GLB humanoid model is not a VRM until it's been run through a VRM-conversion/setup step (typically in Unity with UniVRM, or in Blender with a VRM export addon) that adds the VRM-specific metadata, humanoid bone mapping, and blendshape-clip definitions.
- **FBX** — useful as an interchange format if the model needs to pass through a DCC tool (Blender, Maya) for manual rig/weight fixes before VRM conversion; not itself a runtime format for these VTuber tools.

### Minimum facial controls / blendshapes for VRM

VRM's standard defines expected "expression presets" that runtimes look for. At minimum, a usable VRM face needs blendshapes (or equivalent bone-driven shape keys) for:

- **Blink**: `blink`, plus ideally independent `blinkLeft`/`blinkRight` (directly relevant here, since the two halves may blink asymmetrically — this is one of the still-open questions)
- **Basic mouth/viseme set**: VRM's standard viseme preset is the five-vowel set — `aa`, `ih`, `ou`, `ee`, `oh` (i.e., A/I/U/E/O) — mapped from phoneme detection or audio analysis in the runtime
- **Basic emotion presets**: `happy`, `angry`, `sad`, `surprised`, `neutral` (VRM 0.x/1.0 standard expression names differ slightly but cover the same ground)
- **Look-at**: horizontal/vertical eye-look blendshapes or bone-driven eye rotation

### Humanoid rig requirements

- A **VRM-compliant humanoid bone hierarchy** (hips → spine → chest → neck → head, plus arm/leg chains) is mandatory — VSeeFace/Warudo body tracking maps directly onto Unity's `HumanoidAvatar` bone naming convention. A non-standard skeleton will not track correctly even if it looks right when static.
- Weight painting (which vertices move with which bones) needs to be clean enough that the seam, ears, and any HOSHOKU-specific asymmetric geometry deform believably — this is exactly the kind of non-standard-anatomy problem Meshy's automatic rigging is least likely to get right without human review (see below).

### What Meshy can and can't do automatically

- **Can likely automate:** base mesh generation from reference images, basic texturing/PBR materials, and — per its own tooling — a first-pass humanoid rig via its rigging feature, plus separate multi-view reconstruction for better accuracy than single-image.
- **Likely needs manual follow-up:** facial blendshapes (Meshy's auto-rig is body/skeleton-focused, not a substitute for a sculpted blendshape set), any non-standard anatomy weight-painting cleanup (the seam and asymmetric ears are unusual enough that automatic weighting should be checked, not trusted blind), and the actual VRM packaging step (bone-mapping + blendshape-clip authoring), which is a separate Unity/UniVRM (or Blender VRM addon) pass Meshy does not perform itself.
- This validation requirement is the same one already logged in `HOSHOKU_VTUBER_STATE.md`'s resource policy: skeleton, weights, eyes, mouth, facial controls, blendshapes, and export format all need to be checked on any Meshy output, not assumed correct.

### VSeeFace / Warudo + tracking

- Both are free/low-cost VRM-loading runtimes with webcam or (for Warudo) additional iPhone ARKit tracking support, mapping tracked face/mouth movement onto the VRM's blendshapes in real time.
- Output goes to OBS the same way as the 2D track: window capture, or a virtual camera/NDI output the runtime provides.

### What's automatable vs. manual, 3D track

| Step | Automated | Manual |
| --- | --- | --- |
| Base mesh from reference images | Yes (Meshy) | N/A, though quality depends on reference quality (see turnaround gap) |
| Texturing | Yes (Meshy) | Cleanup/touch-up likely needed for non-standard details (seam, asymmetric fur colors) |
| Humanoid skeleton + first-pass rig | Partial (Meshy's rigging feature) | Weight-painting cleanup, especially around the seam and ears |
| Facial blendshapes | No | Yes — sculpted manually (Blender or similar) unless a paid rigging service/plugin is used |
| VRM packaging (bone mapping, expression clips) | Partial (UniVRM/Blender addon does the mechanical packaging) | Yes — someone has to run and configure that step |
| Face/mouth tracking at runtime | Yes (VSeeFace/Warudo) | N/A |

---

## Software actually available to this project right now

| Tool | Availability in this session | Notes |
| --- | --- | --- |
| OpenArt (image + video generation) | **Available** via MCP tools in this session | 6,227 credits, per the account snapshot in `HOSHOKU_VTUBER_STATE.md` |
| Meshy | **Not available as a tool in this session.** No Meshy MCP tool exists in this session's toolset (checked directly — no `Meshy` server or tool matched a search of available tools). Access must be verified outside this session (e.g. its own web login), not assumed from account history. | Do not treat "the project has a Meshy account" as equivalent to "this session can drive it" |
| Live2D Cubism, Blender, Unity/UniVRM, VTube Studio, VSeeFace, Warudo, OBS | **Not available as tools in this session** — these are desktop applications this session cannot install, launch, or operate | Any work in these tools happens outside this session, on your own machine |

Nothing above was installed, purchased, or configured. This is a capability inventory, not an action taken.

---

## Open technical questions this doesn't resolve

These depend on the visual verification queue and your own production preferences, not further research:

- Whether the humanoid rig should split the face into two coordinated halves (rabbit/fox) or one shared symmetric rig — depends on how the seam and mouth are ultimately designed.
- Whether asymmetric blinking (independent `blinkLeft`/`blinkRight`, matching the "rabbit eye first, then fox eye" motion already seen in OpenArt clips) is wanted for the final rig, in both 2D and 3D.
- Whether the project goes 2D-first, 3D-first, or both in parallel — this document treats them as parallel tracks but doesn't recommend an order.
