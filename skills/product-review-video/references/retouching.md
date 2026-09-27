# Color and optional retouching

This is optional stage 4, after scripts, voice, and the completed base video edit. Use it only when the user requests grading or beauty work. Keep a separate derivative of the base; stage 3 does not automatically apply these treatments. Do not infer permission for face or body reshaping from a generic request for a polished edit.

## Color

Normalize exposure and white balance between shots before adding a look. Retain natural skin and accurate product hues and material texture. Use gentle midtone contrast and detail enhancement to emphasize the person and product. Inspect black products for crushed detail and light clothing for clipped highlights.

Grade footage before rendering text so the typography is not blurred or recolored by skin treatment. Supplied product variant images may need to remain untouched to preserve their intended colors. Inspect the final composite, not only the processed source.

## Smoother skin and makeup without changing the face

- Preserve facial geometry, identity, expressions, eyes, nose, lips, brows, and jaw. Do not use face generation, substitution, or liquify when the user asks to retain the face.
- Track a selective skin mask. Apply restrained edge-preserving smoothing; retain texture and lighting. Protect feature boundaries and hair rather than blurring a rectangular face region.
- Add subtle cheek/lip tone only within appropriate masks, preserving texture and avoiding color leakage.
- If detection is unreliable, skip the treatment for that range or use a reliable manual mask. Do not apply a guessed mask. Check untreated/treated transitions for flicker.
- Review full-frame before/after pairs, face crops, and normal-speed playback. A good single frame does not establish temporal stability.

## Optional subtle body adjustment

Only attempt this when requested. Protect the entire head and face from geometric movement, including feathered mask edges. Restrict the adjustment to suitable body regions, with smooth spatial and temporal falloff; preserve hands, product geometry, footwear, and background lines.

A very small adjustment around 1–2% was sufficient in one edit; it is not a required setting. Disable it on shots where sitting, occlusion, product handling, or background geometry makes distortion likely. Leave the shot unchanged if a natural result is not possible.

When using a geometric remap, inspect and, where feasible, measure displacement in protected face regions: it should be zero. Also check the rendered result for wobble. “No face reshaping” does not mean unchanged face pixels: color and skin treatments can change pixels while retaining facial structure.

## Separate derivative

If an approved master is locked, make a new beauty manifest and processed assets rather than replacing the base. Preserve timing, narration, captions, headline layout, outfit joins, and ending unless requested otherwise. Record which treatments were applied or skipped. Keep processing reproducible, but do not reuse clip-specific masks or processing constants on unrelated footage without inspection.
