# Review, delivery, and versioning

## Review the edit and the file

Before rendering, validate source ranges, font loading, missing assets, final frame count after overlaps, and caption timestamps. Use the existing project's validator when available.

Review a preview in motion, then check representative frames in the final export:

- Opening title on each background it crosses; correct wording, font hierarchy, contrast, and no duplicated hook subtitle when intentionally suppressed.
- Stable subtitle anchor, accent marks, phone-size readability, translucent backing, and no UI/product obstruction.
- Sitting/putting-on action aligned to the comfort line; rejected source ranges absent.
- Every outfit join with continuous turn direction and no doubled faces or shoes.
- Detail zoom endpoints; genuine color variants synchronized to the color line.
- CTA carried by the intended scene; no off-camera reset, duplicated lower/raise action, reverse loop, or unintended frozen ending.
- For retouching: original face structure, product geometry, background stability, and treatment consistency over time.

Check the exported file's dimensions, duration, frame rate, streams, and full decode. Detect black gaps and unexpected freezes; distinguish a designed gallery or still hold from a defect. Measure loudness and true peak. Roughly −16 to −14 LUFS integrated and at most −1 dBTP are possible starting targets, not platform requirements. Listen to intelligibility, music balance, and edit points where supported; disclose if direct listening or playback was unavailable.

Do not infer “viral” performance from editing polish. Deliver an accessible, credible edit and describe only work and checks actually completed.

## Portable delivery

Include the requested final MP4, SRT, selected cover, and editable project. The editable package needs its manifests, relevant source/processed assets, local fonts and licenses, pinned dependencies, and run instructions; a JSON file alone is not a portable project. If a captions-off version retains titles, label it accordingly. A text-free version must remove all text layers.

Use new revision names for new exports. Keep a short review note describing the approved base, changes, checks, and material limitations. Do not label a version approved merely because it rendered successfully.

## Lock an approved version

When requested, copy or identify the self-contained approved delivery and record a SHA-256 manifest for the MP4, cover, captions, and editable archive. Make the files read-only where supported and mark the version clearly. Read-only permissions are a protection against accidental edits, not immutable storage.

Create derivatives beside the master with distinct names and a base-version reference. Verify the master's recorded hashes after packaging the derivative. Keep enough original and working assets to reproduce both versions.

## Remove old versions only when requested

Inventory active manifests, renderers, footage, fonts, and shared assets before cleanup. Version numbers in asset paths do not prove the assets are unused. Trace dependencies from every retained job, including fonts and supplemental media.

Move superseded deliveries and unused working files to the OS Trash or a clearly identified recoverable archive when appropriate. Do not delete original footage or active dependencies as part of revision cleanup. Do not include synced reference sources in cleanup. Record what moved and tell the user whether removal is recoverable or permanent. Validate the retained jobs afterward.
