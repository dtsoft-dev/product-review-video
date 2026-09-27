# Product Review Video

A Codex skill for creating finished review and affiliate videos for TikTok, Reels, and Facebook: **Scripts → Voice → Video edit → Optional color / beauty**.

It guides the agent through footage selection, text design, movement-matched transitions, review, and delivery. The guidance incorporates fixes from iterative editing: floating headline panels, jumping subtitles, disconnected CTAs, awkward outfit changes, and repeated closing actions.

**This repository contains agent instructions and an installer.** It does not include a video renderer, private footage, narration, fonts, a sample commercial campaign, or a paid-service subscription. The skill works with the editing tools available in your project. Installing it does not install those tools or render a video by itself.

## The workflow

| Stage | What happens |
| --- | --- |
| **1. Scripts** | Use your final script or draft and settle the spoken copy, hook, product evidence, and CTA. |
| **2. Voice** | Use your recording, or ask you to choose an available ElevenLabs model and voice, delivery style, pace, and take count before generation. Resolve the selected narration and its timing. |
| **3. Video edit** | Build the complete base video with our headline, subtitle, demonstration, zoom, outfit-transition, color-gallery, and ending-continuity improvements. No new beauty processing or creative color grading. |
| **4. Optional color / beauty** | If requested, create a separate color-graded or subtly retouched derivative. Preserve facial structure, product appearance, and the completed edit. |

Completed stages are reused during revisions. Changing a headline does not trigger a new script or voice. If stage 4 is not requested, the base video is the finished deliverable; it is not blocked on an enhancement decision.

## Install in Codex

### Option 1 — Ask Codex

Paste this into Codex if the built-in skill installer is available:

```text
Use $skill-installer to install the product-review-video skill from
https://github.com/dtsoft-dev/product-review-video/tree/main/skills/product-review-video
```

Restart Codex after installation. If the skill already exists, use the update procedure below to preserve a backup of your local copy.

### Option 2 — Terminal

Requirements: Git and Python 3.9 or newer. The installer uses only Python's standard library.

```sh
git clone https://github.com/dtsoft-dev/product-review-video.git
cd product-review-video
python3 scripts/install.py
```

On Windows, use `py -3 scripts/install.py` if `python3` is unavailable. The same substitution applies to the other Python commands below.

The default destination is `$CODEX_HOME/skills/product-review-video` when `CODEX_HOME` is set; otherwise it is `~/.codex/skills/product-review-video`. To choose a different skills directory:

```sh
python3 scripts/install.py --skills-dir /path/to/agent/skills
```

Restart Codex, then invoke `$product-review-video` in a new chat. You can verify the files exist at the destination printed by the installer. A custom destination must be one your agent actually discovers.

### Update an existing installation

From your repository clone:

```sh
git pull --ff-only
python3 scripts/install.py --update
```

The installer refuses to overwrite an existing skill without `--update`. Updates move the old installation into a timestamped `skill-backups/` folder beside the skills directory, then install the new copy. Local customizations remain in that backup; they are not automatically merged. Backups stay outside the discovery directory to avoid duplicate skills.

To uninstall, remove only the installed `product-review-video` folder from your agent's skills directory and restart Codex. Your editing projects and backup copies remain separate.

## Connect ElevenLabs for generated voice

This is an optional integration for stage 2. You do not need ElevenLabs when supplying your own narration.

1. Install and connect an ElevenLabs plugin/connector in your agent that exposes speech generation, available voices, and models. The skill installer does not install or authenticate that connector.
2. Ask the skill to generate narration after the script is settled. It discovers available models and voices, shows relevant choices and existing previews, and asks for your selection before generation. If you already supplied your choices or explicitly say “choose for me,” it uses that instruction.
3. Choose language/accent, delivery style, pace, and the number of takes as needed. Available technical settings depend on the model and interface. The skill records your choices and does not silently generate extra alternatives.
4. Select a take when you requested alternatives. The chosen audio is saved into the editing project and aligned to the actual speech before the video edit begins.

