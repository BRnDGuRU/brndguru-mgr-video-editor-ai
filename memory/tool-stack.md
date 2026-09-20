# Tool Stack

> Last updated: 2026-09-20
> Install status, credentials, cost, and best-use for each tool in the video pipeline.

## Installed — Local

| Tool | Version | Path | Purpose | Credentials needed | Status |
|---|---|---|---|---|---|
| FFmpeg | 8.1.2 | system PATH | Core encode/assemble/captions/subtitle burn | No | ✅ Ready |
| MoviePy | 2.2.1 | pip | Programmatic editing | No | ✅ Ready |
| openai-whisper | 20250625 | pip | Transcription for clips + captions | No | ✅ Ready |
| faster-whisper | 1.2.1 | pip | Faster transcription alt | No | ✅ Ready |
| yt-dlp | 2026.8.19 | pip | Download footage from web | No | ✅ Ready |
| ffmpeg-python | 0.2.0 | pip | FFmpeg bindings | No | ✅ Ready |
| Torch | 2.14.0 | pip | ML runtime | No | ✅ Ready |
| Pillow | 11.3.0 | pip | Image ops | No | ✅ Ready |
| open-clip-torch | 3.3.0 | pip | Frame classification / smart crop | No | ✅ Ready |
| segment-anything | 1.0 | pip | Object segmentation / smart crop | No | ✅ Ready |
| ShortGPT | git clone | repos/ShortGPT | End-to-end shorts pipeline | EdgeTTS free / ElevenLabs key | ✅ Cloned — needs setup |
| OpenMontage | git clone | repos/OpenMontage | Agentic video production studio | Optional cloud API keys | ✅ Cloned — needs setup |
| video-use | git clone | repos/video-use | Conversation-driven editing | ElevenLabs Scribe key | ✅ Cloned — needs setup |
| kinocut | git clone | repos/kinocut | Guardrailed FFmpeg MCP + CLI | No | ✅ Cloned — needs setup |
| MoneyPrinterTurbo | git clone | repos/MoneyPrinterTurbo | One-keyword → HD short | AI keys | ✅ Cloned — needs setup |
| n8n-video-clipper | git clone | repos/n8n-video-clipper | Whisper+Gemini+FFmpeg → vertical clips | Gemini key optional | ✅ Cloned — needs setup |
| recut-cli | git clone | repos/recut-cli | Auto-clip → vertical shorts + dub | TTS key optional | ✅ Cloned — needs setup |
| VACE | git clone | repos/VACE | All-in-one video creation/editing | — | ✅ Cloned — needs setup |
| LivePortrait | git clone | repos/LivePortrait | Face animation / lip-sync | — | ✅ Cloned — needs setup |
| Remotion | git clone | repos/remotion | React code-to-video | Company license for >3 employees | ✅ Cloned — ⚠️ license check |
| HyperFrames | git clone | repos/hyperframes | HTML/CSS/GSAP → MP4 | No (free) / cloud API optional | ✅ Cloned + 15 skills loaded |
| hermes-agent | git clone | repos/hermes-agent | Agent reference + skill design | — | ✅ Cloned |

## Credentials Pending (1Password — video tool accounts)

| Service | Purpose | Status |
|---|---|---|
| ElevenLabs | Voiceover / TTS / Scribe transcription | 🔴 Not unlocked |
| HeyGen | AI avatar video | 🔴 Not unlocked |
| Canva | Thumbnails, end cards, static assets | 🔴 Not unlocked |
| RunwayML | Inpainting, object removal, green screen, gen-2 | 🔴 Not unlocked |
| Descript | Text-based editing, transcription, overdub | 🔴 Not unlocked |
| Opus Clip / Munch | Long-form → short-form repurposing | 🔴 Not unlocked |
| CapCut (Desktop/API) | Primary AI editing, auto-captions, templates | 🔴 Not unlocked |
| GHL | Track video deliverables per client | 🔴 Not unlocked |

## SaaS / Cloud (not local — eval only)

| Tool | Type | Role | Status |
|---|---|---|---|
| Google Flow | AI creative studio (web) | B-roll / image asset source | ⏸ Not configured |
| NotebookLM | Research / notes (web) | Brief digestion, script outlining | ⏸ Not configured |

## Cost Note

All local tools above are free to run. Cloud APIs charge per use. Ask Shivanshu before any paid seat or API usage spike.
