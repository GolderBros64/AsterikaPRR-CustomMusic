# AsterikaPRR-CustomMusic
Tool to easily insert custom songs in Asterika: Phantom Rose Refrain
## HOW TO USE (asterikamdEncrypt.py & AsterikaMusicInsert.exe)
[video once i make it :p]
- Download the prebuilt `.zip` from the releases (or the SourceCode if you're more comforable with that)
- Once downloaded, run the `.exe` (or `AsterikaMusicInsert.py` for SourceCode)
- On the Left Side, there's a section where you can encrypt songs, you require:
    - ### Song ID   
        - Internal ID the game uses to refer to the song, you need to fill this out for anything regarding songs
    - A .ogg for the main song
    - A .ogg for the preview (if you want) the preview only is long for 30 seconds and will loop each 30s
    - A .png (or .jpg) for the icon (automatically converts .png to .jpg since you can simply rename it, won't add any other converting methods, convert beforehand)
    - (Optional) a .asterika chart to package in the game (If not then the game will show the song, but pressing enter on it won't do anything)
- In the Middle there is the game install Location (Steam -> Browse local Files) you are **REQUIRED** to have bought the game, this **isn't** a piracy tool, please support the creator of the game, and this tool is only tested on the steam version.
    - If you have a clean copy of the game, you will need to press the `Backup Game` button, this will create `app_clean` and `app_mod` in the game's directory, this is done to ensure you don't have to reinstall the game to restore/un-mod it, **DO NOT DELETE ANY OF THESE FOLDERS** or the tool won't give you the option to mod the game.
    - Once backed up, you gain access to `Restore Clean Game` and `Patch Game`, `Restore Clean Game` uses the `app_clean` folder to repackage the game modless, `Patch Game` uses the `app_mod` instead.
- On the Right Side is the "Song Entry Editor" this is needed so the game can recognize the song, NOTE: The game recognizes the songs as basegame songs and will reward you with extra stickers for beating them.
    - ### Title
        - Any string, shows up after `enName`
    - ### En Title (internally enName)
        - Also any string, if declared will put `title` in brackets `(title)` after itself
    - ### Artist
        - Whoever made the song, shows up under the title in-game
    - ### Composer
        - Doesn't seem to do anything visually (toh i didn't look much further into it)
    - ### BPM
        - Pretty self explanatory
    - ### Ready Beats
        - how many beats before the game starts scoring you
    - ### Song Lenght
        - Doesn't seem to matter as the game seems to automatically change it (i'm assuming) you can either put how many beats it has or just the lenght in seconds (the game seems to utilize beats in hex format, but you can use decimal and it works just fine as this data is reread from the .asterika chart file)
    - ### End beat
        - At what beat should the game stop scoring the player
    - ### Initial Delay (in Seconds)
        - How many seconds to delay the song (before it atcually starts)
- ## Difficulty Tagging
    - This is till part of the right side, just that i had to add another frame
    - Tags, i will have another file (tags.md) once i've looked at all of them, since they use Internal Label names instead of plain text
        - ### Tags
            - You can insert multiple tags via tag1,tag2
        - ### Level
            - Difficulty level to show to the player on the menus
- ### Remove/Add entry
    - Adding an entry can only be done once all the required fields are filled (`Difficulty Tagging` must be filled out), it will edit the file called `index-(something, changes between version).js` in `app_mod/out/renderer/assets/`
    - Removing an entry only requires to fill out the `Song ID` field on the left side, NOTE: You must remove an entry in order to edit it, the order of entries doesn't seem to matter for anything
- ### Insert / Remove Files
    - To insert files, first you **must** use the `Encrypt Song` button, after that a folder named `EncryptedSongs` will be created next to the .exe (or .py for source code), it will insert all the encrypted files in it
        - How did i get the encryption key? it's inside the `index-(something, changes between version).js` in `app_clean/out/renderer/assets/`, and the encryption uses `xor` so we can do the same, it's stored next to `const DEFAULT_XOR_KEY_HEX=` (note that you must have unpacked the `app.asar` in `resources/app.asar` to get access to it, [function it uses](#extra-stuff-for-coders-and-such))
        - In HEX the key is: `0x4153544552494b4153555349434b657931` which is `ASTERIKASUSICKey1` in readable format, i dont know what else utilizes this key but in this case that's all i need it for
        - Note that a .preview.asterikamd is no different from a .asterikamd, it just declares if it should use it as the preview for the song
    - If you want to remove files, you have to first have filled out the `Song ID` field for the song you wanted to remove, then it will remove it, if one of the files is missing (beside the .asterika as that is optional) the program will give you the option to open the folder (as with most errors regarding files)

# asterikamdDecrypt.py
This file is just to decrypt a .asterikamd to a .ogg, i used it to test the encrypt function properly, isn't required with the script and as such is an extra you can download, to utilize it just run: `python asterikamdDecrypt.py` it will then ask you for a .asterikamd file (you must type the .asterikamd as well) it will then out put a .ogg (yes the name is not fully correct but eh, you know the name already if you actually played the game no?)

# Extra Stuff for coders and such
`xor` Function for how the game uses it
```js
function xorRange(c,d,f,j){
    if(j['length']===0x0)throw new Error('XOR key must not be empty');
    for(let l=d;l<f;l++){
        c[l]^=j[(l-d)%j['length']];
    }
}
```
