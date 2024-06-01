# NIKKE flavor colors

a Python script that lets you automagically capture all playable nikke's "flavor" colors.

## How?

0. Install requirements. There are probably some missing but I think that's it
    - Do `py -m pip install -r requirements.txt` in order to install some dependencies.
    - [Get Tesseract-OCR here!](https://tesseract-ocr.github.io/tessdoc/Downloads)
    - You're also gonna need to set up `.env`, you can use the `.env.example` file as an example.
1. Open NIKKE. (be sure to close the launcher to prevent window name confusion!)
    - Don't be on full screen, you're gonna need multiple windows up
    - I'd recommend NIKKE to atleast take up all of your desktop's height. The text recognition part for the name may mess up on smaller window sizes.
2. Head to the Nikkepedia, and select whatever Nikke you want to start with. You can just choose Emma as well.
    - When on a [NIKKE's profile screen](https://haxeflixel.is-terrible.com/6reOaDFj0.png), be sure that the [main part of the profile](https://haxeflixel.is-terrible.com/6reOlPatG.png) **isn't obstructed in any way**. If there is a window on top of the NIKKE window, the script won't be able to capture it.
    - Also, do not obstruct the [right arrow](https://haxeflixel.is-terrible.com/6reO_hPUh.png) as that will be clicked by your mouse to go to the next NIKKE.
3. Open an administrator Command Prompt. Just look up `cmd` and click "run as administrator" when it's on the side of the start menu.
4. Run `main.py` in the said administrator command prompt. Then:
    - Press enter.
    - **Immediately after pressing enter, click the NIKKE window immediately.**
5. Let it run it's course, it's going to stop immediately when it comes back to the Nikke you've first selected.
    - It creates 2 images: `color.png` and `name.png`, both containing screenshots of the screen.
    - It also creates `colors.json`, which is the dictionary of colors, with the key being the formatted name of the Nikke (e.g. `Anis: Sparkling Summer`) and the value being the hex code of the color.

## Warnings

**This *may* count as a macro software**, so NIKKE *may* ban you. I'm not entirely sure yet, but be on the lookout. <u>Use at your own risk</u>.

**The color may be ever-changing when rerunning it again**. NIKKE runs a weird image filter over everything, so colors may vary every once in a while.
