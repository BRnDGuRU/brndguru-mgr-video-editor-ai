# QA Checklist — Video Editor AI

> Run before every delivery. One row per asset. Fail = do not deliver until fixed.
> Log result in pending-deliverables.md.

## Per-Asset QA

| Check | Method | Pass criteria | Result |
|---|---|---|---|
| **Source integrity** | ffprobe source file | Codec, duration, resolution match expected | ☐ |
| **Rough cut complete** | Visual scan of timeline | No missing segments, all intended clips included | ☐ |
| **Cut pacing** | Watch full video | Cuts land on beat / natural breaks, no awkward holds | ☐ |
| **Audio sync** | Lip-sync check where applicable; clap/waveform align | Audio matches video within ~1 frame | ☐ |
| **Audio levels** | ffmpeg volumedetect / loudness | Dialog peak ~-6 to -3 dB, integrated loudness ~-16 LUFS (video) or -14 LUFS (social) | ☐ |
| **Noise floor** | Listen to silent sections | No hiss/hum; noisereduce applied if needed | ☐ |
| **Caption accuracy** | Spot-check 10 random caption segments vs source audio | >98% word accuracy, timing aligned | ☐ |
| **Caption style** | Visual check | Brand font/color/size, on-screen long enough to read, no overlap with key visuals | ☐ |
| **Brand kit applied** | Visual check vs brand-kits.md | Correct logo placement, colors, fonts, lower-third style per client | ☐ |
| **Thumbnail** | Visual check | High-CTR criteria: bold, readable at small size, brand-aligned, face/subject clear | ☐ |
| **Aspect ratio** | ffprobe / visual | Correct for destination: 9:16 / 1:1 / 16:9 / 4:5 | ☐ |
| **Resolution** | ffprobe | Matches target (e.g. 1080x1920 for 9:16, 1920x1080 for 16:9) | ☐ |
| **Frame rate** | ffprobe | Matches source or target spec (e.g. 30fps, 60fps) | ☐ |
| **No artifacts** | Full watch | No encoding artifacts, dropped frames, glitch cuts, black frames | ☐ |
| **Music bed** | Listen | Level balanced under dialog, no clashing with audio, correct length | ☐ |
| **Intro/outro** | Visual check | Correct duration, brand-consistent, no dead air at starts/ends | ☐ |
| **Export filename** | Check filename | Naming convention followed: `<client>_<asset>_<format>_<date>.<ext>` | ☐ |
| **Delivery destination** | Confirm | File in correct folder / uploaded to GHL / handed off | ☐ |

---

## Format-Specific Validation

| Format | Resolution | AR | FPS | Loudness target | Notes |
|---|---|---|---|---|---|
| YouTube 16:9 | 1920x1080 / 3840x2160 | 16:9 | 30/60 | -14 LUFS | — |
| Instagram Reel / TikTok 9:16 | 1080x1920 | 9:16 | 30/60 | -14 LUFS | Captions safe zone: center, avoid bottom 20% |
| Instagram Feed 1:1 | 1080x1080 | 1:1 | 30 | -14 LUFS | — |
| Instagram Feed 4:5 | 1080x1350 | 4:5 | 30 | -14 LUFS | — |
| Shorts / Reels cover | 1080x1920 (thumb) | 9:16 | — | — | JPEG/PNG, <2MB ideal |

---

## Caption Accuracy Spot-Check Protocol

1. Pick 10 random caption segments from the video (spread across start/middle/end).
2. Listen to source audio for each segment.
3. Compare caption text to what was actually said.
4. Count errors: wrong word, missing word, extra word, wrong timing.
5. Pass = 0-1 minor errors across 10 segments (>98% accuracy).
6. Fail = 2+ errors → regenerate captions with whisper at higher model size or manually correct.

---

## Audio Sync Check Protocol

1. Find a clear sync point (clap, mouth close-up, percussion hit).
2. Play video — audio and visual must land together.
3. If off, measure the gap. >1 frame (≈33ms at 30fps) = fail.
4. Fix: shift audio in ffmpeg with `-itsoffset` or re-render.

---

## Re-work Tracking

| Asset ID | QA fail reason | Fix applied | Re-QA date | Final |
|---|---|---|---|---|
| [fill per incident] | — | — | — | — |

Target: <5% re-works per delivery batch.
