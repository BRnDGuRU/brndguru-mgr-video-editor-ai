import asyncio
import os
import subprocess
from edge_tts import Communicate

VOICE = 'en-US-GuyNeural'

script = [
    (0.5,  "BRND GURU."),
    (2.5,  "We build Brands. Systems. Growth."),
    (7.0,  "The old way. Leaking leads. Empty pipelines."),
    (11.0, "Growth you can't see. Effort you can't scale."),
    (14.5, "The BRND GURU way. One partner. Six growth engines."),
    (18.0, "Built. Run. Optimized. By us."),
    (20.5, "Six growth engines. Pick where you're stuck."),
    (24.0, "LinkedIn Rev Engine. AI-powered outbound that books qualified B2B appointments on autopilot. One thousand one hundred ninety nine dollars setup, plus three hundred nineteen a month."),
    (30.5, "100K Email Rev Engine. Cold email infrastructure and AI-run campaigns that fill your calendar at scale."),
    (35.0, "E-Commerce Growth Engine. Store, ads and retention automation that turns traffic into repeat revenue."),
    (39.5, "Local Business Growth Engine. Lead generation and follow-up automation for local service businesses. Zero setup fee."),
    (43.5, "Coach Growth B2B Engine. Offer positioning, VSL funnels, LinkedIn-led client acquisition for coaches."),
    (47.0, "Receptionist AI Engine. The AI that answers calls, books appointments and follows up. Twenty-four seven."),
    (51.0, "Proof. Real results from real brands."),
    (53.0, "Nature Empowered. Ten times revenue. Three point two times ROAS."),
    (55.5, "Your growth partner. Not just a service provider."),
    (58.0, "Book a free strategy call at brndguru dot com."),
]

async def main():
    voicedir = "voice_lines"
    os.makedirs(voicedir, exist_ok=True)
    files = []
    for i, (ts, text) in enumerate(script):
        fname = os.path.join(voicedir, f"line_{i:02d}.wav")
        comm = Communicate(text, VOICE)
        await comm.save(fname)
        files.append(fname)
        dur = len(text) * 0.06 + 0.4
        print(f"Line {i:02d} [{ts:.1f}s] ({dur:.1f}s est): {text[:60]}")

    # Concat
    concat_list = os.path.join(voicedir, "list.txt")
    with open(concat_list, "w") as f:
        for fn in files:
            f.write(f"file '{os.path.abspath(fn)}'\n")

    out = "voiceline_full.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list, "-c", "copy", out],
        check=True
    )
    total = os.path.getsize(out)
    print(f"\nDone: {out} ({total/1024:.1f} KB)")
    for fn in files:
        os.remove(fn)
    os.remove(concat_list)
    try:
        os.rmdir(voicedir)
    except OSError:
        pass

asyncio.run(main())
