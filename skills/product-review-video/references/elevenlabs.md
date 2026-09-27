# ElevenLabs voice workflow — stage 2

Use this branch after the script is settled and the user wants new narration. Supplied audio does not need generation. This is a connector/API workflow for an agent, not a bundled speech service. Updating or installing this skill alone does not authorize a voice-generation run.

## Collect the user's choices before generation

First check the current brief and prior answers. Reuse explicit choices; do not repeatedly ask for them. When choices are missing, show a small, relevant shortlist and ask for:

| Choice | What to present / record |
| --- | --- |
| Model | Available speech models that support the language and requested delivery; plain-language tradeoffs based on current capabilities. |
| Voice | Voice names, short descriptions, language/accent labels, and existing preview audio where available; preserve the returned voice ID. |
| Delivery | Language, accent or regional preference, conversational vs energetic style, pace, and pronunciation of brand names or unusual terms. |
| Takes | Desired number of alternatives; make the count explicit because it affects usage. |

Bundle unresolved choices into a concise question. For example: “Which model and voice would you like from these options? Also choose the delivery style, pace, and number of takes.” Give recommendations but wait for the user's selection. If the user says “choose for me,” select from verified options and record that delegation. A request for this choice-first workflow takes precedence over a generic skill's advice to automatically pick a voice.

Existing library previews can help the user choose without generating samples. Do not create a paid preview to populate a shortlist. Do not silently use a model, voice, take count, or accent that differs from the user's choice. Technical controls such as stability, similarity, speed, and style are model-dependent; ask about the desired sound rather than forcing users to tune raw numbers. Only offer and pass settings the current integration supports.

## Connected ElevenLabs tools

Prefer the available ElevenLabs connector for direct media generation. Read its installed `creative-studio` guidance when present, then inspect current tool schemas. These are tool suffixes; discover the actual namespace in the environment rather than hardcoding one.

| Task | Tool / behavior |
| --- | --- |
| Discover speech models | `creative_get_flow_node_types`; filter to speech/TTS models actually available in the workspace. |
| Discover voices | `creative_list_voices`; search from the user's language/style preferences. Use returned IDs or user-provided IDs, never memorized examples. |
| Check prompting and settings | `creative_get_model_guide` and `creative_get_model_schema` for the selected model and TTS node. |
| Estimate a selected run | `creative_generate_speech` with `estimate_only: true` where supported; use the chosen script, model, voice, and take count. This is not generated audio. |
| Generate selected narration | `creative_generate_speech` using the resolved choices. The prompt contains spoken text and only supported delivery tags, not visual directions. |
| Follow an existing run | Retain `flow_id`, `node_id`, and all `session_ids`. Use `creative_get_flow_run_status` with returned polling guidance, or the result view's progress. |
| Present completed takes | Use native results or `creative_show_flow_results` when available; let the user select among requested alternatives. |

Read the generation tool's current variation default and include that count in the user's choice. Pass the user's chosen count explicitly. Do not silently accept a multi-take default or purchase additional samples. Respect existing usage limits and authorization; provide a current estimate when the selected run needs a spend decision. Do not invent prices or add a second confirmation after the user has already resolved the choices and authorized that run.

Do not call generation again to poll or retry a pending run: that can start another charged run. On failure or timeout, inspect the existing run and explain the state. Stop dependent editing if no usable narration exists; a new chargeable attempt or changed settings requires the user's instruction unless already covered by an explicit retry request.

If narration will feed another generation inside an ElevenLabs flow, create the flow first and reuse it for all related nodes. A local video editor only needs the chosen audio file; do not create extra cloud video or lip-sync work merely to obtain narration. Do not design, clone, or save a new custom voice unless requested.

## API fallback and setup

If the connector is unavailable but an authorized ElevenLabs API setup exists, use the official SDK/API and the installed `text-to-speech` skill when available. Consult current documentation rather than copying fixed model IDs or settings from another version:

- [List models](https://elevenlabs.io/docs/api-reference/models/list): discover supported speech models and languages.
- [Text-to-speech overview](https://elevenlabs.io/docs/overview/capabilities/text-to-speech): check current capabilities and limits.
- [Create speech with timing](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps): generate audio with alignment when supported by the chosen model and interface.

Use `ELEVENLABS_API_KEY` through the environment or the host's secret storage for API access. Never request that the key be pasted into the script, committed, put in a manifest, or shown in logs. A connected plugin can use its own authenticated account; the user should not need a second API key just for that path.

If neither path is configured, explain that generating speech needs an ElevenLabs connection or API setup and let the user connect it or supply narration. Continue useful script/footage inspection, but do not claim voice generation succeeded or build final speech timing from an estimate. Do not silently switch providers.

## Handoff to stage 3

1. Resolve the selected take. A single usable take can proceed after quality review; ask which take to use when multiple alternatives were requested unless the user delegated selection.
2. Inspect pronunciation, missing/repeated words, pauses, artifacts, and duration. Check Vietnamese accents and brand pronunciation where relevant. Record unavailable listening checks accurately.
3. Save the selected audio as a local project asset through the supported download/export path. Retain the original generated file. A short-lived media URL is not a portable editing dependency.
4. Record the script version or hash, model ID, voice ID/name, actual supported settings, language/style intent, take count, selected generation ID, and file path in the private job notes. Do not copy credentials or signed URLs into public documentation.
5. Use returned alignment if valid, or align the actual audio locally. Account for any trimming, pauses, or retiming before deriving subtitles. Never estimate final cues from character count.
6. Pass the chosen script, audio, and timings into the base video edit. Any later script or voice change invalidates affected timings and must be reflected in the edit.
