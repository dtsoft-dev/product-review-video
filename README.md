# Product Review Video

A Codex skill for turning supplied product footage, narration, and scripts into finished review and affiliate videos for TikTok, Reels, and Facebook.

It guides the agent through footage selection, text design, movement-matched transitions, review, and delivery. The guidance incorporates fixes from iterative editing: floating headline panels, jumping subtitles, disconnected CTAs, awkward outfit changes, and repeated closing actions.

**This repository contains agent instructions and an installer.** It does not include a video renderer, private footage, narration, fonts, a sample commercial campaign, or a paid-service subscription. The skill works with the editing tools available in your project. Installing it does not install those tools or render a video by itself.

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

## Use it

Provide the project path, footage, voiceover, script, target format, and any visual reference. The skill inspects the existing project before choosing tools or creating outputs.

```text
Use $product-review-video in /path/to/my-product-project.
Use the videos in inputs/videos and the supplied voice.mp3 and script.
Create a 9:16 review video with readable subtitles, restrained transitions,
and detail zooms. Deliver the MP4, SRT, cover, and editable project.
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
| Headlines | Exact requested wording, centered layout when requested, reference font hierarchy, contrast without detached panels. |
| Subtitles | Speech-aligned phrases, fixed lower-screen anchor, consistent region height, restrained stroke and translucent backing. |
| Hook text | Avoid a duplicate opening subtitle when the headline intentionally carries the hook. |
| Callouts and CTA | Keep approved styles and connect the text to the visible scene. |
| Outfit transitions | Match head/body turn direction, framing, and timing; review each join in motion. |
| Product evidence | Align putting-on demonstrations, detail zooms, and real variant images to narration. |
| Ending continuity | Remove repeated, reversed, or overlapping actions instead of concealing them with dissolves. |
| Optional retouching | Selective skin treatment, natural color, protected facial geometry, cautious body adjustment only when requested. |
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