For an existing API-based setup, the agent can instead use the official ElevenLabs SDK/API with `ELEVENLABS_API_KEY` configured privately in its environment or secret storage. Do not paste keys into prompts or commit them. See [ElevenLabs text-to-speech documentation](https://elevenlabs.io/docs/overview/capabilities/text-to-speech) for service capabilities and [the integration reference](skills/product-review-video/references/elevenlabs.md) for discovery, generation, status tracking, and audio handoff.

Generating speech uses your ElevenLabs account and credits. Installing this skill does not start generation. No fixed catalog of voices or models is bundled: choices are discovered from the connected account. If no connector or API access exists, the agent asks you to connect ElevenLabs or provide a recording.

## Use it

Provide the project path, footage, voiceover, script, target format, and any visual reference. The skill inspects the existing project before choosing tools or creating outputs.

```text
Use $product-review-video in /path/to/my-product-project.
Use the videos in inputs/videos and the supplied voice.mp3 and script.
Create a 9:16 review video with readable subtitles, restrained transitions,
and detail zooms. Deliver the MP4, SRT, cover, and editable project.
```

To write a script and generate narration:

```text
Use $product-review-video in /path/to/my-product-project.
First draft a Vietnamese affiliate review script using my product details.
Then use ElevenLabs: show me available model and voice choices before
generating, and ask about delivery style, pace, and number of takes.
Once the voice is selected, complete the video edit with fixed subtitles,
reference-style headlines, smooth outfit changes, and a continuous ending.
Skip color grading and beauty for now; keep those as an optional next stage.
```

An example revision request:

```text
Use $product-review-video to revise the latest approved version.
Center the headline horizontally, remove its solid background panel,
and match the reference typography. Keep all subtitles at one lower-screen
position with a subtle outline and translucent backing. Change outfits on
the head turn, and keep the final presenter shot through the CTA without
repeating the lower-and-raise action.
```

Vietnamese example:

```text
Dùng $product-review-video chỉnh bản mới nhất trong thư mục dự án.
Headline ở giữa theo style ảnh tham chiếu; phụ đề luôn cùng một vị trí
phía dưới, nền mờ và viền chữ vừa đủ đọc. Chuyển outfit đúng nhịp quay đầu.
Đoạn nói đi giày thoải mái dùng cảnh ngồi xuống đeo giày. Giữ cảnh cuối
liền mạch, không lặp động tác đưa giày xuống rồi đưa lên.
```

For an optional beauty derivative:

```text
Lock the approved version and create a separate beauty version.
Soften skin and makeup subtly, improve color, and preserve facial shape
and identity. Only apply very slight body adjustment where it stays natural.
Keep the narration, text layout, transitions, and ending unchanged.
```

## What the skill covers

| Area | Editing guidance |
| --- | --- |
| Scripts | Settle spoken copy before voice generation; keep shot directions separate. |
| ElevenLabs voice | Ask for model and voice selection, discover current options, resolve takes, and align the chosen audio before editing. |
| Headlines | Exact requested wording, centered layout when requested, reference font hierarchy, contrast without detached panels. |
| Subtitles | Speech-aligned phrases, fixed lower-screen anchor, consistent region height, restrained stroke and translucent backing. |
| Hook text | Avoid a duplicate opening subtitle when the headline intentionally carries the hook. |
| Callouts and CTA | Keep approved styles and connect the text to the visible scene. |
| Outfit transitions | Match head/body turn direction, framing, and timing; review each join in motion. |
| Product evidence | Align putting-on demonstrations, detail zooms, and real variant images to narration. |
| Ending continuity | Remove repeated, reversed, or overlapping actions instead of concealing them with dissolves. |
| Optional color / beauty | Separate stage after the base edit: natural color, selective skin treatment, protected facial geometry, body adjustment only when requested. |
| Delivery | Final MP4, captions, cover, portable edit, review notes, and checks on the actual export. |
| Version management | Lock approved masters, create separate derivatives, preserve dependencies, and remove old versions only when requested. |

The sample fonts and subtitle measurements in the typography reference are adjustable examples. They are not mandatory branding or guaranteed platform-safe margins. The skill does not promise virality or fabricate reviews, endorsements, prices, or product claims.

## Editing environment

The installation itself needs no rendering dependencies. Producing videos requires an agent with local file/tool access and a suitable editor or renderer. Existing project configuration takes precedence.

- FFmpeg and FFprobe are useful for media inspection, working copies, and export checks.
- A Remotion project needs its own Node dependencies, browser renderer, compositions, and applicable license. This repository does not supply that project. See [Remotion's documentation](https://www.remotion.dev/docs/).
- If `remotion-best-practices` is installed, the skill uses it when developing Remotion compositions; it is optional.
- Retouching needs appropriate local processing or editor capabilities. The skill supplies guidance, not a universal face/body filter or bundled model.

Use existing voiceover by default. External generation, paid services, and social publishing are not required to start. A reference image helps match styling, but missing optional references should not block useful editing.

## Repository layout

```text
skills/product-review-video/
  SKILL.md
  agents/openai.yaml
  references/
    elevenlabs.md
    typography.md
    continuity.md
    retouching.md
    delivery.md
scripts/install.py
tests/test_install.py
```

The entrypoint loads only relevant references for each task. The repository contains no private media or hardcoded personal workspace paths.

## Validation

Run the installer tests without changing your installed skills:

```sh
python3 -m unittest discover -s tests -v
```

They check a fresh install, refusal to overwrite, preservation of local changes in update backups, custom destinations, and protection of symlinked installations. Installer tests do not assess video quality; the skill requires review of the actual edited output.

## License

[MIT](LICENSE). Media, fonts, and software you use in an editing project have their own licenses.
